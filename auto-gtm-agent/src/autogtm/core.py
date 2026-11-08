"""Core pipeline for the Auto-GTM Agent. Deterministic, offline, testable.

No network calls, no auto-send. Drafts are produced for human approval.
Scoring, drafting, reply triage and the learning loop are pure functions
over CSV / dict inputs so a personal AI agent (or a human) can run them
anywhere.
"""
from __future__ import annotations

import csv
import io
import re
from dataclasses import dataclass, field, asdict

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

# ---------------------------------------------------------------- config

@dataclass
class Segment:
    id: str
    name: str
    roles: list[str]
    company_keywords: list[str]
    regions: list[str]
    min_employees: int = 1
    max_employees: int = 100000
    offer: str = ""
    angle: str = ""
    subject: str = "{company} x {sender_company}"

@dataclass
class Config:
    sender_name: str
    sender_title: str
    sender_company: str
    presentation_url: str = ""
    booking_url: str = ""
    banned_words: list[str] = field(default_factory=list)
    allowed_proof: list[str] = field(default_factory=list)
    segments: list[Segment] = field(default_factory=list)
    cost_per_email_usd: float = 0.04
    scale_below_cost_per_hot_usd: float = 10.0
    pause_above_cost_per_hot_usd: float = 15.0
    pause_min_sent: int = 250

    @classmethod
    def from_dict(cls, d: dict) -> "Config":
        segs = [Segment(**s) for s in d.get("segments", [])]
        rest = {k: v for k, v in d.items() if k != "segments"}
        return cls(segments=segs, **rest)

def check_banned(text: str, banned: list[str]) -> list[str]:
    low = text.lower()
    return [w for w in banned if w.lower() in low]

# ---------------------------------------------------------------- leads

@dataclass
class Lead:
    first_name: str
    last_name: str = ""
    email: str = ""
    title: str = ""
    company: str = ""
    region: str = ""
    employees: int = 0
    industry: str = ""
    signal: str = ""  # one true, checkable personal line (funding, launch, hire...)
    segment_id: str = ""

    @property
    def valid_email(self) -> bool:
        return bool(EMAIL_RE.match(self.email or ""))

def import_leads(csv_text: str, suppression: set[str] | None = None) -> tuple[list[Lead], list[str]]:
    """Parse leads CSV. Returns (leads, problems). Dedupes by email,
    drops suppressed and invalid addresses, never invents data."""
    suppression = {s.lower() for s in (suppression or set())}
    seen, leads, problems = set(), [], []
    for i, row in enumerate(csv.DictReader(io.StringIO(csv_text)), start=2):
        row = {(k or "").strip().lower(): (v or "").strip() for k, v in row.items()}
        email = row.get("email", "").lower()
        if not email or email in seen:
            if email:
                problems.append(f"row {i}: duplicate {email}")
            continue
        seen.add(email)
        if email in suppression:
            problems.append(f"row {i}: suppressed {email}")
            continue
        try:
            employees = int(row.get("employees", "0") or 0)
        except ValueError:
            employees = 0
        lead = Lead(
            first_name=row.get("first_name", ""), last_name=row.get("last_name", ""),
            email=email, title=row.get("title", ""), company=row.get("company", ""),
            region=row.get("region", ""), employees=employees,
            industry=row.get("industry", ""), signal=row.get("signal", ""),
            segment_id=row.get("segment_id", ""),
        )
        if not lead.valid_email:
            problems.append(f"row {i}: invalid email {email!r} dropped")
            continue
        leads.append(lead)
    return leads, problems

# ---------------------------------------------------------------- ICP scoring

def score_lead(lead: Lead, cfg: Config) -> dict:
    """Score a lead against every segment. Returns best segment, fit 0-100,
    tier (A >=75, B >=50, C below) and the reasons, so a human can audit it."""
    best = {"segment_id": "", "fit": 0, "reasons": []}
    for seg in cfg.segments:
        fit, reasons = 0, []
        title = lead.title.lower()
        if any(r.lower() in title for r in seg.roles):
            fit += 40; reasons.append(f"role match: {lead.title}")
        blob = f"{lead.company} {lead.industry}".lower()
        hits = [k for k in seg.company_keywords if k.lower() in blob]
        if hits:
            fit += 25; reasons.append(f"company/industry match: {', '.join(hits)}")
        if lead.region and any(r.lower() in lead.region.lower() for r in seg.regions):
            fit += 20; reasons.append(f"region match: {lead.region}")
        if seg.min_employees <= lead.employees <= seg.max_employees and lead.employees:
            fit += 10; reasons.append(f"size in range: {lead.employees}")
        if lead.signal:
            fit += 5; reasons.append("has a checkable personal signal")
        if fit > best["fit"]:
            best = {"segment_id": seg.id, "fit": fit, "reasons": reasons}
    tier = "A" if best["fit"] >= 75 else "B" if best["fit"] >= 50 else "C"
    return {**best, "tier": tier, "email": lead.email, "company": lead.company}

# ---------------------------------------------------------------- drafting

def draft_email(lead: Lead, cfg: Config, segment: Segment) -> dict:
    """Draft ONE personal email. Status is always draft_needs_approval.
    Refuses to draft without a personal signal, because a generic blast
    is not personalisation. Fails closed on banned words."""
    if not lead.signal:
        return {"email": lead.email, "status": "blocked_no_signal",
                "reason": "No checkable personal signal for this lead. Research one first."}
    subject = segment.subject.format(company=lead.company, sender_company=cfg.sender_company)
    proof = f" {cfg.allowed_proof[0]}" if cfg.allowed_proof else ""
    body = (
        f"Hi {lead.first_name},\n\n"
        f"{lead.signal} Most teams I talk to are under pressure to show real outcomes from AI, not just pilots.\n\n"
        f"I run {cfg.sender_company}.{proof} {segment.angle}\n\n"
        f"Open to a 20-minute look at whether {segment.offer} makes sense for {lead.company}?\n\n"
        f"{cfg.sender_name}\n{cfg.sender_title}, {cfg.sender_company}"
        + (f"\n{cfg.presentation_url}" if cfg.presentation_url else "")
    )
    hits = check_banned(subject + "\n" + body, cfg.banned_words)
    if hits:
        return {"email": lead.email, "status": "blocked_banned_word", "reason": f"Banned words: {hits}"}
    return {"email": lead.email, "company": lead.company, "segment_id": segment.id,
            "subject": subject, "body": body, "status": "draft_needs_approval"}

# ---------------------------------------------------------------- reply triage

HOT = ["pricing", "price", "send the deck", "send a deck", "book", "call", "tuesday", "thursday",
       "monday", "wednesday", "friday", "talk to my", "intro", "interested", "sounds good"]
ESCALATE = ["contract", "legal", "nda", "procurement", "security review", "dpa", "invoice"]
NEGATIVE = ["unsubscribe", "remove me", "not interested", "stop emailing", "no thanks"]
OOO = ["out of office", "on leave", "annual leave", "will reply when"]

def triage_reply(text: str, cfg: Config) -> dict:
    """Classify a reply. Pricing/contract replies ALWAYS escalate to a human
    and are never auto-answered. That rule outranks 'hot'."""
    low = text.lower()
    if any(k in low for k in NEGATIVE):
        return {"class": "negative", "action": "suppress_contact_no_followup"}
    if any(k in low for k in OOO):
        return {"class": "out_of_office", "action": "retry_after_return_date"}
    if any(k in low for k in ESCALATE):
        return {"class": "hot_escalate", "action": "forward_to_human_draft_only_do_not_auto_send"}
    if any(k in low for k in HOT):
        action = "send_booking_link" if cfg.booking_url else "ask_human_for_booking_link"
        return {"class": "hot", "action": action}
    return {"class": "warm_unclear", "action": "forward_to_human"}

# ---------------------------------------------------------------- learning loop

def learn(results: list[dict], cfg: Config) -> list[dict]:
    """results rows: segment_id, sent, hot_leads, spend_usd (optional).
    Mirrors Explee: scale cheap segments, pause expensive ones, but only
    after enough volume to mean anything (pause_min_sent)."""
    out = []
    for r in results:
        sent = int(r.get("sent", 0)); hot = int(r.get("hot_leads", 0))
        spend = float(r.get("spend_usd", sent * cfg.cost_per_email_usd))
        cph = round(spend / hot, 2) if hot else None
        hot_rate = round(hot / sent, 4) if sent else 0.0
        if hot and cph is not None and cph < cfg.scale_below_cost_per_hot_usd and hot_rate >= 0.03:
            verdict = "scale"
        elif sent >= cfg.pause_min_sent and (not hot or hot_rate < 0.01 or (cph is not None and cph > cfg.pause_above_cost_per_hot_usd)):
            verdict = "pause"
        else:
            verdict = "keep_testing"
        out.append({"segment_id": r.get("segment_id", ""), "sent": sent, "hot_leads": hot,
                    "spend_usd": round(spend, 2), "cost_per_hot_usd": cph,
                    "hot_rate": hot_rate, "verdict": verdict})
    return out

def leads_to_csv(rows: list[dict]) -> str:
    if not rows:
        return ""
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
    return buf.getvalue()

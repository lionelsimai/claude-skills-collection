"""CLI for the Auto-GTM Agent.

Commands:
  validate   check a config (banned words, segments, booking link)
  score      score a leads CSV against the ICP segments
  draft      draft personal emails for tier A/B leads (approval-gated)
  triage     classify a reply text
  learn      scale / pause / keep-testing verdicts from campaign results
  demo       run the whole pipeline on the bundled sample leads

Sending is deliberately NOT a command in v0.1. Drafts go to a human.
A future sender must sit behind an explicit approval flag and a
separate warmed sending domain, never the sender's primary domain.
"""
from __future__ import annotations

import argparse, csv, io, json, sys
from pathlib import Path

try:
    import yaml
except ImportError:  # minimal fallback: configs in tests use JSON-compatible YAML subset via json
    yaml = None

from .core import Config, Lead, import_leads, score_lead, draft_email, triage_reply, learn

def load_config(path: str) -> Config:
    text = Path(path).read_text()
    if yaml:
        data = yaml.safe_load(text)
    else:
        data = json.loads(text)
    return Config.from_dict(data)

def _read_csv(path: str) -> str:
    return Path(path).read_text()

def cmd_validate(args):
    cfg = load_config(args.config)
    issues = []
    if not cfg.segments: issues.append("no segments defined")
    if not cfg.booking_url: issues.append("booking_url is empty: hot replies cannot be booked automatically")
    for s in cfg.segments:
        if not s.offer: issues.append(f"segment {s.id}: no offer")
    print(json.dumps({"sender": f"{cfg.sender_name} / {cfg.sender_company}",
                      "segments": [s.id for s in cfg.segments],
                      "banned_words": cfg.banned_words, "issues": issues}, indent=2))
    return 0

def _scored(cfg, leads_csv):
    leads, problems = import_leads(leads_csv)
    rows = []
    for lead in leads:
        s = score_lead(lead, cfg)
        rows.append((lead, s))
    return rows, problems

def cmd_score(args):
    cfg = load_config(args.config)
    rows, problems = _scored(cfg, _read_csv(args.leads))
    out = [s for _, s in sorted(rows, key=lambda x: -x[1]["fit"])]
    print(json.dumps({"scored": out, "problems": problems}, indent=2))
    return 0

def cmd_draft(args):
    cfg = load_config(args.config)
    rows, problems = _scored(cfg, _read_csv(args.leads))
    seg_by_id = {s.id: s for s in cfg.segments}
    drafts = []
    for lead, s in rows:
        if s["tier"] == "C" or not s["segment_id"]:
            drafts.append({"email": lead.email, "status": "skipped_low_fit", "fit": s["fit"]})
            continue
        drafts.append(draft_email(lead, cfg, seg_by_id[s["segment_id"]]))
    if args.out:
        Path(args.out).write_text(json.dumps(drafts, indent=2))
        print(f"Wrote {len(drafts)} drafts to {args.out} (all need human approval)")
    else:
        print(json.dumps({"drafts": drafts, "problems": problems}, indent=2))
    return 0

def cmd_triage(args):
    cfg = load_config(args.config)
    print(json.dumps(triage_reply(args.text, cfg), indent=2))
    return 0

def cmd_learn(args):
    cfg = load_config(args.config)
    rows = list(csv.DictReader(io.StringIO(_read_csv(args.results))))
    print(json.dumps(learn(rows, cfg), indent=2))
    return 0

def cmd_demo(args):
    here = Path(__file__).resolve().parents[2]
    cfg_path = args.config or str(here / "config" / "the-ai-capitol.yaml")
    leads_path = args.leads or str(here / "examples" / "leads-sample.csv")
    cfg = load_config(cfg_path)
    rows, problems = _scored(cfg, _read_csv(leads_path))
    seg_by_id = {s.id: s for s in cfg.segments}
    drafts, scores = [], []
    for lead, s in rows:
        scores.append(s)
        if s["tier"] in ("A", "B") and s["segment_id"]:
            drafts.append(draft_email(lead, cfg, seg_by_id[s["segment_id"]]))
    sample_results = [
        {"segment_id": "a_ai_vendors_apac", "sent": 300, "hot_leads": 34},
        {"segment_id": "b_finance_sg", "sent": 280, "hot_leads": 2},
        {"segment_id": "c_video_ai", "sent": 120, "hot_leads": 9},
    ]
    report = {"config": cfg_path, "problems": problems, "scores": scores,
              "drafts": drafts,
              "triage_examples": {
                  "pricing": triage_reply("Sounds good, send pricing and can we do Tuesday 2pm?", cfg),
                  "contract": triage_reply("Please send the contract and NDA for legal review.", cfg),
                  "negative": triage_reply("Not interested, please unsubscribe.", cfg)},
              "learning_demo (illustrative sample numbers, not real results)": learn(sample_results, cfg)}
    out = Path(args.out or (here / "demo-output" / "demo-report.json"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2))
    print(f"Demo complete. Report: {out}")
    print(f"Leads scored: {len(scores)} | Drafts: {sum(1 for d in drafts if d['status']=='draft_needs_approval')}"
          f" | Blocked/skipped drafts: {sum(1 for d in drafts if d['status']!='draft_needs_approval')}")
    return 0

def main(argv=None):
    p = argparse.ArgumentParser(prog="autogtm", description="Auto-GTM Agent v0.1")
    p.add_argument("--config", default="config/the-ai-capitol.yaml")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    s = sub.add_parser("score"); s.add_argument("--leads", required=True)
    d = sub.add_parser("draft"); d.add_argument("--leads", required=True); d.add_argument("--out", default="")
    t = sub.add_parser("triage"); t.add_argument("--text", required=True)
    l = sub.add_parser("learn"); l.add_argument("--results", required=True)
    dm = sub.add_parser("demo"); dm.add_argument("--leads", default=""); dm.add_argument("--config", default=""); dm.add_argument("--out", default="")
    args = p.parse_args(argv)
    fn = {"validate": cmd_validate, "score": cmd_score, "draft": cmd_draft,
          "triage": cmd_triage, "learn": cmd_learn, "demo": cmd_demo}[args.cmd]
    return fn(args)

if __name__ == "__main__":
    sys.exit(main())

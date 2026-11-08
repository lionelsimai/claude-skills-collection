import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from autogtm.core import Config, Segment, Lead, import_leads, score_lead, draft_email, triage_reply, learn

def cfg():
    return Config(
        sender_name="Lionel Sim", sender_title="Founder", sender_company="The AI Capitol",
        presentation_url="https://www.theaicapitol.com/presentation", booking_url="",
        banned_words=["beachhead"], allowed_proof=["We run OpenBuilder, 8,000+ builders."],
        segments=[Segment(id="a", name="A", roles=["Head of Partnerships"],
                          company_keywords=["ai"], regions=["Singapore"],
                          min_employees=50, max_employees=5000,
                          offer="an annual partner slot", angle="We run the room.")])

def test_dedupe_and_invalid():
    leads, problems = import_leads("email,first_name\n a@x.com,A\n a@x.com,A2\n bad,B\n")
    assert len(leads) == 1 and len(problems) == 2

def test_score_tier_a():
    lead = Lead(first_name="Maya", email="m@x.com", title="Head of Partnerships APAC",
                company="Voice AI Co", region="Singapore", employees=400, industry="ai", signal="Saw a launch.")
    s = score_lead(lead, cfg())
    assert s["fit"] == 100 and s["tier"] == "A" and s["segment_id"] == "a"

def test_draft_blocked_without_signal():
    lead = Lead(first_name="Tom", email="t@x.com", title="Head of Partnerships", company="AI Co")
    d = draft_email(lead, cfg(), cfg().segments[0])
    assert d["status"] == "blocked_no_signal"

def test_draft_needs_approval_and_no_banned_word():
    lead = Lead(first_name="Maya", email="m@x.com", title="Head of Partnerships", company="AI Co",
                signal="Saw AI Co opened a Singapore office.")
    d = draft_email(lead, cfg(), cfg().segments[0])
    assert d["status"] == "draft_needs_approval" and "beachhead" not in d["body"].lower()

def test_triage_escalates_contract_over_hot():
    r = triage_reply("Interested, please send pricing and the contract for legal.", cfg())
    assert r["class"] == "hot_escalate"

def test_triage_negative_suppresses():
    assert triage_reply("Not interested, unsubscribe.", cfg())["action"] == "suppress_contact_no_followup"

def test_learn_scale_and_pause():
    out = {r["segment_id"]: r for r in learn([
        {"segment_id": "cheap", "sent": 300, "hot_leads": 40},
        {"segment_id": "expensive", "sent": 300, "hot_leads": 2},
        {"segment_id": "early", "sent": 50, "hot_leads": 0}], cfg())}
    assert out["cheap"]["verdict"] == "scale"
    assert out["expensive"]["verdict"] == "pause"
    assert out["early"]["verdict"] == "keep_testing"

"""Handler for Sponsor Deliverable Tracker (sponsor-deliverable-tracker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "checklist",
  "items": [
    "logo placed",
    "speaking slot",
    "lead list shared",
    "social post",
    "post-event report"
  ],
  "slug": "sponsor-deliverable-tracker",
  "name": "Sponsor Deliverable Tracker"
}
def run(args):
    return run_engine(CONFIG, args or {})

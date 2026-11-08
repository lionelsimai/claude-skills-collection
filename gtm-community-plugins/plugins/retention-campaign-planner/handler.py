"""Handler for Retention Campaign Planner (retention-campaign-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "plan",
  "items": [
    "segment at-risk members",
    "personal outreach",
    "value reminder",
    "win-back offer",
    "measure return rate"
  ],
  "slug": "retention-campaign-planner",
  "name": "Retention Campaign Planner"
}
def run(args):
    return run_engine(CONFIG, args or {})

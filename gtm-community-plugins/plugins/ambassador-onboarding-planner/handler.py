"""Handler for Ambassador Onboarding Planner (ambassador-onboarding-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "plan",
  "items": [
    "welcome call",
    "starter kit",
    "first task",
    "introduce to members",
    "30-day check-in"
  ],
  "slug": "ambassador-onboarding-planner",
  "name": "Ambassador Onboarding Planner"
}
def run(args):
    return run_engine(CONFIG, args or {})

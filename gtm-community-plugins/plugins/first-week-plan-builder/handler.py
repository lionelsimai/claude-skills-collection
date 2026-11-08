"""Handler for First-week Plan Builder (first-week-plan-builder). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "plan",
  "items": [
    "day 1 welcome",
    "day 2 resource",
    "day 3 intro prompt",
    "day 5 event invite",
    "day 7 check-in"
  ],
  "slug": "first-week-plan-builder",
  "name": "First-week Plan Builder"
}
def run(args):
    return run_engine(CONFIG, args or {})

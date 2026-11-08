"""Handler for Engagement Campaign Planner (engagement-campaign-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "plan",
  "items": [
    "pick theme",
    "week 1 prompt",
    "week 2 challenge",
    "week 3 spotlight",
    "week 4 event tie-in"
  ],
  "slug": "engagement-campaign-planner",
  "name": "Engagement Campaign Planner"
}
def run(args):
    return run_engine(CONFIG, args or {})

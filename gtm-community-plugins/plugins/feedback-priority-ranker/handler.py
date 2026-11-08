"""Handler for Feedback Priority Ranker (feedback-priority-ranker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "prioritize",
  "items": [
    "mentions",
    "severity",
    "member impact",
    "effort to fix",
    "strategic fit"
  ],
  "slug": "feedback-priority-ranker",
  "name": "Feedback Priority Ranker"
}
def run(args):
    return run_engine(CONFIG, args or {})

"""Handler for Lead Priority Ranker (lead-priority-ranker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "prioritize",
  "items": [
    "fit score",
    "intent score",
    "deal size",
    "recency",
    "effort to reach"
  ],
  "slug": "lead-priority-ranker",
  "name": "Lead Priority Ranker"
}
def run(args):
    return run_engine(CONFIG, args or {})

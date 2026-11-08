"""Handler for Waitlist Priority Ranker (waitlist-priority-ranker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "prioritize",
  "items": [
    "member tenure",
    "rsvp speed",
    "past attendance",
    "contribution",
    "effort"
  ],
  "slug": "waitlist-priority-ranker",
  "name": "Waitlist Priority Ranker"
}
def run(args):
    return run_engine(CONFIG, args or {})

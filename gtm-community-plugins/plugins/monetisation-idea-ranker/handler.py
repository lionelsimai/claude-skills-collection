"""Handler for Monetisation Idea Ranker (monetisation-idea-ranker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "prioritize",
  "items": [
    "revenue potential",
    "member goodwill",
    "effort",
    "sponsor fit",
    "speed to launch"
  ],
  "slug": "monetisation-idea-ranker",
  "name": "Monetisation Idea Ranker"
}
def run(args):
    return run_engine(CONFIG, args or {})

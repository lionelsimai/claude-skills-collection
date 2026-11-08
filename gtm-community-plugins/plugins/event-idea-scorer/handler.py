"""Handler for Event Idea Scorer (event-idea-scorer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "score",
  "items": [
    "member demand",
    "speaker availability",
    "cost",
    "sponsor fit",
    "format novelty"
  ],
  "slug": "event-idea-scorer",
  "name": "Event Idea Scorer"
}
def run(args):
    return run_engine(CONFIG, args or {})

"""Handler for Content Performance Scorer (content-performance-scorer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "score",
  "items": [
    "views",
    "reactions",
    "comments",
    "shares",
    "saves"
  ],
  "slug": "content-performance-scorer",
  "name": "Content Performance Scorer"
}
def run(args):
    return run_engine(CONFIG, args or {})

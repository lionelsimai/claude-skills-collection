"""Handler for Content Idea Scorer (content-idea-scorer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "score",
  "items": [
    "audience relevance",
    "originality",
    "proof available",
    "effort to produce",
    "distribution fit"
  ],
  "slug": "content-idea-scorer",
  "name": "Content Idea Scorer"
}
def run(args):
    return run_engine(CONFIG, args or {})

"""Handler for Reply Intent Classifier (reply-intent-classifier). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "classify",
  "items": [
    "interested",
    "meeting request",
    "objection",
    "not now",
    "not relevant",
    "unsubscribe",
    "pricing question"
  ],
  "slug": "reply-intent-classifier",
  "name": "Reply Intent Classifier"
}
def run(args):
    return run_engine(CONFIG, args or {})

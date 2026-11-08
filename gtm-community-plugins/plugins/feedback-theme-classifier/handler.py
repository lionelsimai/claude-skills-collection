"""Handler for Feedback Theme Classifier (feedback-theme-classifier). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "classify",
  "items": [
    "content quality",
    "networking",
    "logistics",
    "speakers",
    "food and venue",
    "other"
  ],
  "slug": "feedback-theme-classifier",
  "name": "Feedback Theme Classifier"
}
def run(args):
    return run_engine(CONFIG, args or {})

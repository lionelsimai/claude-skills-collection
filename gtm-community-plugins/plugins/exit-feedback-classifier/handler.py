"""Handler for Exit Feedback Classifier (exit-feedback-classifier). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "classify",
  "items": [
    "no time",
    "not relevant",
    "cost",
    "found alternative",
    "life change",
    "negative experience"
  ],
  "slug": "exit-feedback-classifier",
  "name": "Exit Feedback Classifier"
}
def run(args):
    return run_engine(CONFIG, args or {})

"""Handler for New Member Intro Classifier (new-member-intro-classifier). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "classify",
  "items": [
    "builder",
    "founder",
    "operator",
    "student",
    "job seeker",
    "investor",
    "other"
  ],
  "slug": "new-member-intro-classifier",
  "name": "New Member Intro Classifier"
}
def run(args):
    return run_engine(CONFIG, args or {})

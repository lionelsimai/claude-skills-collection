"""Handler for Proposal Win/Loss Classifier (proposal-win-loss-classifier). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "classify",
  "items": [
    "price",
    "budget frozen",
    "competitor chosen",
    "timing",
    "no response",
    "champion left"
  ],
  "slug": "proposal-win-loss-classifier",
  "name": "Proposal Win/Loss Classifier"
}
def run(args):
    return run_engine(CONFIG, args or {})

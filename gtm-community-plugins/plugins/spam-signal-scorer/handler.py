"""Handler for Spam Signal Scorer (spam-signal-scorer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "score",
  "items": [
    "link density",
    "new account",
    "repeated text",
    "keyword stuffing",
    "report count"
  ],
  "slug": "spam-signal-scorer",
  "name": "Spam Signal Scorer"
}
def run(args):
    return run_engine(CONFIG, args or {})

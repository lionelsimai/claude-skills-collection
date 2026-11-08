"""Handler for Quote Follow-up Drafter (quote-follow-up-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "quote reference",
    "decision blocker help",
    "deadline reminder",
    "next step"
  ],
  "slug": "quote-follow-up-drafter",
  "name": "Quote Follow-up Drafter"
}
def run(args):
    return run_engine(CONFIG, args or {})

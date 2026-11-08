"""Handler for Objection Response Drafter (objection-response-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "acknowledge objection",
    "supplied evidence",
    "reframe",
    "low-risk next step"
  ],
  "slug": "objection-response-drafter",
  "name": "Objection Response Drafter"
}
def run(args):
    return run_engine(CONFIG, args or {})

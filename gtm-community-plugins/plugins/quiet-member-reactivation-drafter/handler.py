"""Handler for Quiet Member Reactivation Drafter (quiet-member-reactivation-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "personal note",
    "what they missed supplied by user",
    "low-effort invite",
    "opt out line"
  ],
  "slug": "quiet-member-reactivation-drafter",
  "name": "Quiet Member Reactivation Drafter"
}
def run(args):
    return run_engine(CONFIG, args or {})

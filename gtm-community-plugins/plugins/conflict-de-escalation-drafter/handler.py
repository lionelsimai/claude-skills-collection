"""Handler for Conflict De-escalation Drafter (conflict-de-escalation-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "calm opening",
    "shared ground",
    "rule reminder",
    "private follow-up offer"
  ],
  "slug": "conflict-de-escalation-drafter",
  "name": "Conflict De-escalation Drafter"
}
def run(args):
    return run_engine(CONFIG, args or {})

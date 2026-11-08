"""Handler for Buyer Persona Gap Audit (buyer-persona-gap-audit). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "audit",
  "items": [
    "job title",
    "pain points",
    "buying triggers",
    "objections",
    "preferred channels",
    "decision role"
  ],
  "slug": "buyer-persona-gap-audit",
  "name": "Buyer Persona Gap Audit"
}
def run(args):
    return run_engine(CONFIG, args or {})

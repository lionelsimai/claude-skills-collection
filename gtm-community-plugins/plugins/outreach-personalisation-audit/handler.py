"""Handler for Outreach Personalisation Audit (outreach-personalisation-audit). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "audit",
  "items": [
    "personal signal",
    "named company",
    "role relevance",
    "specific detail",
    "call to action"
  ],
  "slug": "outreach-personalisation-audit",
  "name": "Outreach Personalisation Audit"
}
def run(args):
    return run_engine(CONFIG, args or {})

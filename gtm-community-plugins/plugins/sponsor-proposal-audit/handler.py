"""Handler for Sponsor Proposal Audit (sponsor-proposal-audit). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "audit",
  "items": [
    "audience evidence",
    "deliverables",
    "pricing",
    "dates",
    "terms",
    "call to action"
  ],
  "slug": "sponsor-proposal-audit",
  "name": "Sponsor Proposal Audit"
}
def run(args):
    return run_engine(CONFIG, args or {})

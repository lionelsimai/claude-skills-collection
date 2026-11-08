"""Handler for Proposal Structure Builder (proposal-structure-builder). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "problem",
    "outcomes",
    "scope",
    "deliverables",
    "timeline",
    "investment",
    "terms"
  ],
  "slug": "proposal-structure-builder",
  "name": "Proposal Structure Builder"
}
def run(args):
    return run_engine(CONFIG, args or {})

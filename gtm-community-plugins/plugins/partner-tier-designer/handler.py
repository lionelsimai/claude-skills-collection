"""Handler for Partner Tier Designer (partner-tier-designer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "plan",
  "items": [
    "define entry tier",
    "define annual tier",
    "price the gap",
    "list deliverables per tier",
    "set upgrade trigger"
  ],
  "slug": "partner-tier-designer",
  "name": "Partner Tier Designer"
}
def run(args):
    return run_engine(CONFIG, args or {})

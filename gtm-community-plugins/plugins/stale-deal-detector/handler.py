"""Handler for Stale Deal Detector (stale-deal-detector). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "checklist",
  "items": [
    "last activity date",
    "next step",
    "stage age",
    "owner assigned",
    "close date updated"
  ],
  "slug": "stale-deal-detector",
  "name": "Stale Deal Detector"
}
def run(args):
    return run_engine(CONFIG, args or {})

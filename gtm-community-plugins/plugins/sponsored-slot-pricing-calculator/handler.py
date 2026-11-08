"""Handler for Sponsored Slot Pricing Calculator (sponsored-slot-pricing-calculator). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "analyze",
  "items": [
    "audience size",
    "expected impressions",
    "base rate",
    "premium factor",
    "package price"
  ],
  "slug": "sponsored-slot-pricing-calculator",
  "name": "Sponsored Slot Pricing Calculator"
}
def run(args):
    return run_engine(CONFIG, args or {})

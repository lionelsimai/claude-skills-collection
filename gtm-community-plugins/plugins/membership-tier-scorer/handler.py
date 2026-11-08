"""Handler for Membership Tier Scorer (membership-tier-scorer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "score",
  "items": [
    "value delivered",
    "price fit",
    "exclusivity",
    "delivery cost",
    "support load"
  ],
  "slug": "membership-tier-scorer",
  "name": "Membership Tier Scorer"
}
def run(args):
    return run_engine(CONFIG, args or {})

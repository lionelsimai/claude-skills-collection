"""Handler for Sponsor Fit Scorer (sponsor-fit-scorer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "score",
  "items": [
    "audience match",
    "brand alignment",
    "budget fit",
    "category exclusivity",
    "activation interest"
  ],
  "slug": "sponsor-fit-scorer",
  "name": "Sponsor Fit Scorer"
}
def run(args):
    return run_engine(CONFIG, args or {})

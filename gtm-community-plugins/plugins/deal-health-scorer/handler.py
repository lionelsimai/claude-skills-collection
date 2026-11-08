"""Handler for Deal Health Scorer (deal-health-scorer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "score",
  "items": [
    "days since contact",
    "next step set",
    "champion engaged",
    "economic buyer known",
    "close date realistic"
  ],
  "slug": "deal-health-scorer",
  "name": "Deal Health Scorer"
}
def run(args):
    return run_engine(CONFIG, args or {})

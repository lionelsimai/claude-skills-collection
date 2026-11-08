"""Handler for NPS Calculator (nps-calculator). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "analyze",
  "items": [
    "promoters",
    "passives",
    "detractors",
    "total responses",
    "nps score"
  ],
  "slug": "nps-calculator",
  "name": "NPS Calculator"
}
def run(args):
    return run_engine(CONFIG, args or {})

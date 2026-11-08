"""Handler for Sequence Cadence Planner (sequence-cadence-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "plan",
  "items": [
    "day 1 email",
    "day 3 bump",
    "day 7 value email",
    "day 12 linkedin touch",
    "day 21 break-up"
  ],
  "slug": "sequence-cadence-planner",
  "name": "Sequence Cadence Planner"
}
def run(args):
    return run_engine(CONFIG, args or {})

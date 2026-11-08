"""Handler for Lookalike Seed Planner (lookalike-seed-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "plan",
  "items": [
    "select seed accounts",
    "extract shared traits",
    "exclude existing customers",
    "build search criteria",
    "validate sample size"
  ],
  "slug": "lookalike-seed-planner",
  "name": "Lookalike Seed Planner"
}
def run(args):
    return run_engine(CONFIG, args or {})

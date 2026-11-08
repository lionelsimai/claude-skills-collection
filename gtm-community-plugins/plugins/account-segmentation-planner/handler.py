"""Handler for Account Segmentation Planner (account-segmentation-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "plan",
  "items": [
    "define segment criteria",
    "rank accounts by fit",
    "assign segment tiers",
    "name segment owners",
    "set review cadence"
  ],
  "slug": "account-segmentation-planner",
  "name": "Account Segmentation Planner"
}
def run(args):
    return run_engine(CONFIG, args or {})

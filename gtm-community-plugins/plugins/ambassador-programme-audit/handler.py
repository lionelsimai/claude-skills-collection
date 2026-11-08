"""Handler for Ambassador Programme Audit (ambassador-programme-audit). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "audit",
  "items": [
    "selection criteria",
    "onboarding",
    "activity tracking",
    "recognition",
    "rewards",
    "exit process"
  ],
  "slug": "ambassador-programme-audit",
  "name": "Ambassador Programme Audit"
}
def run(args):
    return run_engine(CONFIG, args or {})

"""Handler for Cohort Retention Reporter (cohort-retention-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "analyze",
  "items": [
    "month 0 members",
    "month 1 retained",
    "month 3 retained",
    "month 6 retained",
    "retention curve"
  ],
  "slug": "cohort-retention-reporter",
  "name": "Cohort Retention Reporter"
}
def run(args):
    return run_engine(CONFIG, args or {})

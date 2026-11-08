"""Handler for Monthly Report Builder (monthly-report-builder). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "headline metric",
    "growth",
    "engagement highlight supplied by user",
    "challenges",
    "next month priority"
  ],
  "slug": "monthly-report-builder",
  "name": "Monthly Report Builder"
}
def run(args):
    return run_engine(CONFIG, args or {})

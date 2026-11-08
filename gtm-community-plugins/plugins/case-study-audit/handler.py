"""Handler for Case Study Audit (case-study-audit). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "audit",
  "items": [
    "client permission",
    "problem",
    "approach",
    "measured result",
    "quote",
    "dates"
  ],
  "slug": "case-study-audit",
  "name": "Case Study Audit"
}
def run(args):
    return run_engine(CONFIG, args or {})

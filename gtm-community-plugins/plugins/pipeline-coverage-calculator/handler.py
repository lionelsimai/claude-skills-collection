"""Handler for Pipeline Coverage Calculator (pipeline-coverage-calculator). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "analyze",
  "items": [
    "open pipeline",
    "target",
    "coverage ratio",
    "weighted pipeline",
    "gap"
  ],
  "slug": "pipeline-coverage-calculator",
  "name": "Pipeline Coverage Calculator"
}
def run(args):
    return run_engine(CONFIG, args or {})

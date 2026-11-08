"""Handler for Experiment Priority Ranker (experiment-priority-ranker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "prioritize",
  "items": [
    "expected impact",
    "confidence",
    "effort",
    "learning value",
    "speed to result"
  ],
  "slug": "experiment-priority-ranker",
  "name": "Experiment Priority Ranker"
}
def run(args):
    return run_engine(CONFIG, args or {})

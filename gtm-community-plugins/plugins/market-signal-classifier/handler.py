"""Handler for Market Signal Classifier (market-signal-classifier). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "classify",
  "items": [
    "funding",
    "expansion",
    "hiring",
    "leadership change",
    "technology adoption",
    "no signal"
  ],
  "slug": "market-signal-classifier",
  "name": "Market Signal Classifier"
}
def run(args):
    return run_engine(CONFIG, args or {})

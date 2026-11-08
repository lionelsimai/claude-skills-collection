"""Handler for Intent Signal Scorer (intent-signal-scorer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "score",
  "items": [
    "pricing page visits",
    "comparison searches",
    "repeat visits",
    "content depth",
    "recency"
  ],
  "slug": "intent-signal-scorer",
  "name": "Intent Signal Scorer"
}
def run(args):
    return run_engine(CONFIG, args or {})

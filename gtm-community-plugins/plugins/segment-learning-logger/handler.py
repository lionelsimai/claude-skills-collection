"""Handler for Segment Learning Logger (segment-learning-logger). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "segment",
    "result",
    "evidence",
    "decision scale or pause",
    "next test"
  ],
  "slug": "segment-learning-logger",
  "name": "Segment Learning Logger"
}
def run(args):
    return run_engine(CONFIG, args or {})

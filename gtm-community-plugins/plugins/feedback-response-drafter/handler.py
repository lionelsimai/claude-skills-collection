"""Handler for Feedback Response Drafter (feedback-response-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "thank them",
    "specific point",
    "what will change supplied by user",
    "timeline"
  ],
  "slug": "feedback-response-drafter",
  "name": "Feedback Response Drafter"
}
def run(args):
    return run_engine(CONFIG, args or {})

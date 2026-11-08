"""Handler for Win-back Drafter (win-back-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "acknowledge absence",
    "what is new supplied by user",
    "personal invite",
    "no pressure close"
  ],
  "slug": "win-back-drafter",
  "name": "Win-back Drafter"
}
def run(args):
    return run_engine(CONFIG, args or {})

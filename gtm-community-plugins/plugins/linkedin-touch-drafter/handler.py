"""Handler for LinkedIn Touch Drafter (linkedin-touch-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "shared context",
    "specific observation",
    "useful resource",
    "open question"
  ],
  "slug": "linkedin-touch-drafter",
  "name": "LinkedIn Touch Drafter"
}
def run(args):
    return run_engine(CONFIG, args or {})

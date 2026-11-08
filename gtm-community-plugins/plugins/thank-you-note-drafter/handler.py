"""Handler for Thank-you Note Drafter (thank-you-note-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "specific contribution",
    "audience impact supplied by user",
    "photo or recording link",
    "future invite"
  ],
  "slug": "thank-you-note-drafter",
  "name": "Thank-you Note Drafter"
}
def run(args):
    return run_engine(CONFIG, args or {})

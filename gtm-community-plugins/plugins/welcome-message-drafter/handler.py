"""Handler for Welcome Message Drafter (welcome-message-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "member name supplied by user",
    "first step",
    "introduce-yourself prompt",
    "key resource"
  ],
  "slug": "welcome-message-drafter",
  "name": "Welcome Message Drafter"
}
def run(args):
    return run_engine(CONFIG, args or {})

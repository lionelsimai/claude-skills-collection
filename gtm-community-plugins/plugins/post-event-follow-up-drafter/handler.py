"""Handler for Post-event Follow-up Drafter (post-event-follow-up-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "thank you",
    "highlight supplied by user",
    "recording link",
    "feedback ask",
    "next event"
  ],
  "slug": "post-event-follow-up-drafter",
  "name": "Post-event Follow-up Drafter"
}
def run(args):
    return run_engine(CONFIG, args or {})

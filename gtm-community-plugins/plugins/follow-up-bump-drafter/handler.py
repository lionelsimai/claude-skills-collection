"""Handler for Follow-up Bump Drafter (follow-up-bump-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "thread reference",
    "new value point",
    "choice question",
    "easy opt out"
  ],
  "slug": "follow-up-bump-drafter",
  "name": "Follow-up Bump Drafter"
}
def run(args):
    return run_engine(CONFIG, args or {})

"""Handler for LinkedIn Post Drafter (linkedin-post-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "hook",
    "supplied insight",
    "supplied example",
    "lesson",
    "question to readers"
  ],
  "slug": "linkedin-post-drafter",
  "name": "LinkedIn Post Drafter"
}
def run(args):
    return run_engine(CONFIG, args or {})

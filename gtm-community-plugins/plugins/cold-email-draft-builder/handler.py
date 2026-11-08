"""Handler for Cold Email Draft Builder (cold-email-draft-builder). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "subject line",
    "personal signal",
    "problem statement",
    "relevant proof supplied by user",
    "soft call to action"
  ],
  "slug": "cold-email-draft-builder",
  "name": "Cold Email Draft Builder"
}
def run(args):
    return run_engine(CONFIG, args or {})

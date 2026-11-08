"""Handler for Speaker Outreach Drafter (speaker-outreach-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "event context",
    "audience supplied by user",
    "topic fit",
    "logistics",
    "next step"
  ],
  "slug": "speaker-outreach-drafter",
  "name": "Speaker Outreach Drafter"
}
def run(args):
    return run_engine(CONFIG, args or {})

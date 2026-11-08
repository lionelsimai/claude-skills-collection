"""Handler for Event Lead Capture Checklist (event-lead-capture-checklist). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "checklist",
  "items": [
    "consent wording",
    "badge scan process",
    "qualifying question",
    "offer hook",
    "follow-up owner",
    "same-day upload"
  ],
  "slug": "event-lead-capture-checklist",
  "name": "Event Lead Capture Checklist"
}
def run(args):
    return run_engine(CONFIG, args or {})

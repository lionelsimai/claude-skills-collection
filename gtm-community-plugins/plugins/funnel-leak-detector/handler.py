"""Handler for Funnel Leak Detector (funnel-leak-detector). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "checklist",
  "items": [
    "visit to signup",
    "signup to reply",
    "reply to meeting",
    "meeting to proposal",
    "proposal to close"
  ],
  "slug": "funnel-leak-detector",
  "name": "Funnel Leak Detector"
}
def run(args):
    return run_engine(CONFIG, args or {})

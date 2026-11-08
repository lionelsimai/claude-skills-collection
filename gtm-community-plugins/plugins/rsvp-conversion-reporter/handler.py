"""Handler for RSVP Conversion Reporter (rsvp-conversion-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "analyze",
  "items": [
    "registrations",
    "check-ins",
    "show rate",
    "waitlist",
    "no-shows"
  ],
  "slug": "rsvp-conversion-reporter",
  "name": "RSVP Conversion Reporter"
}
def run(args):
    return run_engine(CONFIG, args or {})

"""Handler for Event Run Sheet Checklist (event-run-sheet-checklist). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "checklist",
  "items": [
    "venue confirmed",
    "speakers confirmed",
    "av tested",
    "registration list",
    "signage",
    "photographer briefed"
  ],
  "slug": "event-run-sheet-checklist",
  "name": "Event Run Sheet Checklist"
}
def run(args):
    return run_engine(CONFIG, args or {})

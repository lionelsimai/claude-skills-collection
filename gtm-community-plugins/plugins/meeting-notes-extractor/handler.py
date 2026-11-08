"""Handler for Meeting Notes Extractor (meeting-notes-extractor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "audit",
  "items": [
    "decision",
    "action item",
    "owner",
    "deadline",
    "risk",
    "next meeting"
  ],
  "slug": "meeting-notes-extractor",
  "name": "Meeting Notes Extractor"
}
def run(args):
    return run_engine(CONFIG, args or {})

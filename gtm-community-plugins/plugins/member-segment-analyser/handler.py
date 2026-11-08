"""Handler for Member Segment Analyser (member-segment-analyser). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "classify",
  "items": [
    "power user",
    "regular",
    "occasional",
    "lurker",
    "at risk"
  ],
  "slug": "member-segment-analyser",
  "name": "Member Segment Analyser"
}
def run(args):
    return run_engine(CONFIG, args or {})

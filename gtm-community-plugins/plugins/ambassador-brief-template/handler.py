"""Handler for Ambassador Brief Template (ambassador-brief-template). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "campaign goal",
    "key message supplied by user",
    "assets",
    "do and do not",
    "deadline"
  ],
  "slug": "ambassador-brief-template",
  "name": "Ambassador Brief Template"
}
def run(args):
    return run_engine(CONFIG, args or {})

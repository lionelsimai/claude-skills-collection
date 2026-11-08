"""Handler for Speaker Fit Scorer (Community) (speaker-fit-scorer-community). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "score",
  "items": [
    "topic relevance",
    "audience level",
    "talk experience",
    "diversity of perspective",
    "availability"
  ],
  "slug": "speaker-fit-scorer-community",
  "name": "Speaker Fit Scorer (Community)"
}
def run(args):
    return run_engine(CONFIG, args or {})

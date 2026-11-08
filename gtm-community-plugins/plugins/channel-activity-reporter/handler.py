"""Handler for Channel Activity Reporter (channel-activity-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "analyze",
  "items": [
    "posts",
    "replies",
    "unique contributors",
    "unanswered posts",
    "response time hours"
  ],
  "slug": "channel-activity-reporter",
  "name": "Channel Activity Reporter"
}
def run(args):
    return run_engine(CONFIG, args or {})

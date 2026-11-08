"""Handler for Reply SLA Tracker (reply-sla-tracker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "analyze",
  "items": [
    "replies received",
    "replies answered",
    "in time",
    "in late",
    "average response hours"
  ],
  "slug": "reply-sla-tracker",
  "name": "Reply SLA Tracker"
}
def run(args):
    return run_engine(CONFIG, args or {})

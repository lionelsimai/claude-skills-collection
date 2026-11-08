"""Handler for Campaign Metrics Reporter (campaign-metrics-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "analyze",
  "items": [
    "sent",
    "opened",
    "replied",
    "meetings",
    "cost per meeting"
  ],
  "slug": "campaign-metrics-reporter",
  "name": "Campaign Metrics Reporter"
}
def run(args):
    return run_engine(CONFIG, args or {})

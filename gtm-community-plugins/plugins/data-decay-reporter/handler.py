"""Handler for Data Decay Reporter (data-decay-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "analyze",
  "items": [
    "records checked",
    "stale records",
    "job changes detected",
    "bounced emails",
    "decay rate"
  ],
  "slug": "data-decay-reporter",
  "name": "Data Decay Reporter"
}
def run(args):
    return run_engine(CONFIG, args or {})

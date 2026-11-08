"""Handler for Lead List Deduper (lead-list-deduper). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "analyze",
  "items": [
    "total records",
    "unique records",
    "duplicate records",
    "duplicate rate",
    "domains represented"
  ],
  "slug": "lead-list-deduper",
  "name": "Lead List Deduper"
}
def run(args):
    return run_engine(CONFIG, args or {})

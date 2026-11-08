"""Handler for Co-marketing Planner (co-marketing-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "plan",
  "items": [
    "joint audience",
    "shared asset",
    "channel split",
    "owner per side",
    "success metric"
  ],
  "slug": "co-marketing-planner",
  "name": "Co-marketing Planner"
}
def run(args):
    return run_engine(CONFIG, args or {})

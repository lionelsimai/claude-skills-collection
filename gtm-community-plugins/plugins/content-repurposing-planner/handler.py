"""Handler for Content Repurposing Planner (content-repurposing-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "plan",
  "items": [
    "pick anchor asset",
    "extract clips",
    "extract quotes",
    "write short post",
    "schedule newsletter section"
  ],
  "slug": "content-repurposing-planner",
  "name": "Content Repurposing Planner"
}
def run(args):
    return run_engine(CONFIG, args or {})

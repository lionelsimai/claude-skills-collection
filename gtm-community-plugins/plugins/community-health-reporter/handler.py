"""Handler for Community Health Reporter (community-health-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "analyze",
  "items": [
    "total members",
    "active members",
    "active rate",
    "new members",
    "churned members"
  ],
  "slug": "community-health-reporter",
  "name": "Community Health Reporter"
}
def run(args):
    return run_engine(CONFIG, args or {})

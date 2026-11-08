"""Handler for Revenue Mix Reporter (revenue-mix-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "analyze",
  "items": [
    "sponsorship",
    "tickets",
    "memberships",
    "workshops",
    "other revenue"
  ],
  "slug": "revenue-mix-reporter",
  "name": "Revenue Mix Reporter"
}
def run(args):
    return run_engine(CONFIG, args or {})

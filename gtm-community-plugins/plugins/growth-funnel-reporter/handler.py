"""Handler for Growth Funnel Reporter (growth-funnel-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "analyze",
  "items": [
    "invites",
    "signups",
    "activated",
    "engaged",
    "retained"
  ],
  "slug": "growth-funnel-reporter",
  "name": "Growth Funnel Reporter"
}
def run(args):
    return run_engine(CONFIG, args or {})

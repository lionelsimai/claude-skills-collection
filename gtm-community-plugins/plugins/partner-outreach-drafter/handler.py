"""Handler for Partner Outreach Drafter (partner-outreach-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "shared audience",
    "entry offer",
    "proof supplied by user",
    "meeting ask"
  ],
  "slug": "partner-outreach-drafter",
  "name": "Partner Outreach Drafter"
}
def run(args):
    return run_engine(CONFIG, args or {})

"""Handler for Sponsor Package Builder (sponsor-package-builder). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "audience supplied by user",
    "deliverables",
    "term",
    "investment",
    "reporting"
  ],
  "slug": "sponsor-package-builder",
  "name": "Sponsor Package Builder"
}
def run(args):
    return run_engine(CONFIG, args or {})

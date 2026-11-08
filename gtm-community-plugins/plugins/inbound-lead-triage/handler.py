"""Handler for Inbound Lead Triage (inbound-lead-triage). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "classify",
  "items": [
    "demo request",
    "content download",
    "pricing question",
    "general enquiry",
    "support request",
    "spam"
  ],
  "slug": "inbound-lead-triage",
  "name": "Inbound Lead Triage"
}
def run(args):
    return run_engine(CONFIG, args or {})

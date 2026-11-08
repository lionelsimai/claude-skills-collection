"""Handler for Pricing Page Audit (pricing-page-audit). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "audit",
  "items": [
    "tiers named",
    "price anchor",
    "deliverables per tier",
    "faq",
    "terms",
    "call to action"
  ],
  "slug": "pricing-page-audit",
  "name": "Pricing Page Audit"
}
def run(args):
    return run_engine(CONFIG, args or {})

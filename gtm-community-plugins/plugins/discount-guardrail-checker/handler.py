"""Handler for Discount Guardrail Checker (discount-guardrail-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "score",
  "items": [
    "margin protected",
    "scope reduced",
    "payment terms",
    "expiry date",
    "approval level"
  ],
  "slug": "discount-guardrail-checker",
  "name": "Discount Guardrail Checker"
}
def run(args):
    return run_engine(CONFIG, args or {})

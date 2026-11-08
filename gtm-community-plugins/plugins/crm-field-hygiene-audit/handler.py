"""Handler for CRM Field Hygiene Audit (crm-field-hygiene-audit). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "audit",
  "items": [
    "company",
    "contact",
    "stage",
    "amount",
    "close date",
    "next step",
    "source"
  ],
  "slug": "crm-field-hygiene-audit",
  "name": "CRM Field Hygiene Audit"
}
def run(args):
    return run_engine(CONFIG, args or {})

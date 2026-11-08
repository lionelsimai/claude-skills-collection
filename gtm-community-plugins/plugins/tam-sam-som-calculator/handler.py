"""Handler for TAM SAM SOM Calculator (tam-sam-som-calculator). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "analyze",
  "items": [
    "total accounts",
    "serviceable accounts",
    "obtainable accounts",
    "average contract value",
    "win rate"
  ],
  "slug": "tam-sam-som-calculator",
  "name": "TAM SAM SOM Calculator"
}
def run(args):
    return run_engine(CONFIG, args or {})

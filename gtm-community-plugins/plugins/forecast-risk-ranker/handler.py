"""Handler for Forecast Risk Ranker (forecast-risk-ranker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "prioritize",
  "items": [
    "deal size",
    "stage confidence",
    "days to close",
    "slippage count",
    "effort to save"
  ],
  "slug": "forecast-risk-ranker",
  "name": "Forecast Risk Ranker"
}
def run(args):
    return run_engine(CONFIG, args or {})

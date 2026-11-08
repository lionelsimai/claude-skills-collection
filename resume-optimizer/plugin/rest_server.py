#!/usr/bin/env python3
"""Lionel Resume Optimizer — REST plugin server (Python 3, stdlib only).

Same four tools as the MCP server, over HTTP/JSON, for agents and apps
that call plugins via an OpenAPI spec (GPT Actions, LangChain, custom
agents, curl).

Endpoints:
  GET  /health                         -> {"status": "ok", ...}
  GET  /openapi.json                   -> OpenAPI 3.1 spec for this API
  GET  /.well-known/ai-plugin.json     -> plugin manifest
  POST /score          {resume_text, job_text, top?}
  POST /keywords       {job_text, top?}
  POST /gap-analysis   {resume_text, job_text, top?}
  POST /check-format   {resume_text}

Run:  python3 rest_server.py [--port 8787] [--host 127.0.0.1]
Local by default. Put it behind your own auth/TLS before exposing it
publicly — resumes are personal data.
"""

import argparse
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

_HERE = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.insert(0, _HERE)
from mcp_server import call_tool  # reuse one implementation

ROUTES = {
    "/score": "score_resume",
    "/keywords": "extract_keywords",
    "/gap-analysis": "gap_analysis",
    "/check-format": "check_format",
}


def _load(name):
    with open(os.path.join(_HERE, name), encoding="utf-8") as fh:
        return fh.read()


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):  # quiet
        pass

    def _send(self, code, body, ctype="application/json"):
        data = body if isinstance(body, bytes) else body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/health":
            self._send(200, json.dumps({"status": "ok", "name": "lionel-resume-optimizer", "version": "2.0.0"}))
        elif self.path == "/openapi.json":
            self._send(200, _load("openapi.json"))
        elif self.path == "/.well-known/ai-plugin.json":
            self._send(200, _load("ai-plugin.json"))
        else:
            self._send(404, json.dumps({"error": "not found"}))

    def do_POST(self):
        tool = ROUTES.get(self.path)
        if not tool:
            self._send(404, json.dumps({"error": "not found"}))
            return
        try:
            length = int(self.headers.get("Content-Length") or 0)
            args = json.loads(self.rfile.read(length) or b"{}")
            result = call_tool(tool, args)
            self._send(200, json.dumps(result, indent=2))
        except KeyError as exc:
            self._send(400, json.dumps({"error": f"missing field: {exc}"}))
        except Exception as exc:
            self._send(400, json.dumps({"error": str(exc)}))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8787)
    ap.add_argument("--host", default="127.0.0.1")
    args = ap.parse_args()
    HTTPServer((args.host, args.port), Handler).serve_forever()


if __name__ == "__main__":
    main()

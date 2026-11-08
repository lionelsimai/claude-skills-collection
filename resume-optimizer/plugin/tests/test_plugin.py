#!/usr/bin/env python3
"""Smoke tests for the Resume Optimizer plugin (MCP tools + REST routes).
Stdlib only. Run: python3 plugin/tests/test_plugin.py
"""
import json
import os
import subprocess
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.dirname(HERE)
REPO = os.path.dirname(PLUGIN)
sys.path.insert(0, PLUGIN)

from mcp_server import call_tool  # noqa: E402

resume = open(os.path.join(REPO, "examples/sample-resume.txt")).read()
job = open(os.path.join(REPO, "examples/sample-job.txt")).read()

fails = []

def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (f" — {detail}" if detail and not cond else ""))
    if not cond:
        fails.append(name)

# --- direct tool calls (what the MCP server runs) ---
s = call_tool("score_resume", {"resume_text": resume, "job_text": job})
check("score_resume overall in range", 0 <= s["overall_score"] <= 100, str(s))
check("score_resume has keywords", s["keywords_checked"] > 0)

k = call_tool("extract_keywords", {"job_text": job, "top": 10})
check("extract_keywords returns list", len(k["keywords"]) > 0)

g = call_tool("gap_analysis", {"resume_text": resume, "job_text": job})
check("gap_analysis partitions keywords",
      len(g["matched_keywords"]) + len(g["missing_keywords"]) == s["keywords_checked"])
check("gap_analysis carries honesty rule", "Never fabricate" in g["honesty_rule"])

f = call_tool("check_format", {"resume_text": resume})
check("check_format reports sections", "experience" in f["sections"])
check("check_format word count", f["word_count"] > 0)

# --- MCP stdio handshake ---
proc = subprocess.Popen([sys.executable, os.path.join(PLUGIN, "mcp_server.py")],
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
def rpc(proc, obj):
    proc.stdin.write(json.dumps(obj) + "\n"); proc.stdin.flush()
    return json.loads(proc.stdout.readline())

r = rpc(proc, {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
check("mcp initialize", r["result"]["serverInfo"]["name"] == "lionel-resume-optimizer")
r = rpc(proc, {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
names = [t["name"] for t in r["result"]["tools"]]
check("mcp tools/list = 4 tools", names == ["score_resume", "extract_keywords", "gap_analysis", "check_format"], str(names))
r = rpc(proc, {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
               "params": {"name": "score_resume", "arguments": {"resume_text": resume, "job_text": job}}})
sc = json.loads(r["result"]["content"][0]["text"])
check("mcp tools/call score matches direct", sc["overall_score"] == s["overall_score"])
proc.stdin.close(); proc.wait(timeout=5)

# --- REST server ---
srv = subprocess.Popen([sys.executable, os.path.join(PLUGIN, "rest_server.py"), "--port", "8799"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    for _ in range(50):
        try:
            with urllib.request.urlopen("http://127.0.0.1:8799/health", timeout=1) as resp:
                if json.loads(resp.read())["status"] == "ok":
                    break
        except Exception:
            time.sleep(0.1)
    req = urllib.request.Request("http://127.0.0.1:8799/score",
                                 data=json.dumps({"resume_text": resume, "job_text": job}).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=5) as resp:
        body = json.loads(resp.read())
    check("rest /score matches direct", body["overall_score"] == s["overall_score"])
    with urllib.request.urlopen("http://127.0.0.1:8799/openapi.json", timeout=5) as resp:
        spec = json.loads(resp.read())
    check("rest /openapi.json has 4 paths", len(spec["paths"]) == 4)
finally:
    srv.terminate(); srv.wait(timeout=5)

print("\n" + ("ALL PASS" if not fails else f"FAILURES: {fails}"))
sys.exit(1 if fails else 0)

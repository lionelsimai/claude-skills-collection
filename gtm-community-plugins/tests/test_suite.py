#!/usr/bin/env python3
"""Full suite: catalogue, folders, registry callability, MCP, REST. Stdlib only.
Run: python3 tests/test_suite.py"""
import json, os, subprocess, sys, time, urllib.request
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,ROOT)
fails=[]; passed=0
def check(name, cond, detail=""):
    global passed
    print(("PASS " if cond else "FAIL ")+name+(f" — {detail}" if detail and not cond else ""))
    if cond: passed+=1
    else: fails.append(name)

catalog=json.load(open(os.path.join(ROOT,"catalog.json")))
plugins=catalog["plugins"]
check("catalogue count >= 120 (target 120)", len(plugins)==120, str(len(plugins)))
check("catalogue count field matches", catalog["count"]==len(plugins))
slugs=[p["slug"] for p in plugins]; check("slugs unique", len(set(slugs))==len(slugs))
check("GTM = 60", sum(1 for p in plugins if p["domain"]=="GTM")==60)
check("Community = 60", sum(1 for p in plugins if p["domain"]=="Community")==60)
cats={p["category"] for p in plugins}; check("20 categories", len(cats)==20, str(cats))

for p in plugins:
    d=os.path.join(ROOT,"plugins",p["slug"])
    ok=True
    try:
        meta=json.load(open(os.path.join(d,"plugin.json")))
        assert meta["version"]=="1.0.0" and meta["license"]=="MIT" and meta["author"]["name"]=="Lionel Sim"
        assert meta["guardrails"]["no_auto_send"] and meta["guardrails"]["no_fabrication"]
        assert meta["tools"] and meta["tools"][0]["sample_input"] is not None
        rd=open(os.path.join(d,"README.md")).read(); assert "Guardrails" in rd and "Example call" in rd
        assert os.path.isfile(os.path.join(d,"handler.py"))
    except Exception as e: ok=False; check(f"folder {p['slug']}", False, str(e))
    if not ok: break
else: check("all 120 folders: valid plugin.json + README(guardrails/example) + handler.py", True)

from core.registry import get_registry
reg=get_registry()
check("registry tools = 120", len(reg.tools)==120, str(len(reg.tools)))
bad=[]
for p in plugins:
    t=p["tool"]; meta=reg.tools[t]["meta"]
    try:
        r=reg.call(t, meta["sample_input"])
        assert r["plugin"]==p["slug"] and r["tool"]==t and "result" in r and "guardrails" in r
        assert r["guardrails"]["human_approval_required"]
        # kind-specific shape
        k=p["kind"]; res=r["result"]
        if k=="score": assert "score" in res and "breakdown" in res
        elif k=="classify": assert "label" in res
        elif k=="checklist" or k=="audit": assert "completion_pct" in res or "present" in res
        elif k=="template": assert "draft" in res and "DRAFT" in res["status"]
        elif k=="analyze": assert isinstance(res, dict)
        elif k=="prioritize": assert "ranked" in res
        elif k=="plan": assert "steps" in res
    except Exception as e: bad.append((t,str(e)))
check("every tool callable with sample input + documented shape + guardrails", not bad, str(bad[:3]))

# MCP handshake
proc=subprocess.Popen([sys.executable, os.path.join(ROOT,"mcp_server.py")], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
def rpc(o):
    proc.stdin.write(json.dumps(o)+"\n"); proc.stdin.flush(); return json.loads(proc.stdout.readline())
r=rpc({"jsonrpc":"2.0","id":1,"method":"initialize","params":{}})
check("MCP initialize", r["result"]["serverInfo"]["name"]=="lionel-gtm-community-plugins")
r=rpc({"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}})
check("MCP tools/list = 120", len(r["result"]["tools"])==120, str(len(r["result"]["tools"])))
first=plugins[0]; r=rpc({"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":first["tool"],"arguments":reg.tools[first["tool"]]["meta"]["sample_input"]}})
check("MCP tools/call works", json.loads(r["result"]["content"][0]["text"])["plugin"]==first["slug"])
proc.stdin.close(); proc.wait(timeout=5)

# REST smoke
srv=subprocess.Popen([sys.executable, os.path.join(ROOT,"rest_server.py"),"--port","8798"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    ok=False
    for _ in range(50):
        try:
            with urllib.request.urlopen("http://127.0.0.1:8798/health",timeout=1) as resp: ok=json.loads(resp.read())["tools"]==120
            if ok: break
        except Exception: time.sleep(0.1)
    check("REST /health tools=120", ok)
    t="nps_calculator"; req=urllib.request.Request(f"http://127.0.0.1:8798/tools/{t}", data=json.dumps(reg.tools[t]["meta"]["sample_input"]).encode(), headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=5) as resp: body=json.loads(resp.read())
    check("REST /tools/nps_calculator callable", body["plugin"]=="nps-calculator")
finally: srv.terminate(); srv.wait(timeout=5)

print(f"\n{passed} checks passed, {len(fails)} failed")
if fails: print("FAILURES:",fails)
sys.exit(1 if fails else 0)

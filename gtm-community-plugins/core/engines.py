#!/usr/bin/env python3
"""Deterministic engines for all plugins. Stdlib only.

Each plugin supplies a distinct config (kind + items). Engines never
invent facts: missing inputs are reported, generative kinds return
drafts built only from supplied facts with placeholders marked.
"""
import re
from statistics import mean

GUARDRAILS = {
    "no_fabrication": True,
    "use_supplied_facts_only": True,
    "human_approval_required": True,
    "no_auto_send": True,
    "draft_only": True,
}

def _key(s):
    return re.sub(r"[^a-z0-9]+", "_", s.strip().lower()).strip("_")

def _grade(score):
    return "A" if score >= 85 else "B" if score >= 70 else "C" if score >= 50 else "D"

def _wrap(cfg, result):
    return {"plugin": cfg["slug"], "tool": cfg["slug"].replace("-", "_"),
            "kind": cfg["kind"], "result": result, "guardrails": dict(GUARDRAILS)}

def run_engine(cfg, args):
    kind, items = cfg["kind"], cfg["items"]
    keys = [_key(i) for i in items]
    if kind == "score":
        metrics = args.get("metrics") or {}
        breakdown, missing = {}, []
        for item, k in zip(items, keys):
            if k in metrics:
                v = max(0, min(100, float(metrics[k])))
                breakdown[item] = v
            else:
                missing.append(item)
        score = round(mean(breakdown.values()), 1) if breakdown else 0
        return _wrap(cfg, {"score": score, "grade": _grade(score),
                           "breakdown": breakdown, "missing_metrics": missing,
                           "note": "Equal-weighted mean of supplied criteria only."})
    if kind == "classify":
        text = (args.get("text") or "").lower()
        scores = {}
        for item in items:
            words = [w for w in re.findall(r"[a-z]+", item.lower()) if len(w) > 2]
            scores[item] = sum(1 for w in words if w in text)
        best = max(items, key=lambda i: scores[i]) if items else None
        total = sum(scores.values())
        if total == 0:
            best, conf = items[-1] if items else None, 0.0
        else:
            conf = round(scores[best] / total, 2)
        return _wrap(cfg, {"label": best, "confidence": conf, "scores": scores,
                           "route": f"Route to human owner for '{best}' — classification is a triage aid, not a final decision."})
    if kind in ("checklist", "audit"):
        if kind == "checklist":
            done = { _key(x) for x in (args.get("completed") or []) }
            present = [i for i, k in zip(items, keys) if k in done or i.lower() in {str(x).lower() for x in (args.get("completed") or [])}]
            missing = [i for i in items if i not in present]
        else:
            text = (args.get("text") or "").lower()
            present = [i for i in items if i.lower() in text]
            missing = [i for i in items if i not in present]
        pct = round(100 * len(present) / len(items)) if items else 0
        return _wrap(cfg, {"present": present, "missing": missing,
                           "completion_pct": pct, "ready": pct == 100})
    if kind == "template":
        facts = args.get("facts") or {}
        lines, used, placeholders = [], {}, []
        for item, k in zip(items, keys):
            if k in facts:
                lines.append(f"{item}: {facts[k]}"); used[item] = facts[k]
            else:
                lines.append(f"{item}: [missing: supply {item}]"); placeholders.append(item)
        return _wrap(cfg, {"draft": "\n".join(lines), "sections": items,
                           "facts_used": used, "placeholders": placeholders,
                           "status": "DRAFT — human approval required before any use or send"})
    if kind == "analyze":
        counts = args.get("counts") or {}
        amounts = args.get("amounts") or {}
        series = args.get("series") or []
        out = {}
        if counts:
            vals = {i: counts.get(_key(i)) for i in items if _key(i) in counts}
            out["counts"] = vals
            vs = [float(v) for v in vals.values() if isinstance(v, (int, float))]
            if len(vs) >= 2 and vs[0]:
                out["first_to_last_change_pct"] = round(100 * (vs[-1] - vs[0]) / vs[0], 1)
            low = " ".join(items).lower()
            if "promoter" in items[0].lower() and len(items) >= 4:
                p = float(counts.get(_key(items[0]), 0)); d = float(counts.get(_key(items[2]), 0))
                t = float(counts.get(_key(items[3]), 0))
                if t: out["nps"] = round(100 * (p - d) / t); out.pop("first_to_last_change_pct", None)
            if "ticket price" in low:
                costs = [float(counts.get(_key(i), 0)) for i in items[:3]]
                price = float(counts.get(_key(items[3]), 0)) if len(items) > 3 else 0
                if price: out["break_even_units"] = int(-(-sum(costs) // price))
            if "duplicate" in low and vs:
                pass
        if amounts:
            tot = sum(float(v) for v in amounts.values() if isinstance(v, (int, float)))
            out["amount_shares_pct"] = {k: round(100 * float(v) / tot, 1) for k, v in amounts.items() if tot}
            out["total_amount"] = tot
        if series:
            out["series"] = {"n": len(series), "min": min(series), "max": max(series),
                             "mean": round(mean(series), 2),
                             "trend": "up" if series[-1] > series[0] else "down" if series[-1] < series[0] else "flat"}
        out["metrics_context"] = items
        return _wrap(cfg, out)
    if kind == "prioritize":
        rows = []
        for it in (args.get("items") or []):
            impact, effort = float(it.get("impact", 0)), float(it.get("effort", 1)) or 1
            rows.append({"name": it.get("name", "[unnamed]"), "impact": impact,
                         "effort": effort, "ratio": round(impact / effort, 2)})
        rows.sort(key=lambda r: r["ratio"], reverse=True)
        return _wrap(cfg, {"ranked": rows, "criteria": items,
                           "note": "Ranked by supplied impact / effort only."})
    if kind == "plan":
        goal = args.get("goal") or "[missing: supply a goal]"
        days = int(args.get("timeframe_days") or 30)
        steps = [{"step": i + 1, "action": s, "by_day": max(1, round(days * (i + 1) / len(items)))}
                 for i, s in enumerate(items)]
        return _wrap(cfg, {"goal": goal, "timeframe_days": days, "steps": steps,
                           "status": "PLAN — owner must confirm before execution"})
    raise ValueError(f"Unknown kind: {kind}")

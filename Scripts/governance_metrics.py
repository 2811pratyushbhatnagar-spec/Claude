#!/usr/bin/env python3
"""governance_metrics.py -- escalation provenance + governance-machinery diagnostics.

GUARD (critical, conservative-static-analysis property): these metrics only FLAG an escalation
rule for HUMAN review of its breadth. Automation may NEVER auto-tighten or auto-relax an
escalation rule -- that would be the machine making itself more permissive. De-escalation rate
is a RULE diagnostic, never a reviewer target. This output is governance instrumentation and
lives in .automation/ -- it never appears in the research views (SNAPSHOT/DECISIONS), and it
must never contain scientific evidence-band vocabulary (two-object separation, enforced below).

Usage:
  python governance_metrics.py log --item Q-X --from C --to B --rule <rule-name>   # provenance
  python governance_metrics.py report                                             # diagnostics
"""
import argparse, json, os, datetime, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ESC = os.path.join(ROOT, ".automation", "escalations.jsonl")
BAND_TERMS = ("builder-supported", "independently-reproduced", "finite-verified",
              "general-conjecture", "promoted", "builder-only", "cross-confirmed",
              "externally-audited")

def now(): return datetime.datetime.now().astimezone().isoformat(timespec="seconds")

def log_escalation(item, frm, to, rule):
    os.makedirs(os.path.dirname(ESC), exist_ok=True)
    with open(ESC, "a", encoding="utf-8") as f:
        f.write(json.dumps({"item": item, "from": frm, "to": to, "rule": rule,
                            "at": now(), "by": "automation"}) + "\n")

def report():
    escs = []
    if os.path.exists(ESC):
        escs = [json.loads(l) for l in open(ESC, encoding="utf-8") if l.strip()]
    deesc_items = set()
    dp = os.path.join(ROOT, "DECLASSIFICATIONS.md")
    if os.path.exists(dp):
        for m in re.finditer(r"^- (\S+?):", open(dp, encoding="utf-8").read(), re.M):
            deesc_items.add(m.group(1))
    by_rule = {}
    for e in escs:
        r = by_rule.setdefault(e["rule"], {"n": 0, "deescalated": 0})
        r["n"] += 1
        if e["item"] in deesc_items: r["deescalated"] += 1
    total, dee = len(escs), sum(r["deescalated"] for r in by_rule.values())
    lines = [
        "# Governance-machinery diagnostics -- FLAGS FOR HUMAN RULE-BREADTH REVIEW ONLY",
        "*(automation may NEVER auto-tighten/relax an escalation rule; de-escalation rate is a",
        "rule diagnostic, never a reviewer target; generated " + now() + ")*", "",
        f"- auto-escalations logged: {total}",
        f"- human de-escalation rate: {dee}/{total}" + (f" = {dee/total:.2f}" if total else " (n/a)"),
        "- precision BY RULE (fraction later human-de-escalated -> localizes a too-broad rule):",
    ]
    for rule, r in sorted(by_rule.items()):
        flag = "  <- FLAG: review this rule's breadth (human)" if r["n"] and r["deescalated"]/r["n"] > 0.5 else ""
        lines.append(f"  - {rule}: {r['deescalated']} of {r['n']} de-escalated{flag}")
    if not by_rule:
        lines.append("  - (no auto-escalations on record yet; provenance logging is live)")
    # reasoning-efficiency (resource rules): usable-now metrics only; long-run metric stays undefined
    rl = os.path.join(ROOT, ".automation", "run_ledger.jsonl")
    if os.path.exists(rl):
        runs = [json.loads(l) for l in open(rl, encoding="utf-8") if l.strip()]
        noop = sum(1 for r in runs if r.get("gate") == "no-op")
        tok_runs = [r for r in runs if r.get("model_tokens")]
        changed = sum(r.get("files_changed", 0) for r in tok_runs)
        lines += ["", "## Reasoning-efficiency (resource rules; diagnostic only)",
                  f"- runs: {len(runs)} | no-op gate (zero-reasoning) rate: {noop}/{len(runs)}",
                  f"- tokens per changed artifact: " +
                  (f"{sum(r['model_tokens'] for r in tok_runs)/changed:.0f}" if changed else
                   "n/a (wrapper has not appended token counts yet)"),
                  "- tokens per accepted packet: n/a (no packets through review yet)",
                  "- tokens per promoted theorem: UNDEFINED until promotions exist (long-run only; never gated on early)"]
    out = "\n".join(lines) + "\n"
    # two-object separation: governance instrumentation must not carry scientific bands
    assert not any(t in out for t in BAND_TERMS), "band vocabulary leaked into governance metrics"
    p = os.path.join(ROOT, ".automation", "governance_metrics.md")
    open(p, "w", encoding="utf-8").write(out)
    print(out)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    lg = sub.add_parser("log")
    lg.add_argument("--item", required=True); lg.add_argument("--from", dest="frm", required=True)
    lg.add_argument("--to", required=True); lg.add_argument("--rule", required=True)
    sub.add_parser("report")
    a = ap.parse_args()
    if a.cmd == "log":
        log_escalation(a.item, a.frm, a.to, a.rule); print("escalation provenance logged")
    else:
        report()

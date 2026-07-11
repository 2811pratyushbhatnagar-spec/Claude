# Project heartbeat generator — GENERATED VIEWS ONLY, never canonical, regenerable anytime.
# Sources: status.json, questions.json, counts.json, LedgerE/evidence_log.md, git, run_checks.py.
# Emits: SNAPSHOT.md + snapshot.json (heartbeat) and DECISIONS.md (automation vs Tier-3 queues).
#   python snapshot.py            -> regenerate all three
import json, os, re, subprocess, sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
def load(p): return json.load(open(os.path.join(HERE, p), encoding="utf-8"))
def readf(p): return open(os.path.join(HERE, p), encoding="utf-8").read()
def git(*args):
    return subprocess.run(["git"] + list(args), capture_output=True, text=True, cwd=HERE).stdout.strip()

status, qreg, cj = load("status.json"), load("questions.json"), load("counts.json")
Q = qreg["questions"]
L = status["ledgers"]
status["areas"] = {   # derived display strings (unified schema, 2026-07-05)
    "Mathematics":    {"status": f"Ledger A frozen v{L['A']['version']} canonical"},
    "Protocol":       {"status": f"Ledger B frozen v{L['B']['version']}; testing, not extension"},
    "Correspondence": {"status": f"empty by design; admitted={L['C'].get('admitted', 0)}; "
                                 f"candidate queue: {len(L['C'].get('candidate_queue', []))} (unadmitted)"},
    "Ontology":       {"status": L['D']['state']},
    "EvidenceLog":    {"status": L['E']['state']},
    "Journal":        {"status": status["journal"]["state"]},
    "Publication":    {"status": status["publication"]["state"]},
}

head = git("log", "-1", "--format=%h %ad", "--date=format:%Y-%m-%d %H:%M")
recent = git("log", "--oneline", "-5").splitlines()
GENERATED = ("SNAPSHOT.md", "snapshot.json", "DECISIONS.md")
dirty = "\n".join(l for l in git("status", "--porcelain").splitlines()
                  if not l.strip().endswith(GENERATED))

print("running run_checks.py (full recompute; this is what makes the heartbeat honest)...")
chk = subprocess.run([sys.executable, os.path.join(HERE, "run_checks.py")],
                     capture_output=True, text=True, cwd=HERE)
checks_pass = chk.returncode == 0
checks_line = "ALL TIER-1 CHECKS PASS" if checks_pass else "TIER-1 CHECKS FAILED — see run_checks.py"

# Ledger E: table rows + validator metrics cell
ev = readf("LedgerE/evidence_log.md")
rows = [r for r in ev.splitlines() if r.startswith("|") and "---" not in r][1:]
last_rows = []
for r in rows[-5:]:
    c = [x.strip() for x in r.strip().strip("|").split("|")]
    if len(c) == 6: last_rows.append((c[0], c[1], c[4]))
vmetrics = next((r for r in rows if "Validator metrics" in r), "")
vm_cell = [x.strip() for x in vmetrics.strip().strip("|").split("|")][3] if vmetrics else "n/a"

live = [q for q in Q if q["state"] in ("open", "investigating", "conjecture")]
conj = [q for q in Q if q["state"] == "conjecture"]
blockers = [q for q in live if q["owner"] == "human"]
destroy = [(q["id"], q["state"], q["invalidated_if"]) for q in live if q["invalidated_if"]]
by_ver = {}
for k, v in cj["counts"].items():
    by_ver.setdefault(v["verification"], []).append(
        f"{k}: {v['fraction_nondeterministic']['numerator']} of {v['fraction_nondeterministic']['denominator']} nondeterministic")

math_ready = not conj and not [q for q in live if q["state"] != "conjecture"]
snap = {
    "generated_at_head": head,
    "canonical": {a: d["status"] for a, d in status["areas"].items()},
    "checks": checks_line, "working_tree_clean": not dirty,
    "readiness": {"Mathematics": "ready" if math_ready else
                  f"not ready: {len(conj)} conjecture(s), {len(live)-len(conj)} open",
                  "Publication": f"not ready: {len(blockers)} item(s) awaiting human action"},
    "open_blockers": [{"id": q["id"], "next_action": q["next_action"]} for q in blockers],
    "verified_computations": {k: f"{v['fraction_nondeterministic']['numerator']} of "
                              f"{v['fraction_nondeterministic']['denominator']} nondeterministic ({v['verification']})"
                              for k, v in cj["counts"].items()},
    "reproduction_bands": {k: v for k, v in by_ver.items()},
    "destroy_attempts_outstanding": [{"id": i, "state": s, "attempts": a} for i, s, a in destroy],
    "ledgerE_recent": [{"date": d, "artifact": a, "disposition": p} for d, a, p in last_rows],
    "validator_catches": vm_cell,
}
with open(os.path.join(HERE, "snapshot.json"), "w", encoding="utf-8") as f:
    json.dump(snap, f, indent=2)

md = []
md.append(f"# PROJECT SNAPSHOT — generated view, non-canonical · Class-D artifact (regenerate: `python snapshot.py`)")
md.append(f"\n*Generated at head `{head}`. The one file to read first; everything below is derived from "
          f"status.json / questions.json / counts.json / Ledger E / git / a fresh run_checks execution.*\n")
md.append("## Canonical state")
for a, d in status["areas"].items(): md.append(f"- **{a}**: {d['status']}")
md.append(f"- **head**: `{head}` · working tree {'clean' if not dirty else 'DIRTY'}")
md.append("\n## Repo health")
md.append(f"- checks (fresh run): **{checks_line}**")
md.append(f"- validator catches to date: {vm_cell}")
md.append("\n## Readiness (condensed; full: `python readiness.py`)")
for k, v in snap["readiness"].items(): md.append(f"- **{k}**: {v}")
md.append("\n## Open blockers (human-owned, live)")
for q in blockers: md.append(f"- **{q['id']}** [{q['state']}] — {q['next_action']}")
md.append("\n## Last verified computations (counts.json, regression-guarded)")
for k, v in snap["verified_computations"].items(): md.append(f"- {k}: {v}")
md.append("\n## Independent-reproduction banding")
for lvl in ("externally-audited", "cross-confirmed", "builder-only"):
    items = by_ver.get(lvl, [])
    md.append(f"- **{lvl}** ({len(items)}): " + ("; ".join(i.split(':')[0] for i in items) if items else "none"))
md.append("\n## Outstanding destroy-attempts (what an adversary should try, per live claim)")
for i, s, a in destroy:
    md.append(f"- **{i}** [{s}]:")
    for x in a: md.append(f"  - {x}")
md.append("\n## Ledger E — recent rows")
for d, a, p in last_rows: md.append(f"- {d} · {a} · **{p}**")
md.append("\n## Recent commits")
for c in recent: md.append(f"- `{c}`")
with open(os.path.join(HERE, "SNAPSHOT.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(md) + "\n")

# ---- DECISIONS.md: decision classes A-D by irreversibility (see DECISION-CLASSES.md) ----
def dclass(q):
    c = q.get("decision_class")
    if not c:  # ambiguity classifies UP -- and the auto-escalation logs its provenance (rule name)
        c = "A" if q["owner"] == "human" else "C"
        try:
            import datetime as _d
            with open(os.path.join(HERE, ".automation", "escalations.jsonl"), "a", encoding="utf-8") as f:
                f.write(json.dumps({"item": q["id"], "from": None, "to": c,
                                    "rule": "default-missing-class-up",
                                    "at": _d.datetime.now().astimezone().isoformat(timespec="seconds"),
                                    "by": "automation"}) + "\n")
        except Exception:
            pass
    return c
def indep(q):
    e = q["evidence"].lower()
    return "yes" if any(k in e for k in ("blinded", "audit", "cross-confirmed", "agrees with the r-series")) else "not yet"
def packet(q):
    p = [f"- **{q['id']}** [{q['state']}] · Class {dclass(q)}",
         f"  - what/why: {q['statement']}",
         f"  - evidence (provenance): {q['evidence'][:240]}",
         f"  - validators at generation: {checks_line}",
         f"  - dependencies: {', '.join(q['depends_on']) if q['depends_on'] else 'none'}",
         f"  - independent reproduction: {indep(q)}",
         f"  - recommended action: {q['next_action']}"]
    if dclass(q) == "A":
        cl = q.get("checklist")
        p.append("  - substantial-result checklist (DRAFT, unfrozen): " +
                 ("; ".join(f"{k[2:]}: {v.split(' (')[0].split(' - ')[0]}" for k, v in cl.items())
                  if cl else "not yet drafted for this item"))
    return p
live = [q for q in Q if q["state"] in ("open", "investigating", "conjecture")]
qA = [q for q in live if dclass(q) == "A"]
qB = [q for q in live if dclass(q) == "B"]
qC = [q for q in live if dclass(q) == "C"]
dm = ["# DECISION QUEUE — generated view · itself a Class-D artifact (a view OF the queues)",
      "\n*Decision classes by IRREVERSIBILITY (`DECISION-CLASSES.md`). Tie-break: ambiguous items",
      "classify UP. Every item carries an evidence packet so context never needs reconstructing.*\n",
      "## CLASS A — irreversible scientific claims (individual review, NEVER batched)",
      "*Anchored to `status.json → governance.tier3_human_only`; automation may not declassify an A-item.*"]
for q in qA: dm += packet(q)
dm += ["\n### Standing Class-A / Tier-3 acts (never automated)",
       "- promote conjecture → theorem (ratify a band upgrade)",
       "- freeze / unfreeze a ledger; modify Ledger B (needs observed friction)",
       "- admit a Ledger C correspondence entry",
       "- publish anything; send held letters; freeze the substantial-result checklist",
       "- merge a reconciliation; accept external material as canonical"]
dm.append("\n## CLASS B — interpretive / governance changes (small batched review, with rationale)")
for q in qB: dm += packet(q)
cbq = os.path.join(HERE, ".automation", "class_b_queue.md")
if os.path.exists(cbq):
    rows = [l for l in open(cbq, encoding="utf-8").read().splitlines() if l.startswith("- ")]
    dm.append(f"*Batch queue ({len(rows)} item(s), `.automation/class_b_queue.md`):*")
    dm += rows
dm += ["\n## CLASS C — evidence records (bulk review; spot-check samples)"]
for q in qC: dm.append(f"- **{q['id']}** [owner: {q['owner']}] — {q['next_action']}")
dm += ["- Ledger E appended rows · brute-force bank (`.automation/bf_findings.md`) · recomputations",
       "- STANDING — run `python run_checks.py` (validate + consistency + regression)"]
dm += ["\n## CLASS D — purely generated artifacts (no approval if validators pass; regenerate on demand)",
       "- SNAPSHOT.md · snapshot.json · DECISIONS.md · readiness/agenda output · counts renderings · null-certificate horizon",
       "- STANDING — regenerate views (`python snapshot.py`; `python readiness.py`; `python agenda.py`)",
       "- **Labeling rule:** every artifact carries its class at display; a Class-D count is never presentable as a Class-A result."]
bf_path = os.path.join(HERE, ".automation", "bf_state.json")
if os.path.exists(bf_path):
    bf = json.load(open(bf_path, encoding="utf-8"))
    dm.append("\n## BRUTE-FORCE QUEUE (cycle-integrated chunk step; resumable; negatives bank as findings)")
    for q in bf["queue"]:
        line = f"- **{q['id']}** [{q['status']}] — {q['title']}"
        if q["id"] == "BF-1" and q.get("space"):
            line += f" · progress {q['next_F']}/{q['space']} ({100.0*q['next_F']/q['space']:.1f}%)"
        dm.append(line)
    dm.append("- bank: `.automation/bf_findings.md` · null certificate: `.automation/bf_null_certificate.md`")
dcand = os.path.join(HERE, ".automation", "deferred_candidates.md")
if os.path.exists(dcand):
    cands = [l for l in open(dcand, encoding="utf-8").read().splitlines() if l.startswith("- CANDIDATE")]
    if cands:
        dm.append("\n## DEFERRED DESIGN CANDIDATES (logged, NOT built — await a pre-registered execution signal)")
        dm += cands
        dm.append("- full records + reopen signals: `.automation/deferred_candidates.md`")
dm += ["\n## FINITE HORIZON (Pratyush's directive, 2026-07-05)",
       "The automation is finite-horizon: it runs until a novel substantial result — a FORCED bridge",
       "OR an exhaustively-demonstrated NULL — is ratified and published. Post-publication, the",
       "stateless-worker + repo-as-only-memory design makes every result independently reproducible",
       "(pull the repo, re-run every check). This is the exit condition; it is not meant to run forever.",
       "The physics bar stays forced-only: the cycle exhausts the search and never declares contact;",
       "a forced bridge, if one surfaces, goes to Tier-3 ratification — never auto-promoted."]
# TWO-OBJECT SEPARATION (enforced, not conventional): packet-quality metrics and scientific
# evidence-bands are different objects and must NEVER appear in the same research view.
METRIC_TOKENS = ("confidence_after", "additional_context_requested", "review_metrics")
for name, text in (("SNAPSHOT.md", "\n".join(md)), ("DECISIONS.md", "\n".join(dm))):
    leaked = [t for t in METRIC_TOKENS if t in text]
    assert not leaked, f"review-metric object leaked into research view {name}: {leaked}"

with open(os.path.join(HERE, "DECISIONS.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(dm) + "\n")

# ---- EVIDENCE RIVER: Ledger E rendered as a chronological timeline (Class-D generated view) ----
river = ["# EVIDENCE RIVER — Ledger E as a timeline · Class-D generated view "
         "(regenerate: `python snapshot.py`; canonical record: `LedgerE/evidence_log.md`)",
         "\n*A semantic, chronological read of what already happened. Append-only source; this view*",
         "*adds nothing and certifies nothing.*\n"]
RESEARCH_KW = ("enumeration", "audit", "proof", "theorem", "counterexample", "null", "destroy",
               "carry-set", "structure-map", "n=4", "n=3", "reconciliation of the two parallel",
               "msf", "k(e)", "ladder", "witness", "conjecture")
n_research = n_infra = 0
# re-parse Ledger E locally ('rows' was shadowed by the Class-B queue rendering above)
_ev_rows = [r for r in readf("LedgerE/evidence_log.md").splitlines()
            if r.startswith("|") and "---" not in r][1:]
for r in _ev_rows:  # Date|Artifact|Action|Evidence|Disposition|Reason
    c = [x.strip() for x in r.strip().strip("|").split("|")]
    if len(c) == 6:
        kind = "research" if any(k in (c[1] + " " + c[2]).lower() for k in RESEARCH_KW) else "infra"
        if kind == "research":
            n_research += 1
            river.append(f"- **{c[0]}** · {c[1]} — *{c[2]}* → **{c[4]}**")
            river.append(f"  - {c[5][:220]}")
        else:
            n_infra += 1
            river.append(f"- <small>{c[0]} · {c[1]} — {c[2]} → {c[4]}</small> *(infra, backgrounded)*")
healthy = n_research >= n_infra
river.append(f"\n---\n**River health (diagnostic, not target):** {n_research} research / {n_infra} "
             f"infrastructure events — "
             + ("healthy: the river reads as research." if healthy else
                "**FLAG: machinery is the primary activity.** A healthy river reads as research "
                "(n=4 completed, counterexample not found, destroy attempt failed, null packaged). "
                "This flag is a valid observation-signal input for the governance sensor stream."))
with open(os.path.join(HERE, "EVIDENCE-RIVER.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(river) + "\n")

print(f"wrote SNAPSHOT.md, snapshot.json, DECISIONS.md, EVIDENCE-RIVER.md | checks: {checks_line} | head: {head}")

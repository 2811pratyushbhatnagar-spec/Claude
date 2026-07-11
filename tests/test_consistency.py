# Tier-1 CONSISTENCY: cross-references, versions, schema, no dangling refs.
# Scope: LedgerA/B/C/D/E, ARCHITECTURE, README, reconciliation, handoffs.
# (Experiments/ excluded: external research notes referencing files outside this repo.)
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAIL = []

def check(name, cond, detail=""):
    if cond: print(f"  ok   {name}")
    else:
        print(f"  FAIL {name}  {detail}")
        FAIL.append(name)

def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()

# --- inventory ---
repo_files = set()
for dirpath, _, files in os.walk(ROOT):
    if ".git" in dirpath: continue
    for f in files:
        repo_files.add(f)

# --- 1. no dangling file references (scoped dirs) ---
SCOPE = ["LedgerA", "LedgerB", "LedgerC", "LedgerD", "LedgerE", "reconciliation", "handoffs"]
SCOPE_FILES = ["README.md", "ARCHITECTURE.md"]
KNOWN_PENDING = {"ledger_a_verify.py", "kr.txt",
                 # external source-folder files named in handoffs (not repo content):
                 "reversible_contact_protocol_ledger_v0.4.md", "reversible_contact_v0.1.md",
                 # files inside the superseded chat-side scaffold zip, cited by Ledger E as record:
                 "validate.py",
                 # Implementation A's chat-side enumerator (deliberately UNREAD per the
                 # independence protocol; cited by the reproduction evidence as provenance):
                 "r1_ladder_n4.py"}
mds = list(SCOPE_FILES)
for d in SCOPE:
    for dirpath, _, files in os.walk(os.path.join(ROOT, d)):
        if os.path.basename(dirpath) in ("archive", "audits"):
            continue  # archives/audit reports are frozen records; they cite their historical context
        mds += [os.path.relpath(os.path.join(dirpath, f), ROOT) for f in files if f.endswith(".md")]
ref_pat = re.compile(r"[A-Za-z0-9_\-]+(?:\.[A-Za-z0-9_\-]+)*\.(?:py|md)\b")
for rel in mds:
    txt = read(rel)
    for ref in set(ref_pat.findall(txt)):
        base = os.path.basename(ref)
        if base in KNOWN_PENDING: continue
        check(f"ref exists: {base} (in {os.path.basename(rel)})", base in repo_files)

# --- 2. Ledger A canonical: required structure ---
can = read("LedgerA/ledger_A_canonical.md")
check("canonical is v0.7", "v0.7 · CANONICAL" in can)
check("changelog chain v0.7..v0.1", "v0.7 (2026-07-05" in can and
      all(f"v0.{i} (2026-07-04" in can for i in (6, 5, 4, 3, 2, 1)))
check("Theorem R1 defined exactly once", len(re.findall(r"^## Theorem R1", can, re.M)) == 1)
check("Proposition R2 defined exactly once", len(re.findall(r"^## Proposition R2", can, re.M)) == 1)
check("R2 assumptions explicit", "**Assumptions (explicit).**" in can)
check("R1 confidence band present", "Confidence band (updated" in can or "Confidence band (governance" in can)
check("R2 promotion HELD (firewall)", "promotion HELD" in can)
check("canonical points to frozen reconciliation", "reconciliation_2026-07-04.md" in can)
arch_v1 = read("LedgerA/archive/ledger_A_math_v0.1_frozen.md")
check("archived v0.1 carries SUPERSEDED banner", "SUPERSEDED" in arch_v1)

# --- 3. reconciliation snapshot frozen ---
rec = read("reconciliation/reconciliation_2026-07-04.md")
check("snapshot marked FROZEN SNAPSHOT", "FROZEN SNAPSHOT" in rec)
check("snapshot states never-edited rule", "never edited" in rec)

# --- 4. Ledger B/C/D governance markers ---
prot = read("LedgerB/protocol_ledger.md")
check("protocol is v0.5 frozen", "v0.5" in prot and "frozen" in prot.lower())
check("Ledger C marked EMPTY by design", "EMPTY" in read("LedgerC/README.md"))
check("Ledger D allowed empty", "allowed empty" in read("LedgerD/README.md"))

# --- 5. Ledger E fixed schema, append-only ---
ev = read("LedgerE/evidence_log.md")
check("Ledger E schema line present", "`Date | Artifact | Action | Evidence | Disposition | Reason`" in ev)
check("Ledger E declares append-only", "append-only" in ev)
rows = [l for l in ev.splitlines() if l.startswith("|") and "---" not in l]
hdr = rows[0] if rows else ""
check("Ledger E header row matches schema",
      [c.strip() for c in hdr.strip("|").split("|")] == ["Date", "Artifact", "Action", "Evidence", "Disposition", "Reason"])
bad = [i for i, r in enumerate(rows[1:], 2)
       if len([c for c in r.strip().strip("|").split("|")]) != 6]
check("every Ledger E row has exactly 6 fields", not bad, f"bad rows at table lines {bad}")

# --- 6. Question Registry + status: schema-valid, governance note present ---
import json
qreg = json.loads(read("questions.json"))
check("questions.json parses with _meta.governance", "governance" in qreg.get("_meta", {}))
SCHEMA = ["id", "statement", "state", "evidence", "band", "next_action", "owner"]
DEP_FIELDS = ["depends_on", "invalidated_if", "blocks"]
STATES = set(qreg["_meta"]["states"])
ids = [q.get("id") for q in qreg["questions"]]
check("question ids unique", len(ids) == len(set(ids)))
for q in qreg["questions"]:
    check(f"registry fields complete: {q.get('id','?')}", all(k in q and q[k] for k in SCHEMA))
    check(f"registry dep-fields present: {q.get('id','?')}",
          all(k in q and isinstance(q[k], list) for k in DEP_FIELDS))
    check(f"registry state valid: {q.get('id','?')}", q.get("state") in STATES, f"got {q.get('state')}")
    check(f"registry owner valid: {q.get('id','?')}", q.get("owner") in ("auto", "human"))
    for k in ("depends_on", "blocks"):
        for tok in q.get(k, []):
            if tok.startswith("Q-"):
                check(f"dep resolves: {q['id']}.{k} -> {tok}", tok in ids)
st = json.loads(read("status.json"))
check("status.json unified schema: ledgers A-E present",
      all(k in st.get("ledgers", {}) for k in "ABCDE"))
check("status.json has journal, publication, governance blocks",
      all(k in st for k in ("journal", "publication", "governance")))
check("status.json Ledger A version matches canonical header",
      f"v{st['ledgers']['A']['version']} · CANONICAL" in can)
check("dual-agreement rule recorded in governance",
      "dual_agreement_rule" in st["governance"])
check("decision classes: policy doc anchored to Tier-3",
      "anchored to the Tier-3 firewall" in read("DECISION-CLASSES.md")
      and "decision_classes" in st["governance"])
check("substantial-result checklist is DRAFT, not frozen",
      "NOT FROZEN" in read("SUBSTANTIAL-RESULT-CHECKLIST-DRAFT.md")
      and "Pratyush's signature" in read("SUBSTANTIAL-RESULT-CHECKLIST-DRAFT.md"))
check("top invariant pair present in status.json",
      any("never certifies evidence" in i for i in st["architecture"].get("invariants", [])))
check("every registry entry carries a decision_class",
      all("decision_class" in q_ for q_ in qreg["questions"]))

# --- governance refinements (2026-07-05): monotonicity, lifecycle order, event-time packets ---
check("monotonic-classification guard present in worker_guard",
      "AUTOMATED DE-ESCALATION" in read("Scripts/worker_guard.py")
      and "DECLASSIFICATIONS.md" in read("Scripts/worker_guard.py"))
check("declassification register exists, human-only",
      "HUMAN-ONLY" in read("DECLASSIFICATIONS.md"))
check("destroy-protocol infrastructure present, none frozen",
      "No protocol is frozen yet" in read("protocols/README.md"))
import glob as _g
for prf in _g.glob(os.path.join(ROOT, "protocols", "*.json")):
    pr = json.loads(open(prf, encoding="utf-8").read())
    if pr.get("frozen_at"):
        check(f"frozen protocol has frozen_by: {os.path.basename(prf)}", bool(pr.get("frozen_by")))
props = _g.glob(os.path.join(ROOT, ".automation", "promotion_proposals", "*.json"))
for ppf in props:
    pp = json.loads(open(ppf, encoding="utf-8").read())
    prf = os.path.join(ROOT, pp.get("protocol", ""))
    ok_proto = os.path.exists(prf) and json.loads(open(prf, encoding="utf-8").read()).get("frozen_at")
    check(f"proposal {os.path.basename(ppf)}: references a FROZEN protocol", bool(ok_proto),
          "INADMISSIBLE: protocol missing or unfrozen")
    if ok_proto:
        chain = [json.loads(open(prf, encoding="utf-8").read())["frozen_at"],
                 pp.get("run_started_at", ""), pp.get("evidence_collected_at", ""),
                 pp.get("proposed_at", "")]
        check(f"proposal {os.path.basename(ppf)}: lifecycle order frozen<run<evidence<proposed",
              all(chain) and chain == sorted(chain) and len(set(chain)) == 4,
              "INADMISSIBLE as substantial-result candidate: timestamp order violated")
    check(f"proposal {os.path.basename(ppf)}: carries event-time packet", "packet" in pp,
          "NO packet -> NOT reviewable; provenance cannot be manufactured retroactively")
print(f"  ok   lifecycle guard active ({len(props)} promotion proposal(s) on file; vacuously green when zero)")
check("event-time packet clause in WORKER-CONTRACT",
      "event-time" in read("WORKER-CONTRACT.md") and "never reconstructed retroactively" in read("WORKER-CONTRACT.md"))
check("review instrumentation is diagnostic-only",
      "NEVER TARGET" in read("Scripts/review_metric.py").upper()
      and "not running" in read("Scripts/review_metric.py").lower())

# --- v1.2 + v2.0 (2026-07-06): crypto freeze, root of trust, stopping rule, two-object rule ---
mfj = json.loads(read("MANIFEST.sha256.json"))
check("manifest present with core + files sections",
      bool(mfj.get("core")) and bool(mfj.get("files")))
check("constitutional core pins validator + guard + class rules + dep schema + gov version",
      all(k in mfj["core"] for k in ("validate.py", "Scripts/worker_guard.py",
                                     "DECISION-CLASSES.md", "DEPENDENCIES.json",
                                     "GOVERNANCE-VERSION.json", "WORKER-CONTRACT.md")))
vsrc = read("validate.py")
check("root of trust: core verified FIRST, hard-fails downstream",
      "ROOT OF TRUST" in vsrc and "CORE COMPROMISED" in vsrc
      and vsrc.index("ROOT OF TRUST") < vsrc.index("version drift"))
gv = json.loads(read("GOVERNANCE-VERSION.json"))
check("governance v2.0: machinery in force, FREEZE ACT queued Class-A (not self-executed)",
      gv["version"] == "2.0" and gv["frozen"] is False
      and "CLASS-A" in gv["freeze_status"].upper()
      and "execution_evidence" in gv["reopen_evidence_stream"]
      and any("Deterministic software decides" in i for i in gv["invariants"]))
check("freeze-ratification item is in the Class-A queue",
      any(q_["id"] == "Q-GOV-V2-FREEZE" and q_["decision_class"] == "A"
          and q_["owner"] == "human" for q_ in qreg["questions"]))
check("observation schema pre-registered (exactly the six signals)",
      gv["observation_schema"] == ["queue-scaling", "packet-sufficiency", "validator-effectiveness",
                                   "dependency-declaration-accuracy", "automation-time-savings",
                                   "token-resource-efficiency"])
check("observation is not ratification (failures admit proposals, never rewrite rules)",
      "never auto-rewrites" in gv["observation_vs_ratification"])
check("constitutional core CLOSED: manifest core == declared core list (incl. the router)",
      set(mfj["core"].keys()) == set(gv["constitutional_core"])
      and "Scripts/cycle_check.py" in gv["constitutional_core"])
check("self-referential fixed point: the boundary list itself is inside the core",
      "GOVERNANCE-VERSION.json" in gv["constitutional_core"]
      and "GOVERNANCE-VERSION.json" in mfj["core"]
      and "BOUNDARY LIST ITSELF" in gv["core_closure"].upper())
check("decision vs enforcement recorded as separate states",
      "decision_status" in gv.get("decision_vs_enforcement", {})
      and "enforcement_status" in gv["decision_vs_enforcement"]
      and "NOT the enforcement milestone" in gv["decision_vs_enforcement"]["enforcement_status"])

# --- read-model invariant (2026-07-06): projections never carry or gate governance ---
PROJECTIONS = ("SNAPSHOT.md", "DECISIONS.md", "EVIDENCE-RIVER.md", "snapshot.json", "status.html")
pinned_all = list(mfj["core"].keys()) + list(mfj["files"].keys())
check("read-model: projections are never manifest-pinned as governance",
      not any(os.path.basename(p) in PROJECTIONS for p in pinned_all))
depdecl = json.loads(read("DEPENDENCIES.json"))["declarations"]
check("read-model: projections never appear in dependency declarations",
      not any(os.path.basename(d) in PROJECTIONS for v in depdecl.values() for d in v))
check("read-model + packaging principles recorded",
      "read-only PROJECTIONS" in read("READ-MODEL-AND-PACKAGING.md")
      and "Result Package #001" in read("READ-MODEL-AND-PACKAGING.md")
      and "never confer" in read("READ-MODEL-AND-PACKAGING.md"))
check("river diagnostic live in the generated view",
      "River health" in read("EVIDENCE-RIVER.md") if os.path.exists(os.path.join(ROOT, "EVIDENCE-RIVER.md")) else True)
check("stage0 gate is the pinned router (steward-authorized core change)",
      "Scripts/stage0_gate.py" in gv["constitutional_core"]
      and "Scripts/stage0_gate.py" in mfj["core"])
check("evidence writers tag pre-registered signals",
      '"signal": "validator-effectiveness"' in read("Scripts/cycle_check.py")
      and '"signal": "validator-effectiveness"' in read("Scripts/worker_guard.py"))
check("halt-not-degrade: missing dependency declaration halts the producer",
      "HALT: DEPENDENCIES.json missing" in read("Scripts/brute_force_step.py"))
cbq_txt = read(".automation/class_b_queue.md")
check("class-B queue carries the stop-line marker",
      "GOVERNANCE v2.0 STOP-LINE" in cbq_txt)
post = cbq_txt.split("GOVERNANCE v2.0 STOP-LINE")[1]
post_rows = [l for l in post.splitlines() if l.startswith("- ")]
for r in post_rows:
    check("post-freeze proposal cites execution evidence", "execution-evidence:" in r, r[:80])
check("escalation metrics: flag-for-human only, never auto-tighten",
      "NEVER auto-tighten" in read("Scripts/governance_metrics.py")
      or "NEVER auto-tighten" in read("Scripts/governance_metrics.py").replace("may NEVER", "NEVER"))
check("dependency declarations versioned",
      json.loads(read("DEPENDENCIES.json"))["_meta"]["version"] == "1.0")
check("canonical evidence-band vocabulary recorded",
      "builder-supported / independently-reproduced / finite-verified" in read("DECISION-CLASSES.md"))
for view in ("SNAPSHOT.md", "DECISIONS.md"):
    if os.path.exists(os.path.join(ROOT, view)):
        check(f"two-object separation: no review-metric fields in {view}",
              not any(t in read(view) for t in ("confidence_after", "additional_context_requested")))
check("SUPERSEDED + one-live-packet mechanism present",
      "SUPERSEDED" in read("Scripts/brute_force_step.py")
      and "exactly one per decision" in read("Scripts/brute_force_step.py"))
check("retrospective labeling rule recorded",
      "retrospective" in gv.get("retrospective_rule", ""))

# --- 7. honest checks: register leaks, silent conjecture-dependence, withdrawn citations ---
# (a) felt-register / Journal language must not leak into Ledger A prose
FELT = re.compile(r"\b(love|silence|faith|orientation|mercy|sacred)\b", re.I)
for dirpath, _, files in os.walk(os.path.join(ROOT, "LedgerA")):
    if os.path.basename(dirpath) == "archive": continue
    for f in files:
        if not f.endswith(".md"): continue
        rel = os.path.relpath(os.path.join(dirpath, f), ROOT)
        hits = sorted({m.group(0).lower() for m in FELT.finditer(read(rel))})
        check(f"no felt-register leak in {f}", not hits, f"found {hits}")

# (b) a stated result must not silently depend on a conjecture:
# any Ledger-A section citing a token whose registry entry is state=conjecture
# must carry a band marker in that section.
MARKERS = re.compile(r"conjecture|candidate|pending|band|held", re.I)
CONJ_TOKENS = {"R1": "Q-R1-GENERAL", "R2": "Q-R2-BAND"}
conj_states = {q["id"]: q["state"] for q in qreg["questions"]}
sections = re.split(r"^## ", can, flags=re.M)
for tok, qid in CONJ_TOKENS.items():
    if conj_states.get(qid) != "conjecture": continue
    pat = re.compile(rf"\b{tok}\b")
    for i, sec in enumerate(sections):
        if pat.search(sec):
            title = sec.splitlines()[0][:50] if sec else "(header)"
            check(f"conjecture-cite banded: {tok} in section '{title}'", bool(MARKERS.search(sec)))

# (c) withdrawn items must not be cited by Ledgers A-D
ev_txt = read("LedgerE/evidence_log.md")
withdrawn = []
for r in ev_txt.splitlines():
    cells = [c.strip() for c in r.strip().strip("|").split("|")]
    if len(cells) == 6 and "WITHDRAWN" in cells[4].upper():
        withdrawn.append(cells[1].split(" (")[0].strip())
for w in withdrawn:
    for d in ("LedgerA", "LedgerB", "LedgerC", "LedgerD"):
        for dirpath, _, files in os.walk(os.path.join(ROOT, d)):
            if os.path.basename(dirpath) == "archive": continue
            for f in files:
                if not f.endswith(".md"): continue
                rel = os.path.relpath(os.path.join(dirpath, f), ROOT)
                check(f"withdrawn '{w}' not cited in {rel}", w not in read(rel))

# --- 8. structured counts: internal coherence + ledger prose sync ---
cj = json.loads(read("counts.json"))
LEVELS = set(cj["_meta"]["verification_levels"])
for k, v in cj["counts"].items():
    f = v["fraction_nondeterministic"]
    check(f"counts {k}: total = det + nondet",
          v["count_total"] == v["count_deterministic"] + v["count_nondeterministic"])
    check(f"counts {k}: fraction fields consistent",
          f["numerator"] == v["count_nondeterministic"] and f["denominator"] == v["count_total"]
          and abs(f["value"] - (f["numerator"] / f["denominator"] if f["denominator"] else 0)) < 5e-5)
    check(f"counts {k}: verification level valid", v.get("verification") in LEVELS)
# ledger prose renders 'N of M' from counts.json (no bare-ratio drift)
for key in ("feq-free-n2", "feq-free-n3"):
    f = cj["counts"][key]["fraction_nondeterministic"]
    check(f"ladder prose matches counts.json ({key})",
          f"{f['numerator']} of {f['denominator']}" in can)
check("ladder cites counts.json ids", "feq-free-n2" in can and "feq-subid-n2" in can and "feq-strict-n2" in can)
check("no bare slash-ratio in ladder row", "56 survivors / 37" not in can and "4400 / 4087" not in can)

# --- 9. ARCHITECTURE.md status labels must not drift from actual ledger versions ---
arch = read("ARCHITECTURE.md")
can_ver = re.search(r"v(0\.\d+) · CANONICAL", can).group(1)
prot_ver = re.search(r"v(0\.\d+)", prot).group(1)
check("ARCHITECTURE Ledger-A label matches canonical version", f"v{can_ver}" in
      re.search(r"^## Ledger A[^\n]*", arch, re.M).group(0))
check("ARCHITECTURE Ledger-B label matches protocol version", f"v{prot_ver}" in
      re.search(r"^## Ledger B[^\n]*", arch, re.M).group(0))

# --- 10. governance firewall stated in README ---
rd = read("README.md")
check("firewall: procedures only", "executes procedures only" in rd)
check("firewall: no C admission / B change / promotion / D", all(
    s in rd for s in ["admit a Ledger-C entry", "change Ledger B", "promote conjecture", "touch Ledger D"]))

if FAIL:
    print(f"\nCONSISTENCY FAILED ({len(FAIL)}): {FAIL}")
    sys.exit(1)
print("\nCONSISTENCY: ALL CROSS-REFERENCES AND SCHEMAS COHERENT.")

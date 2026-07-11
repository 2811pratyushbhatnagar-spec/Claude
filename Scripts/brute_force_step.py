#!/usr/bin/env python3
"""brute_force_step.py -- resumable brute-force chunk step, called by cycle_check.py.

PROCEDURES ONLY, per WORKER-CONTRACT.md. Advances a BOUNDED, time-boxed chunk of the open
computational frontier each cycle; persists progress to .automation/bf_state.json (excluded
from canon via .gitignore); banks ALL outcomes INCLUDING NEGATIVES to .automation/bf_findings.md
and appends completion/negative rows to Ledger E (append-only). It EXHAUSTS the search and
records nulls; it never declares contact with physics -- a forced bridge, if one ever surfaced,
goes to Tier-3 ratification. No new scheduled task: this runs inside the existing 5h cycle.

Usage: python brute_force_step.py [--repo PATH] [--budget SECONDS] [--status]
"""
import argparse, json, os, sys, time, glob, datetime, hashlib, subprocess

def now(): return datetime.datetime.now().astimezone().isoformat(timespec="seconds")

def evidence_packet(repo, deps=None):
    """EVENT-TIME packet, emitted at production (never reconstructed later). Carries ground-truth
    provenance + dependency hashes. STALE is purely mechanical: the packet is STALE iff any
    declared-dependency hash differs from the hash recorded here at emission -- no judgment.
    Dependency declarations come from versioned, manifest-pinned DEPENDENCIES.json."""
    dep_decl_ver, dep_decl_hash = None, None
    if deps is None:
        dj = os.path.join(repo, "DEPENDENCIES.json")
        if not os.path.exists(dj):
            # HALT-NOT-DEGRADE: a missing dependency declaration halts; it never silently degrades.
            print("HALT: DEPENDENCIES.json missing -- packets cannot be emitted without a "
                  "versioned dependency declaration (budget_rule: halt-not-degrade)")
            sys.exit(1)
        raw = open(dj, "rb").read()
        decl = json.loads(raw)
        deps = tuple(decl["declarations"]["brute_force_step"])
        dep_decl_ver = decl["_meta"]["version"]
        dep_decl_hash = hashlib.sha256(raw).hexdigest()[:12]
    dep_hashes = {}
    for d in deps:
        p = os.path.join(repo, d)
        if os.path.exists(p):
            dep_hashes[d] = hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]
    head = None
    try:
        r = subprocess.run(["git", "-C", repo, "rev-parse", "--short", "HEAD"],
                           capture_output=True, text=True, timeout=10)
        head = r.stdout.strip() or None
    except Exception:
        pass
    return {"produced_at": now(), "producer": "Scripts/brute_force_step.py",
            "repo_head": head, "dep_hashes": dep_hashes,
            "dep_declaration": {"version": dep_decl_ver, "hash": dep_decl_hash},
            "class": "C (evidence record; never presentable as Class-A)"}

# ---------- bitmask relation machinery (rows as bit-ints; rel = tuple of n rows) ----------
def build_T(n):
    """T[rel_key][rowbits] = OR of rel's rows selected by rowbits. rel_key packs n rows of n bits."""
    size = 1 << (n * n)
    rows_of = []
    T = []
    mask = (1 << n) - 1
    for key in range(size):
        rows = tuple((key >> (n * i)) & mask for i in range(n))
        rows_of.append(rows)
        t = [0] * (1 << n)
        for rb in range(1 << n):
            acc = 0; b = rb; i = 0
            while b:
                if b & 1: acc |= rows[i]
                b >>= 1; i += 1
            t[rb] = acc
        T.append(t)
    return T, rows_of

def compose_key(FrowsList, TG):
    return tuple(TG[fr] for fr in FrowsList)

def is_subdiag(rows, n):  return all(rows[i] & ~(1 << i) == 0 for i in range(n))
def contains_diag(rows, n): return all(rows[i] >> i & 1 for i in range(n))
def is_diag(rows, n):     return all(rows[i] == (1 << i) for i in range(n))
def single_valued(rows):  return all(r == 0 or (r & (r - 1)) == 0 for r in rows)

def sweep(n, F_start, F_end, T, rows_of, counts, budget_end):
    """Fused predicates over (F,G) pairs, F in [F_start, F_end): free F-eq via F;G;F=F and
    G;F;G=G (reduction: absorption+idempotence equivalent under forced identities E0=F;G,
    E1=G;F -- verified at init); strict F-eq / F-sup / F-sub with RET fractions in same pass."""
    size = 1 << (n * n)
    F = F_start
    while F < F_end:
        if time.monotonic() > budget_end:
            return F, False
        Frows = rows_of[F]; TF = T[F]
        for G in range(size):
            TG = T[G]
            FG = tuple(TG[fr] for fr in Frows)          # rows of F;G
            FGF = tuple(TF[r] for r in FG)               # rows of (F;G);F
            if FGF == Frows:
                Grows = rows_of[G]
                GF = tuple(TF[gr] for gr in Grows)
                GFG = tuple(TG[r] for r in GF)
                if GFG == Grows:
                    counts["feq_free"] += 1
                    E0, E1 = FG, GF
                    if not (single_valued(E0) and single_valued(E1) and
                            single_valued(Frows) and single_valued(Grows)):
                        counts["feq_free_nondet"] += 1
                        if len(counts["nondet_witnesses"]) < 3:
                            counts["nondet_witnesses"].append({"F": F, "G": G})
                    if is_diag(E0, n) and is_diag(E1, n):
                        counts["feq_strict"] += 1
                    elif is_subdiag(E0, n) and is_subdiag(E1, n):
                        counts["feq_partial_proper"] += 1
            else:
                Grows = rows_of[G]
                GF = tuple(TF[gr] for gr in Grows)
            # strict-rung inclusions (identities pinned to diagonal)
            sup = is_subdiag(FG, n) and is_subdiag(GF, n)        # composed <= Delta
            sub = contains_diag(FG, n) and contains_diag(GF, n)  # Delta <= composed
            if sup:
                counts["fsup_strict"] += 1
                if sub: counts["fsup_strict_retE"] += 1
            if sub:
                counts["fsub_strict"] += 1
                if sup: counts["fsub_strict_retX"] += 1
        F += 1
    return F, True

def run_reference(n):
    """Full sweep at small n for self-verification against deposited counts."""
    T, rows_of = build_T(n)
    counts = dict(feq_free=0, feq_free_nondet=0, feq_strict=0, feq_partial_proper=0,
                  fsup_strict=0, fsup_strict_retE=0, fsub_strict=0, fsub_strict_retX=0,
                  nondet_witnesses=[])
    sweep(n, 0, 1 << (n * n), T, rows_of, counts, time.monotonic() + 10**9)
    return counts

# ---------- banking ----------
def bank(repo, title, body):
    p = os.path.join(repo, ".automation", "bf_findings.md")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    new = not os.path.exists(p)
    pk = evidence_packet(repo)
    with open(p, "a", encoding="utf-8") as f:
        if new:
            f.write("# Brute-force findings bank -- append-only; negatives are findings, not failures\n\n")
        f.write(f"## {now()} -- {title}\n{body}\n\nevidence-packet (event-time): `{json.dumps(pk)}`\n\n")

def ledgerE_append(repo, artifact, action, evidence, disposition, reason):
    p = os.path.join(repo, "LedgerE", "evidence_log.md")
    if not os.path.exists(p): return
    lines = open(p, encoding="utf-8").read().splitlines()
    last_row = max(i for i, l in enumerate(lines) if l.startswith("|"))
    row = f"| {now()[:10]} | {artifact} | {action} | {evidence} | {disposition} | {reason} |"
    lines.insert(last_row + 1, row)
    open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")

def check_stale_packets(repo):
    """Dependency-scoped staleness (DECISION-CLASSES v1.1 (4)): a stored packet is STALE iff
    something in ITS OWN dep-closure changed -- unrelated commits never invalidate the queue.
    Stale packets are marked 'STALE -- regenerate before review' in the cycle output; they are
    ineligible for approval until regenerated (regeneration re-derives class monotonically)."""
    def cur_hash(d):
        p = os.path.join(repo, d)
        return hashlib.sha256(open(p, "rb").read()).hexdigest()[:12] if os.path.exists(p) else None
    def stale_deps(pk):
        return [d for d, h in pk.get("dep_hashes", {}).items()
                if cur_hash(d) is not None and cur_hash(d) != h]
    out = []
    bank_p = os.path.join(repo, ".automation", "bf_findings.md")
    if os.path.exists(bank_p):
        title = "?"
        for line in open(bank_p, encoding="utf-8"):
            s = line.strip()
            if s.startswith("## "):
                title = s[3:]
            elif s.startswith("evidence-packet (event-time): `"):
                try:
                    pk = json.loads(s[len("evidence-packet (event-time): `"):-1])
                    sd = stale_deps(pk)
                    if sd:
                        out.append(f"STALE -- regenerate before review: bank entry '{title[:60]}' (changed deps: {', '.join(sd)})")
                except Exception:
                    out.append(f"UNPARSEABLE packet under '{title[:60]}' -- treat as no-packet (not reviewable)")
    # promotion proposals: STALE + SUPERSEDED states, with the one-live-packet invariant.
    # SUPERSEDED = a newer packet exists for the same decision; every decision has exactly ONE
    # live (non-stale, non-superseded) packet = the review target; priors retained append-only.
    by_item = {}
    for ppf in glob.glob(os.path.join(repo, ".automation", "promotion_proposals", "*.json")):
        try:
            pp = json.load(open(ppf, encoding="utf-8"))
            by_item.setdefault(pp.get("item", "?"), []).append((pp.get("proposed_at", ""), ppf, pp))
        except Exception:
            out.append(f"UNPARSEABLE proposal {os.path.basename(ppf)} -- not reviewable")
    for item, props in by_item.items():
        props.sort()  # newest proposed_at last
        for _, ppf, pp in props[:-1]:
            out.append(f"SUPERSEDED (retained): proposal {os.path.basename(ppf)} for {item} -- newer packet exists")
        _, ppf, pp = props[-1]
        sd = stale_deps(pp.get("packet", {}))
        if sd:
            out.append(f"STALE -- regenerate before review: proposal {os.path.basename(ppf)} for {item} (changed deps: {', '.join(sd)})")
        else:
            out.append(f"LIVE review target for {item}: {os.path.basename(ppf)} (exactly one per decision)")
    return out

# ---------- the queue ----------
def default_state():
    return {
        "created": now(), "reduction_verified": False,
        "queue": [
            {"id": "BF-1", "title": "n=4 free-rung F-eq enumeration + strict F-sup/F-sub + RET (fused pass)",
             "status": "active", "next_F": 0, "space": 1 << 16,
             "counts": dict(feq_free=0, feq_free_nondet=0, feq_strict=0, feq_partial_proper=0,
                            fsup_strict=0, fsup_strict_retE=0, fsub_strict=0, fsub_strict_retX=0,
                            nondet_witnesses=[]),
             "milestones_banked": [], "chunks": 0, "seconds": 0.0,
             "cross_checks": "on completion: feq_strict must equal 24 = 4! and partial-proper must equal 209-24=185 (audit's blind-prediction values)"},
            {"id": "BF-2", "title": "exact-number diff vs ledger_a_verify.py",
             "status": "pending-material", "probe_paths": [
                 r"C:\Users\Bhatnagar\Desktop", r"C:\Users\Bhatnagar\Desktop\New folder (2)",
                 r"C:\Users\Bhatnagar\Desktop\New folder (2)\framework",
                 r"C:\Users\Bhatnagar\Desktop\code\framework"]},
            {"id": "BF-3", "title": "forced-bridge null certificate (physics bar: forced-only)",
             "status": "active", "last_horizon": ""},
            {"id": "BF-4", "title": "Q-CONVERGE composition-semantics probe",
             "status": "queued-design",
             "note": "no compute until iteration/composition semantics formulated on the frozen signature; automation-audit may draft"},
            {"id": "BF-5", "title": "further range extensions (automation-audit enqueues here)",
             "status": "open-slot"},
        ],
        "history": [],
    }

def null_certificate(repo, bf1):
    horizon = "n<=3 complete (regression-guarded); n=4 strict+partial audit-verified; n=4 free rung at F=%d/65536 (%.1f%%)" % (
        bf1["next_F"], 100.0 * bf1["next_F"] / bf1["space"])
    body = f"""# Forced-bridge null certificate -- regenerated {now()} · Class-C evidence record
(never presentable as a Class-A result; certification is human-only)
**Physics bar: forced-only. This certificate EXHAUSTS what the frozen Ledger-A axioms produce and
records that none of it forces a physical quantity. It never declares contact.**

Complete list of canonical invariants produced by Ledger A at the current horizon:
- survivor counts: strict n=2,3(,4 audit) = n! (2, 6, 24); sub-identity = sum C(n,k)^2 k! (7, 34, 209 audit);
  free-rung = 56 (n=2), 4400 (n=3), n=4 in progress
- structure identifications at verified scales: S_n (strict), I_n (sub-identity) -- finite-verified n=2,3
- the maximal-point class: transitive groupoid acting on state fibers
- R2 return-halves fractions (RET-existence / RET-exclusivity under F-sup / F-sub)

Finding (NULL, standing): no identification of any of these with a physical quantity is forced.
Every candidate mapping requires an imported unit, an imported interpretation, or an imported
dynamics -- consistent with the cross-track deflation on record (spacetime dimension imported, not
forced; 'universe as must/may object' held at register 2, interpretation-variant). A forced bridge,
if one ever surfaces, is a Tier-3 ratification item, never auto-promoted.

Horizon: {horizon}
"""
    with open(os.path.join(repo, ".automation", "bf_null_certificate.md"), "w", encoding="utf-8") as f:
        f.write(body)
    return horizon

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo"); ap.add_argument("--budget", type=float, default=240.0)
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.abspath(args.repo) if args.repo else os.path.dirname(script_dir)
    spath = os.path.join(repo, ".automation", "bf_state.json")
    state = default_state()
    if os.path.exists(spath):
        try: state = json.load(open(spath, encoding="utf-8"))
        except Exception: pass
    bf1, bf2, bf3 = state["queue"][0], state["queue"][1], state["queue"][2]

    if args.status:
        print(json.dumps({"queue": [{k: v for k, v in q.items() if k != "counts"} for q in state["queue"]],
                          "bf1_counts": bf1["counts"]}, indent=2)); return

    t_end = time.monotonic() + args.budget
    log = []

    # 0. one-time self-verification of the FGF/GFG reduction against deposited counts
    if not state["reduction_verified"]:
        c2, c3 = run_reference(2), run_reference(3)
        ok = (c2["feq_free"], c2["feq_free_nondet"], c3["feq_free"], c3["feq_free_nondet"],
              c2["fsup_strict"], c2["fsub_strict"], c3["fsup_strict"], c3["fsub_strict"],
              c2["fsup_strict_retE"], c3["fsup_strict_retE"]) == (56, 37, 4400, 4087, 49, 31, 1650, 25057, 2, 6)
        state["reduction_verified"] = bool(ok)
        log.append(f"reduction self-test: {'PASS' if ok else 'FAIL'} (n=2: {c2['feq_free']}/{c2['feq_free_nondet']}, n=3: {c3['feq_free']}/{c3['feq_free_nondet']}; strict sup/sub n=2 {c2['fsup_strict']}/{c2['fsub_strict']}, n=3 {c3['fsup_strict']}/{c3['fsub_strict']})")
        if not ok:
            bank(repo, "BF SELF-TEST FAILURE", "reduction did not reproduce deposited counts; halting queue. " + json.dumps({"n2": c2, "n3": c3}))
            ledgerE_append(repo, "Brute-force queue self-test", "halted", "FGF/GFG reduction failed to reproduce deposited counts", "HALTED", "investigate before any chunk runs")
            json.dump(state, open(spath, "w", encoding="utf-8"), indent=2); print("\n".join(log)); sys.exit(1)

    # 1. BF-2 probe: has ledger_a_verify.py appeared?
    if bf2["status"] == "pending-material":
        found = [os.path.join(d, "ledger_a_verify.py") for d in bf2["probe_paths"]
                 if os.path.exists(os.path.join(d, "ledger_a_verify.py"))]
        if found:
            bf2["status"] = "material-arrived"; bf2["found_at"] = found[0]
            bank(repo, "BF-2: ledger_a_verify.py APPEARED", f"at {found[0]} -- run the exact-number diff next cycle; deposit a new dated reconciliation note (steward merges).")
            ledgerE_append(repo, "ledger_a_verify.py", "detected on disk", found[0], "MATERIAL ARRIVED", "exact-number diff now unblocked (BF-2)")
            log.append(f"BF-2: material arrived at {found[0]}")
        else:
            log.append("BF-2: ledger_a_verify.py still absent (probed %d paths)" % len(bf2["probe_paths"]))

    # 2. BF-1 chunk: n=4 fused sweep
    if bf1["status"] == "active" and time.monotonic() < t_end - 10:
        t0 = time.monotonic()
        T, rows_of = build_T(4)
        newF, complete = sweep(4, bf1["next_F"], bf1["space"], T, rows_of, bf1["counts"], t_end)
        dt = time.monotonic() - t0
        rate = (newF - bf1["next_F"]) / dt if dt > 0 else 0
        bf1["next_F"] = newF; bf1["chunks"] += 1; bf1["seconds"] += dt
        pct = 100.0 * newF / bf1["space"]
        eta_h = ((bf1["space"] - newF) / rate / 3600.0) if rate > 0 else -1
        log.append(f"BF-1 chunk {bf1['chunks']}: F={newF}/65536 ({pct:.1f}%), {rate:.1f} F/s, ~{eta_h:.1f} CPU-h remaining; interim: free={bf1['counts']['feq_free']} (nondet {bf1['counts']['feq_free_nondet']}), strict={bf1['counts']['feq_strict']}, sup={bf1['counts']['fsup_strict']}, sub={bf1['counts']['fsub_strict']}")
        for m in (25, 50, 75):
            if pct >= m and m not in bf1["milestones_banked"]:
                bf1["milestones_banked"].append(m)
                bank(repo, f"BF-1 milestone {m}%", log[-1])
        if complete:
            bf1["status"] = "complete"
            c = bf1["counts"]
            xcheck = (c["feq_strict"] == 24 and c["feq_strict"] + c["feq_partial_proper"] == 209)
            body = (f"n=4 COMPLETE. free F-eq survivors = {c['feq_free']} ({c['feq_free_nondet']} nondeterministic of {c['feq_free']}); "
                    f"strict = {c['feq_strict']} (expect 24 = 4!): {'MATCH' if c['feq_strict']==24 else 'MISMATCH'}; "
                    f"strict+partial-proper = {c['feq_strict']+c['feq_partial_proper']} (expect 209): {'MATCH' if xcheck else 'MISMATCH'}; "
                    f"F-sup strict = {c['fsup_strict']} (RET-E {c['fsup_strict_retE']}); F-sub strict = {c['fsub_strict']} (RET-! {c['fsub_strict_retX']}). "
                    f"NOVEL numbers: free-rung count + nondet fraction + n=4 R2 fractions. NULL also recorded if patterns hold (no break = substantive finding). Candidate for counts.json (regression-backed) + registry updates -- steward/instructed session applies.")
            bank(repo, "BF-1 COMPLETE: n=4 enumeration", body)
            ledgerE_append(repo, "n=4 free-rung enumeration (BF-1)", "completed by cycle automation", body[:400], "BANKED (candidate)", "resumable chunks across cycles; outcomes incl. any null are findings; canon updates await instructed session")
    elif bf1["status"] == "complete":
        log.append("BF-1: complete (banked)")

    # 2b. dependency-scoped staleness scan over all stored packets (Class-C reporting)
    for s in check_stale_packets(repo):
        log.append(s)

    # 3. BF-3: regenerate the null certificate at current horizon
    h = null_certificate(repo, bf1)
    if bf3.get("last_horizon") != h:
        bf3["last_horizon"] = h
        log.append("BF-3: null certificate regenerated -- " + h)

    state["history"].append({"t": now(), "log": log})
    state["history"] = state["history"][-50:]
    os.makedirs(os.path.dirname(spath), exist_ok=True)
    json.dump(state, open(spath, "w", encoding="utf-8"), indent=2)
    print("brute-force step:"); [print("  " + l) for l in log]

if __name__ == "__main__":
    main()

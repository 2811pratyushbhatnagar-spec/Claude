"""Self-driving transition rule -- operates BETWEEN rounds, on de-echoed summaries
only (the invariant + open disagreements), never on raw agent transcripts. So
adaptivity never contaminates independence.

next_mandate(rounds): the mandate for the NEXT parallel-blind round, decided by
the last round's signals ("the last round decides the next"). A *standing*
disagreement (unchanged across rounds) no longer forces perpetual Integration --
only a NEWLY-grown disagreement does; a reconciled/standing one lets the loop
proceed to a Diversity stress round and converge.
next_directive(...): when legs are gathered one at a time (e.g. the deferred
ChatGPT leg), also pick the least-recently-used independent path."""

ROLES = ["Construction", "Refutation", "Integration", "Diversity"]

def next_mandate(rounds, *, n_independent=2, tau=0.0, min_rounds=2,
                 max_rounds=6, patience=1):
    if not rounds:
        return "Construction"
    if len(rounds) >= max_rounds:
        return None
    last = rounds[-1]
    prev = rounds[-2] if len(rounds) >= 2 else None
    new_disagreement = bool(last["disagreements"]) and (
        prev is None or set(last["disagreements"]) != set(prev["disagreements"]))
    recent = [r["delta"] for r in rounds[-patience:]]
    stable = (len(rounds) >= min_rounds and all(d <= tau for d in recent)
              and last["independent_paths"] >= n_independent and last["invariant"])
    if stable and last["mandate"] == "Diversity":
        return None                       # survived a diversity stress round -> converged
    if last["delta"] > tau:
        return "Refutation"               # invariant still moving -> pressure it
    if new_disagreement:
        return "Integration"              # only reconcile NEWLY contested claims
    if last["mandate"] != "Diversity":
        return "Diversity"                # stable + standing disagreement -> stress once
    return "Construction"

def _pick_path(rounds, candidate_paths):
    last_used = {}
    for i, r in enumerate(rounds):
        for p in r.get("paths", []):
            last_used[tuple(p)] = i
    return sorted(candidate_paths, key=lambda p: last_used.get(tuple(p), -1))[0]

def next_directive(rounds, candidate_paths, **kw):
    m = next_mandate(rounds, **kw)
    if m is None:
        return None
    model, path = _pick_path(rounds, candidate_paths)
    return {"mandate": m, "model": model, "evidence_path": path}

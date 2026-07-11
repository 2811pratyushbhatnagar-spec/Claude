"""The convergence loop.

run_convergence: the base unit is a PARALLEL BLIND ROUND -- every worker answers
the same question independently, blind to the others (anti-echo). Between rounds,
the transition rule reads only the synthesised invariant + open disagreements and
sets the next round's mandate. The loop STOPS on stability, not stage-count."""
from __future__ import annotations
import json, time
from pathlib import Path
from invariant import extract_invariant, stability
from scheduler import next_mandate

def run_convergence(question, workers, *, n_independent=2, tau=0.0, min_rounds=2,
                    max_rounds=6, patience=1, replicates=1, logdir=None, gather=None):
    """`gather(question, mandate, round, workers)` may override how a round is
    collected (e.g. dispatch subagents concurrently). Default: call each worker
    once, blind to the others."""
    def _default_gather(q, mandate, rnd, ws):
        reps = []
        for _ in range(replicates):
            reps += [w.represent(q, mandate, rnd) for w in ws]   # blind: no cross-talk
        return reps
    gather = gather or _default_gather
    all_reps, rounds, prev = [], [], None
    while True:
        mandate = next_mandate(rounds, n_independent=n_independent, tau=tau,
                               min_rounds=min_rounds, max_rounds=max_rounds, patience=patience)
        if mandate is None:
            break
        rnd = len(rounds) + 1
        round_reps = gather(question, mandate, rnd, workers)     # PARALLEL BLIND ROUND
        all_reps += round_reps
        inv = extract_invariant(all_reps, n_independent)
        delta = stability(prev, inv); prev = inv
        rounds.append({"round": rnd, "mandate": mandate,
                       "paths": sorted({(r.model, r.evidence_path) for r in round_reps}),
                       "delta": round(delta, 4), "invariant": sorted(inv.claims),
                       "independent_paths": inv.independent_paths,
                       "distinct_models": len({r.model for r in all_reps}),
                       "disagreements": sorted(inv.disagreements)})
    converged = bool(rounds) and len(rounds) < max_rounds
    result = {"question": question, "converged": converged, "rounds": len(rounds),
              "stopped_by": "stability" if converged else "budget",
              "invariant": sorted(prev.claims) if prev else [],
              "independent_paths": prev.independent_paths if prev else 0,
              "distinct_models": len({r.model for r in all_reps}),
              "disagreements": sorted(prev.disagreements) if prev else [],
              "round_log": rounds}
    if logdir:
        p = Path(logdir); p.mkdir(parents=True, exist_ok=True)
        f = p / f"conv-{time.strftime('%Y%m%dT%H%M%S')}.json"
        f.write_text(json.dumps(result, indent=2)); result["log"] = str(f)
    return result

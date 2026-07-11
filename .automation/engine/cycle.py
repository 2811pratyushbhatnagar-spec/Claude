"""One scheduled cycle = ONE parallel-blind round, state persisted so the loop
KEEPS RUNNING across firings.

  python cycle.py --peek            # the mandate for the round to gather next
  python cycle.py --new round.json  # append this round's blind legs, recompute
  python cycle.py                   # recompute + print current status

round.json: list of {"agent_id","model","evidence_path","mandate","claims":[...]}.
State: runs/loop_state.json = {"question", "reps":[... with round & mandate]}."""
import argparse, json
from pathlib import Path
from invariant import Representation, extract_invariant, stability
from scheduler import next_mandate

STATE = Path("runs/loop_state.json")
CFG = dict(n_independent=2, tau=0.0, min_rounds=2, max_rounds=6, patience=1)

def load():
    if STATE.exists():
        return json.loads(STATE.read_text())
    q = Path("QUESTION.txt").read_text().strip() if Path("QUESTION.txt").exists() else "(no question)"
    return {"question": q, "reps": []}

def summarise(raw):
    reps = [Representation(r["agent_id"], r["model"], r["evidence_path"],
                           r.get("mandate", "?"), frozenset(r["claims"])) for r in raw]
    rounds, prev = [], None
    for ri in sorted({r.get("round", 1) for r in raw}):
        upto = [rep for rep, r in zip(reps, raw) if r.get("round", 1) <= ri]
        rr = [r for r in raw if r.get("round", 1) == ri]
        inv = extract_invariant(upto, CFG["n_independent"])
        rounds.append({"round": ri, "mandate": rr[0].get("mandate", "?"),
                       "paths": sorted({(x["model"], x["evidence_path"]) for x in rr}),
                       "delta": round(stability(prev, inv), 4), "invariant": sorted(inv.claims),
                       "independent_paths": inv.independent_paths,
                       "distinct_models": len({x.model for x in upto}),
                       "disagreements": sorted(inv.disagreements)})
        prev = inv
    return rounds, (prev if reps else None)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--new"); ap.add_argument("--peek", action="store_true")
    a = ap.parse_args()
    st = load()
    rounds, _ = summarise(st["reps"])
    if a.peek:
        print(json.dumps({"next_mandate": next_mandate(rounds, **CFG) or "CONVERGED"}, indent=2)); return
    if a.new:
        nxt = max([r.get("round", 0) for r in st["reps"]], default=0) + 1
        for r in json.loads(Path(a.new).read_text()):
            st["reps"].append({"agent_id": r["agent_id"], "model": r["model"],
                "evidence_path": r["evidence_path"], "mandate": r.get("mandate", "?"),
                "claims": list(r["claims"]), "round": nxt})
    rounds, inv = summarise(st["reps"])
    STATE.parent.mkdir(parents=True, exist_ok=True); STATE.write_text(json.dumps(st, indent=2))
    models = {r["model"] for r in st["reps"]}
    nm = next_mandate(rounds, **CFG)
    print(json.dumps({"question": st["question"], "rounds": len(rounds),
        "invariant": sorted(inv.claims) if inv else [],
        "independent_paths": inv.independent_paths if inv else 0,
        "distinct_models": len(models), "cross_model_ok": len(models) >= 2,
        "disagreements": sorted(inv.disagreements) if inv else [],
        "next_mandate": nm or "stable on current legs -- ChatGPT cross-model confirmation pending"},
        indent=2))

if __name__ == "__main__":
    main()

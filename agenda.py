# Query reads over questions.json + counts.json — views only, never mutates.
# NOT a graph database; the registry's dependency fields ARE the v1 graph.
#   python agenda.py                     -> all three reads (affected-demo uses Q-D5-BOUNDARY)
#   python agenda.py affected <ID>       -> what recomputes / is affected if <ID> changes
import json, os, sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
Q = json.load(open(os.path.join(HERE, "questions.json"), encoding="utf-8"))["questions"]
C = json.load(open(os.path.join(HERE, "counts.json"), encoding="utf-8"))["counts"]
by_id = {q["id"]: q for q in Q}

def affected(root):
    hit, frontier = [], {root}
    while frontier:
        nxt = set()
        for q in Q:
            if q["id"] in (h[0] for h in hit): continue
            deps = set(q["depends_on"])
            if deps & frontier:
                hit.append((q["id"], q["state"], q["invalidated_if"]))
                nxt.add(q["id"])
        frontier = nxt
    print(f"AFFECTED IF {root} CHANGES (transitive over depends_on):")
    if not hit: print("  (nothing depends on it)")
    for qid, st, inv in hit:
        print(f"  {qid} [{st}]")
        for i in inv: print(f"    invalidated_if: {i}")
    direct = by_id.get(root, {}).get("blocks", [])
    if direct: print(f"  also blocks (declared): {', '.join(direct)}")

def agenda():
    print("NEXT-AGENDA (open/investigating, prerequisites complete: no open/investigating Q-dep, no EXT- material):")
    for q in Q:
        if q["state"] not in ("open", "investigating"): continue
        if any(d.startswith("EXT-") for d in q["depends_on"]): continue
        qdeps = [d for d in q["depends_on"] if d.startswith("Q-")]
        if any(by_id[d]["state"] in ("open", "investigating") for d in qdeps): continue
        print(f"  {q['id']} [owner: {q['owner']}] — {q['next_action']}")

def unverified():
    print("COMPUTATIONS NOT EXTERNALLY AUDITED (from counts.json verification field):")
    for lvl in ("cross-confirmed", "builder-only"):
        rows = [(k, v) for k, v in C.items() if v["verification"] == lvl]
        if rows:
            print(f"  [{lvl}]")
            for k, v in rows:
                f = v["fraction_nondeterministic"]
                print(f"    {k}: {f['numerator']} of {f['denominator']} nondeterministic — {v['description']}")

def render_counts():
    print("GENERATED 'N of M' PROSE (from counts.json — the canonical rendering):")
    for k, v in C.items():
        f = v["fraction_nondeterministic"]
        print(f"  {k}: {f['numerator']} of {f['denominator']} nondeterministic "
              f"({v['count_deterministic']} deterministic of {v['count_total']} total; value {f['value']})")

print("[Class-D artifact — generated query view; never presentable as a Class-A result]\n")
if len(sys.argv) >= 3 and sys.argv[1] == "affected":
    affected(sys.argv[2])
else:
    affected("Q-D5-BOUNDARY"); print()
    agenda(); print()
    unverified(); print()
    render_counts()

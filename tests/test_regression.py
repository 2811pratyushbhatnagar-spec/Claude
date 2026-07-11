# Tier-1 REGRESSION: re-run the Ledger-A verification and ASSERT every reported count.
# Fails loudly (nonzero exit + named assertion) if any number changed.
import subprocess, sys, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAIL = []

def check(name, cond, detail=""):
    if cond: print(f"  ok   {name}")
    else:
        print(f"  FAIL {name}  {detail}")
        FAIL.append(name)

def run_script(rel):
    p = subprocess.run([sys.executable, os.path.join(ROOT, rel)],
                       capture_output=True, text=True, cwd=ROOT)
    if p.returncode != 0:
        print(p.stderr); FAIL.append(f"{rel} crashed"); return ""
    return p.stdout

print("== regression: Scripts/ledger_A_round2.py ==")
out = run_script("Scripts/ledger_A_round2.py")
EXPECT = [
    ("full space size", "space = 65536"),
    ("F-eq free-ids survivors/nondet/subdiag", "F-eq: survivors=56  nondeterministic=37  ids-subdiagonal=7"),
    ("F-sup free-ids survivors/nondet", "F-sup: survivors=3994  nondeterministic=2095  ids-subdiagonal=610"),
    ("F-sub free-ids survivors/nondet", "F-sub: survivors=679  nondeterministic=660  ids-subdiagonal=40"),
    ("R1 |S|=2 strict", "F-eq: survivors=2 | all det=True all total=True all inj=True | w1(existence) always=True w2(exclusivity) always=True"),
    ("F-sup strict n=2 survivors", "F-sup: survivors=49"),
    ("w1 7/49 under F-sup strict", "w1 holds in 7/49"),
    ("F-sub strict n=2 survivors", "F-sub: survivors=31"),
    ("w1 7/31 under F-sub strict", "w1 holds in 7/31"),
    ("partial-identity space", "space = 4096"),
    ("partial-identity survivors", "F-eq survivors=7 | partial bijections=7/7"),
    ("identities forced", "identities forced to dom/ran sub-diagonals: True"),
    ("|S|=3 space", "space = 262144"),
    ("R1 |S|=3", "F-eq: survivors=6 | all det+total+inj=True"),
    ("F-sup n=3 survivors", "F-sup: survivors=1650"),
    ("F-sub n=3 survivors", "F-sub: survivors=25057"),
    ("partial-identity n=3", "survivors=34 partial-bijections=34 nondet=0"),
]
for name, s in EXPECT:
    check(name, s in out, f"(missing: {s!r})")

print("== regression: Scripts/ledger_A_witnesses.py (W-series matrix) ==")
out = run_script("Scripts/ledger_A_witnesses.py")
MATRIX = {   # A1 A2 A3 A4 A5 F EI T R
    'W1':  'TTTTTTTTT', 'W2p': 'TTTFTTTTT', 'W3':  'TTTTTFFTF',
    'W4':  'TTTFTTTFF', 'W6':  'TTTTTFFTF', 'W7a': 'TTTFTFTFF',
    'W7b': 'TTTFTFTFF', 'W8':  'TTTFTTTTF', 'W9':  'TTFTTTTTT',
    'W10': 'TTTTTFTTT', 'W11': 'TTFTTTFTF', 'W12': 'TTTTTTTFT',
}
for line in out.splitlines():
    m = re.match(r'^(W\w+)\s+((?:[TF]\s*)+)$', line.strip())
    if m and m.group(1) in MATRIX:
        got = ''.join(m.group(2).split())
        check(f"matrix {m.group(1)}", got == MATRIX[m.group(1)], f"got {got}, expect {MATRIX[m.group(1)]}")
check("theorem: W11 loose-A3 breaks EI-derivation",
      "A3loose=True, F-eq=True, EI-strong=False" in out)
check("bonus: return without invertibility (W2p)",
      "A4=False but R=True, T=True" in out)

print("== regression: Proposition R2 RET counts (recomputed in-test) ==")
def compose(R, S): return frozenset((a, c) for (a, b) in R for (b2, c) in S if b == b2)
def diag(X): return frozenset((x, x) for x in X)
def rels(A, B):
    P = [(a, b) for a in A for b in B]
    for m in range(1 << len(P)):
        yield frozenset(p for i, p in enumerate(P) if m >> i & 1)
def ret_counts(S0, S1):
    D0, D1 = diag(S0), diag(S1)
    res = {}
    for mode in ('sup', 'sub'):
        ns = ne = nx = 0
        for F in rels(S0, S1):
            for G in rels(S1, S0):
                ee = [(compose(D0, D0), D0), (compose(D1, D1), D1),
                      (compose(D0, F), F), (compose(F, D1), F),
                      (compose(D1, G), G), (compose(G, D0), G),
                      (compose(F, G), D0), (compose(G, F), D1)]
                ok = all(l <= r for l, r in ee) if mode == 'sup' else all(r <= l for l, r in ee)
                if not ok: continue
                ns += 1
                FG, GF = compose(F, G), compose(G, F)
                if D0 <= FG and D1 <= GF: ne += 1
                if FG <= D0 and GF <= D1: nx += 1
        res[mode] = (ns, ne, nx)
    return res

r2 = ret_counts(('a', 'a2'), ('b', 'b2'))
check("R2(a) n=2: F-sup 49, RET-! free, RET-E 2", r2['sup'] == (49, 2, 49), f"got {r2['sup']}")
check("R2(b) n=2: F-sub 31, RET-E free, RET-! 2", r2['sub'] == (31, 31, 2), f"got {r2['sub']}")
r3 = ret_counts(('a', 'a2', 'a3'), ('b', 'b2', 'b3'))
check("R2(a) n=3: F-sup 1650, RET-! free, RET-E 6", r3['sup'] == (1650, 6, 1650), f"got {r3['sup']}")
check("R2(b) n=3: F-sub 25057, RET-E free, RET-! 6", r3['sub'] == (25057, 25057, 6), f"got {r3['sub']}")

print("== regression: D5 ladder free rung (identities forced E0=F;G, E1=G;F) ==")
def free_rung(S0, S1):
    ns = nd = 0
    for F in rels(S0, S1):
        for G in rels(S1, S0):
            E0, E1 = compose(F, G), compose(G, F)
            if compose(E0, E0) != E0 or compose(E1, E1) != E1: continue
            if compose(E0, F) != F or compose(F, E1) != F: continue
            if compose(E1, G) != G or compose(G, E0) != G: continue
            ns += 1
            det = all(len([t for (s, t) in F if s == s0]) <= 1 for s0 in S0) and \
                  all(len([t for (s, t) in G if s == s1]) <= 1 for s1 in S1)
            if not det: nd += 1
    return ns, nd
fr2 = free_rung(('a', 'a2'), ('b', 'b2'))
fr3 = free_rung(('a', 'a2', 'a3'), ('b', 'b2', 'b3'))
check("ladder free rung n=2: 37 of 56 nondet", fr2 == (56, 37))
check("ladder free rung n=3: 4087 of 4400 nondet", fr3 == (4400, 4087))

print("== regression: counts.json values vs recomputation / verified constants ==")
import json
cj = json.load(open(os.path.join(ROOT, "counts.json"), encoding="utf-8"))["counts"]
EXPECTED_COUNTS = {   # (total, nondeterministic) — every value independently asserted above
    "feq-free-n2": fr2, "feq-free-n3": fr3,
    "feq-subid-n2": (7, 0), "feq-subid-n3": (34, 0),
    "feq-strict-n2": (2, 0), "feq-strict-n3": (6, 0),
    "fsup-free-n2": (3994, 2095), "fsub-free-n2": (679, 660),
}
for k, (tot, nd) in EXPECTED_COUNTS.items():
    v = cj[k]
    check(f"counts.json {k} = {nd} of {tot}",
          v["count_total"] == tot and v["count_nondeterministic"] == nd,
          f"file has {v['count_nondeterministic']} of {v['count_total']}")

print("== regression: structure-map check (Q-D5-STRUCTURE-FINITE) ==")
from itertools import permutations as _perms
def conv(R): return frozenset((b, a) for (a, b) in R)
def eqs_ok(E0, E1, F, G):
    return (compose(E0, E0) == E0 and compose(E1, E1) == E1 and compose(E0, F) == F and
            compose(F, E1) == F and compose(E1, G) == G and compose(G, E0) == G and
            compose(F, G) == E0 and compose(G, F) == E1)
def structure_map(n, rung):
    S0 = tuple(f"a{i}" for i in range(n)); S1 = tuple(f"b{i}" for i in range(n))
    iota = {f"b{i}": f"a{i}" for i in range(n)}
    D0, D1 = diag(S0), diag(S1)
    sv = []
    for F in rels(S0, S1):
        for G in rels(S1, S0):
            E0, E1 = compose(F, G), compose(G, F)
            if rung == 'subid' and not (E0 <= D0 and E1 <= D1): continue
            if rung == 'strict' and not (E0 == D0 and E1 == D1): continue
            if eqs_ok(E0, E1, F, G): sv.append((F, G))
    enc = [frozenset((a, iota[b]) for (a, b) in F) for (F, G) in sv]
    if rung == 'subid':
        target = {R for R in rels(S0, S0)
                  if all(len([t for (s, t) in R if s == s0]) <= 1 for s0 in S0)
                  and all(len([s for (s, t) in R if t == t0]) <= 1 for t0 in S0)}
    else:
        target = {frozenset(zip(S0, p)) for p in _perms(S0)}
    c1 = len(enc) == len(set(enc)) == len(target) and set(enc) == target
    c2 = all(frozenset((iota[b], a) for (b, a) in G) == conv(e) for (F, G), e in zip(sv, enc))
    encset = set(enc)
    c3 = all(compose(x, y) in encset for x in encset for y in encset)
    return c1 and c2 and c3
for rung, nm in (('subid', 'I_n'), ('strict', 'S_n')):
    for n in (2, 3):
        check(f"structure map {nm} n={n} (completeness+converse+closure)", structure_map(n, rung))

if FAIL:
    print(f"\nREGRESSION FAILED ({len(FAIL)}): {FAIL}")
    sys.exit(1)
print("\nREGRESSION: ALL COUNTS MATCH THE FROZEN LEDGER.")

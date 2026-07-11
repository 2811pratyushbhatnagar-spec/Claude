#!/usr/bin/env python3
"""free_rung_repro_B.py -- Implementation B: independent reproduction of the FREE-rung counts.

MAXIMAL-INDEPENDENCE PROTOCOL (2026-07-06 directive):
- Built from the SPEC ONLY (pair groupoid, 8 F-eq equations, three identity-effect regimes).
- The regular-pair reduction was NOT inherited: it is re-DERIVED below as a claim and then
  VALIDATED against the RAW four-relation functor (all four effects assigned freely, all 8
  equations imposed directly, no reduction) exhaustively at n=2 -- the raw route is the modeling
  ground truth; the reduction earns its use at n=3,4 only by exact agreement at n=2.
- Representation-independent: boolean MATRIX semantics (numpy uint8 matmul), not bit-row tables,
  sharing no code or data structures with Implementation A (r1_ladder_n4.py, unread) or the
  repo's bit-table harnesses.

DERIVATION OF THE REDUCTION (verified mechanically below):
Under F-eq the 8 equations are equalities of composite effects. Writing juxtaposition for
relational composition: eq7: E0 = FG and eq8: E1 = GF force the identity effects outright.
Substituting: eq3 (E0 F = F) <=> FGF = F; eq4 (F E1 = F) <=> FGF = F (the same condition);
eq5 (E1 G = G) <=> GFG = G; eq6 (G E0 = G) <=> GFG = G. eq1 (E0 E0 = E0): (FG)(FG) = (FGF)G = FG
given FGF = F, so it is implied; eq2 likewise. Hence the 8 equations are EQUIVALENT to the
regular-pair conditions {FGF = F, GFG = G} with E0 = FG, E1 = GF defined. (Claim; validated raw.)

Nondeterminism (pinned definition, counts.json): SOME effect among E0,E1,F,G not single-valued
(a matrix row with >1 ones). Strict regime: E0 = E1 = Id; partial: E0,E1 <= Id.
Cross-check targets published for strict/partial (2/6/24, 7/34/209); FREE computed blind here.

Usage: python free_rung_repro_B.py [n]      (default: raw2 + n2 + n3; n=4 for the big run)
Output: JSON result line + running progress; results banked by the caller.
"""
import sys, json, time
import numpy as np

def all_relations(n):
    """All 2^(n*n) binary relations on n points as an (N, n, n) uint8 tensor."""
    N = 1 << (n * n)
    bits = ((np.arange(N)[:, None] >> np.arange(n * n)) & 1).astype(np.uint8)
    return bits.reshape(N, n, n)

def bmm(A, B):
    """Boolean matrix product; broadcasts over leading axes."""
    return (np.matmul(A.astype(np.uint16), B.astype(np.uint16)) > 0).astype(np.uint8)

def nondet_rows(M):
    """True where some row of M has more than one 1 (not single-valued)."""
    return (M.sum(axis=-1) > 1).any(axis=-1)

def raw_functor_n2():
    """Ground truth at n=2: enumerate ALL FOUR effects freely; impose the 8 equations directly."""
    R = all_relations(2)          # 16 relations
    surv = []
    for iE0 in range(16):
        for iE1 in range(16):
            for iF in range(16):
                for iG in range(16):
                    E0, E1, F, G = R[iE0], R[iE1], R[iF], R[iG]
                    if not np.array_equal(bmm(F, G), E0):  continue   # eq7
                    if not np.array_equal(bmm(G, F), E1):  continue   # eq8
                    if not np.array_equal(bmm(E0, E0), E0): continue  # eq1
                    if not np.array_equal(bmm(E1, E1), E1): continue  # eq2
                    if not np.array_equal(bmm(E0, F), F):  continue   # eq3
                    if not np.array_equal(bmm(F, E1), F):  continue   # eq4
                    if not np.array_equal(bmm(E1, G), G):  continue   # eq5
                    if not np.array_equal(bmm(G, E0), G):  continue   # eq6
                    surv.append((iF, iG))
    return surv

def sweep(n, progress_every=2048, out_path=None):
    """Reduction route (validated raw at n=2): count regular pairs FGF=F, GFG=G over all (F,G),
    with nondet classification and strict/partial/sup/sub/RET cross-checks in the same pass."""
    R = all_relations(n)
    N = len(R)
    I = np.eye(n, dtype=np.uint8)
    offdiag = 1 - I
    free = free_nondet = strict = partial = 0
    fsup = fsup_retE = fsub = fsub_retX = 0
    pairs_seen = set()  # only used at small n for raw cross-validation
    t0 = time.time()
    G_all = R  # (N, n, n)
    for iF in range(N):
        F = R[iF]
        FG = bmm(F[None, :, :], G_all)            # (N, n, n): F @ G for every G
        GF = bmm(G_all, F[None, :, :])            # (N, n, n): G @ F for every G
        # strict-identities inclusion theories (independent of regularity):
        sup_mask = ((FG * offdiag).sum((1, 2)) == 0) & ((GF * offdiag).sum((1, 2)) == 0)
        ret_mask = (FG[:, np.arange(n), np.arange(n)].min(1) == 1) & \
                   (GF[:, np.arange(n), np.arange(n)].min(1) == 1)
        fsup += int(sup_mask.sum()); fsup_retE += int((sup_mask & ret_mask).sum())
        fsub += int(ret_mask.sum()); fsub_retX += int((ret_mask & sup_mask).sum())
        # regular pairs: FGF = F and GFG = G
        FGF = bmm(FG, F[None, :, :])
        m1 = (FGF == F).all((1, 2))
        if m1.any():
            idx = np.nonzero(m1)[0]
            GFG = bmm(GF[idx], G_all[idx])
            m2 = (GFG == G_all[idx]).all((1, 2))
            good = idx[m2]
            free += int(len(good))
            if len(good):
                E0, E1 = FG[good], GF[good]
                nd = nondet_rows(E0) | nondet_rows(E1) | nondet_rows(G_all[good]) | \
                     bool(nondet_rows(F[None])[0])
                free_nondet += int(np.count_nonzero(nd))
                st = (E0 == I).all((1, 2)) & (E1 == I).all((1, 2))
                strict += int(st.sum())
                pa = ((E0 * offdiag).sum((1, 2)) == 0) & ((E1 * offdiag).sum((1, 2)) == 0)
                partial += int(pa.sum())
                if n == 2:
                    for g in good: pairs_seen.add((iF, int(g)))
        if progress_every and iF % progress_every == 0 and iF:
            el = time.time() - t0
            msg = f"  F={iF}/{N} ({100.0*iF/N:.1f}%) free={free} nondet={free_nondet} [{el:.0f}s, ETA {el/iF*(N-iF):.0f}s]"
            print(msg, flush=True)
            if out_path:
                open(out_path, "a", encoding="utf-8").write(msg + "\n")
    res = {"n": n, "free": free, "free_nondet": free_nondet, "free_det": free - free_nondet,
           "strict_xcheck": strict, "partial_xcheck": partial,
           "fsup_strict": fsup, "fsup_retE": fsup_retE, "fsub_strict": fsub, "fsub_retX": fsub_retX,
           "seconds": round(time.time() - t0, 1)}
    return res, pairs_seen

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "small"
    if which == "small":
        print("== RAW four-relation functor, n=2 (modeling ground truth; no reduction) ==")
        raw = raw_functor_n2()
        print(f"raw survivors (F,G pairs): {len(raw)}")
        r2, pairs2 = sweep(2, progress_every=0)
        agree = (set(raw) == pairs2) and (len(raw) == r2["free"])
        print(f"reduction route n=2: {json.dumps(r2)}")
        print(f"RAW == REDUCTION at n=2 (count AND exact survivor sets): {agree}")
        if not agree: sys.exit(1)
        r3, _ = sweep(3, progress_every=0)
        print(f"reduction route n=3: {json.dumps(r3)}")
    elif which == "4":
        out = sys.argv[2] if len(sys.argv) > 2 else None
        r4, _ = sweep(4, progress_every=2048, out_path=out)
        line = "RESULT_N4 " + json.dumps(r4)
        print(line)
        if out: open(out, "a", encoding="utf-8").write(line + "\n")

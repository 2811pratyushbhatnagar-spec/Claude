# BD Route 2 sufficiency — CLOSED NEGATIVE (counterexample packet)

**Claim.** The truncated interval-count vector `I_K(K=6)` is **not a sufficient geometry statistic**
for causal sets at `N=64`, under clean-room standard-CSQG conventions.

**Counterexample.** A valid transitive partial order whose raw low interval counts

    n0..n6 = [181, 122, 95, 77, 64, 55, 47]

sit at Mahalanobis `0.265` from the 2D-sprinkling raw-count mean
(95% scatter radius `3.71`), while its large-scale geometry is clearly non-2D:

- MM dimension: `1.32`
- ordering fraction: `0.814`
- height: `19`
- width: `8`
- tail mass > K: `0.609`

**Mechanism.** Relations are moved into intervals of size `> K`. The BD-visible truncated band
`n0..n6` stays pinned to manifold values while global geometry moves freely. The truncation is the vulnerability.

**Files.**
- `adversary_C.npy` / `adversary_C.txt` — adjacency matrix `C` (`C[i,j]=1` iff `i` precedes `j`)
- `raw_n0_n6.txt` — raw truncated interval-count vector
- `baseline_2d.npz` — 2D baseline mean, ridged covariance, scatter radii, geometry bands
- `metrics.json` — full record including allowed/barred conclusions and versions
- `bd_route2_bank.py` — generator and banking script

**Still allowed.** `I_K(K=6)` remains a useful *heuristic* discriminator for natural families.

**Barred.** BD action solved · spacetime derived · continuum bridge closed · GR/SM contact ·
full untruncated interval vector refuted · physical relevance of the adversary established · MoN-native physics result.

**Conventions.** Clean-room standard CSQG, **not** the MoN-native pipeline. Diff against the native
`I_K` definition / scatter before banking as native.

Round-trip validated: `True`. Reproduce: `python3 bd_route2_bank.py` (seed `20240608`).

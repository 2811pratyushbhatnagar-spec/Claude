# Reproduction Package (STAGED, NOT PUBLISHED): the FREE-rung survivor counts, n ≤ 4

*This package is a read-only, hash-signed rendering of results and their ACTUAL recorded status.
It displays status; it never confers it. Reading this — even reproducing it — certifies nothing;
the project's irreversible acts (promotion, admission, freezing, publication) are explicit named
endorsements made only by its steward. The one intended outcome of reading is understanding.*

## 1. What is claimed
For the pair groupoid with effect-assignments satisfying the eight functoriality equations
(composite effect = composed effects), with identity effects **unconstrained** ("FREE" regime),
the number of surviving assignments — equivalently, pairs (F, G) of binary relations with
FGF = F and GFG = G, identity effects then forced to FG and GF — is, **as a finite exhaustive
computation, independently corroborated by two implementations**:

| n (state-set size) | survivors | of which nondeterministic |
|---|---|---|
| 2 | 56 | 37 |
| 3 | 4,400 | 4,087 |
| 4 | **992,696** | **984,279** |

Corroborating cross-checks in the same computation: strict regime 2 / 6 / 24 = n!; sub-identity
regime 7 / 34 / 209 = Σₖ C(n,k)²k!; and at n=4 the return-halves corollary (RET-∃ ∧ RET-! = the
24-element strict core, under both inclusion theories).

## 2. What is NOT claimed
- **No general theorem is claimed by this package.** The related general statement (R1: strict
  regime forces bijective dynamics at every cardinality) has an audited proof text carried
  elsewhere with status *conjecture, promotion pending human ratification* — finite agreement at
  n ≤ 4 is not a proof of it and must not be read as one.
- **No physics, no interpretation, no ontology.** These are counts about a finite algebraic
  structure. Nothing here maps to a physical quantity; the project's own records hold that no
  such mapping is forced.
- Two n=4 side-quantities (F-sup 177,347; F-sub 423,054,463) are **single-source** and await
  their own reproduction — displayed as such, not as corroborated.

## 3. What evidence supports it
- `FREE-RUNG-REPRODUCTION-2026-07-06.md` — the two-implementation comparison object with the
  first-party **independent-derivation provenance block** (shared reduction: No; shared
  implementation: No; independent code: Yes; the single recorded limitation: non-literal
  blindness, documented rather than laundered).
- `free_rung_repro_B.py` — Implementation B, complete and self-contained: the reduction is
  re-derived in its header as a claim and validated against a RAW four-relation enumeration at
  n=2 (exact survivor-set agreement), then run at n=3, 4 with boolean-matrix semantics.
- Implementation A (independent origin, different representation) reported the same n=4 count
  before B ran; A's code was deliberately not read by B's author.

## 4. How to reproduce — or challenge — it
**Reproduce** (Python 3 + numpy):
```
python free_rung_repro_B.py small   # raw n=2 ground truth + reduction validation + n=2,3  (~1 min)
python free_rung_repro_B.py 4      # full n=4 sweep                                       (~30 min)
```
Expected: raw n=2 = 56 with exact set-agreement; RESULT_N4 line with free=992696,
free_nondet=984279, strict_xcheck=24, partial_xcheck=209.

**Challenge** (what would change the status):
- Write your own enumerator from §1's definition WITHOUT the FGF/GFG reduction (raw four-relation
  route) at any n — a divergent count at the first divergent n is a finding; report it rather
  than reconciling it away.
- Attack the reduction claim itself (header of `free_rung_repro_B.py`): a pair (F,G) satisfying
  the 8 equations whose identity effects are NOT FG/GF, or vice versa, would break it.
- Check the nondeterminism classification against its pinned definition (some effect among
  E0, E1, F, G not single-valued); the count under the narrower F-only reading differs by design.

`package_manifest.json` carries SHA-256 hashes of every file here plus the source-repo commit.

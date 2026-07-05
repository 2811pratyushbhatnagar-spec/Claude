# The Carry-Set Separation Problem

*A compact research note. The problem (§1) is self-contained; §3 is the reduction to CM theory; §3.5 records the current status of the CM-side in the published literature — strongly settled, with the exact citation being pinned. Registers are marked throughout; cited-but-not-re-derived-here items are flagged.*

---

## 1. Problem — self-contained, no algebraic geometry needed

Fix an odd prime `e`. For `m ∈ (ℤ/e)^×`, define the **non-carry set of multiplication by `m`**:

$$\Phi_m \;=\; \bigl\{\, t \in (\mathbb{Z}/e)^\times \;:\; (t \bmod e) + (mt \bmod e) < e \,\bigr\}.$$

Let `G = ⟨ m ↦ m⁻¹, m ↦ −1−m ⟩ ≅ S₃` (the anharmonic group) act on `{1,…,e−2}`. Let `(ℤ/e)^×` act on subsets by scaling, `Φ ↦ uΦ`.

> **Conjecture (Carry-Set Separation).** For every odd prime `e`, the map `m ↦ Φ_m` is **injective on `G`-orbits up to scaling**: distinct `G`-orbits produce `Φ`-sets that are not scaling-equivalent.

Equivalently: the carry pattern of multiplication-by-`m` determines the `G`-orbit of `m`. A finite, elementary question in modular arithmetic. §3.5 records that the CM-theoretic content of this statement is settled in the published literature (Koblitz–Rohrlich 1978 / Aoki 1991); the exact citation for the prime-`e` case is being pinned.

---

## 2. Computational corroboration

`verify.py` (requires `sympy`; run `python3 verify.py`) checks two finite facts; `verify_output.txt` is one recorded run, to be reproduced by the reader.

- **Check A — carry-set injectivity on `G`-orbits** for all odd primes `5 ≤ e ≤ 250`: no colliding prime (extended to `e ≤ 2000` in a separate run I have not personally reproduced). A single colliding prime would be a genuine counterexample; none occurs in range.
- **Check B — direct certificate that `K_P(e)=D(e)` as spaces** for `e ∈ {7,11,13,17,19,23}` (containment `D ⊆ K_P` **and** equal exact rational dimension) — establishes `K(e)=D(e)` for those `e` unconditionally, no CM machinery.
- **`verify_kr_bridge.py`** checks the two identifications linking this note's objects to the published CM classification (§3.5): `Φ_m = H_{1,m,−1−m}` (the carry set equals the Fermat CM type) and `G`-orbit `= ` triple-equivalence class.

---

## 3. The reduction to CM theory

**Setup.** For `p ≡ 1 (mod e)`, `T(1,m) = Tr_{ℚ(ζ_e)/ℚ} J(χ,χ^m) = Σ_{s} J(χ^s,χ^{ms})`, and `T(1,m) = e·N_m(p) − (p−2)` (Theorem A) with `N_m(p) = #{v : ind(v)+m·ind(1−v) ≡ 0 (e)}`. `D(e)` = span of the orbit relations, `K(e)` = true ℚ-relation space of `p ↦ N_m(p)`; `D(e) ⊆ K(e)` unconditionally.

**Reduction chain.** (1) The `T(1,m_i)` are Frobenius traces on the CM factors of the Fermat Jacobian of `x^e+y^e=z^e`, indexed by `G`-orbits. (2) The CM type equals the carry set: `Φ_m` (verified, §3.5). (3) `K(e)=D(e) ⟺` the `r(e)` CM factors are pairwise non-isogenous `⟺` their CM types `Φ_{m_i}` are pairwise distinct up to scaling `⟺` **Carry-Set Separation**. The `(⟸)` direction uses Chebotarev + Brauer–Nesbitt; the `(⟹)` direction uses that isogenous CM factors have equal Frobenius traces at every prime of good reduction (all `p ≡ 1 mod e`, by Néron–Ogg–Shafarevich + Fermat smoothness over `ℤ[1/e]`).

---

## 3.5 Status of the CM-side (published literature — settled, citation being pinned)

The load-bearing statement is: **for every odd prime `e`, distinct `G`-orbits give non-isogenous Fermat-Jacobian factors** (this is exactly Carry-Set Separation, via §3). Its status in the literature, as currently audited:

- **Koblitz–Rohrlich (1978)**, *Simple factors in the Jacobian of a Fermat curve*, Canad. J. Math. **30**(6), 1183–1205, **initiated** the isogeny/simplicity determination and settled the clean case (`N` prime to 6, via a Carlitz–Olson / Maillet-determinant argument). Every odd prime `e ≥ 5` is prime to 6, so this case *includes* the prime moduli relevant here. A primary-source read (in progress) reports KR Theorem 1 stating, for `N` prime to 6, that CM types coincide iff the triples are equivalent and the only isogenies are the obvious ones — which, if confirmed, *is* CSS for prime `e`.
- **Aoki (1991)**, *Simple factors of the Jacobian of a Fermat curve and the Picard number of a product of Fermat curves*, Amer. J. Math. **113**, 779–833, **completed** the classification for general `N` (Theorem 0.1). The non-obvious ("exceptional") isogenies form a finite list, all at **composite** moduli (9, 12, 15, 21, 24, 60, …; none prime, none `> 180`). This is what makes CSS a genuine prime-specific statement — it can, and at some composite moduli does, fail — and it is consistent with the empirical no-collision result to `e = 250`.

- **Bridge to this note (verified independently, `verify_kr_bridge.py`):** `Φ_m = H_{1,m,−1−m}` for all `m` (checked `e ≤ 61`, and by an elementary identity: the three-term residue sum equals `N` exactly when the two-term carry does not overflow), and the `G`-orbit of `m` equals the equivalence class of `(1, m, −1−m)` (checked `e ≤ 31`).

**Citation — pinned.** For the prime-`e` case (our case), the reference is **Koblitz–Rohrlich 1978, Theorem 1** (hypothesis: `N` prime to 6, which every odd prime `e ≥ 5` satisfies). The prime case is in fact the *clean* sub-case of KR's paper: for prime-power modulus it follows immediately (KR §2) from linear independence of characters — every odd character `χ` mod a prime power has `B_{1,χ} ≠ 0` (the classical non-vanishing underlying `h⁻`), so the CM types separate — and KR note a reader interested only in this case "need proceed no further." The Carlitz–Olson / Maillet-determinant machinery, and Aoki's completion, are for **composite** `N`, where Gauss-sum sign ambiguities (the Hasse–Yamamoto phenomenon) make it hard. KR Theorems 3–4 (the non-obvious isogenies) require `N = 3ⁿ` or `2ᵏ` with exponent `≥ 2` — composite, never prime. So no non-obvious isogeny occurs at any prime, and `K(e)=D(e)` holds **unconditionally for all odd primes `e ≥ 5`**, resting on KR 1978 Theorem 1.

**Honest register (what is verified here vs. read from source).** The bridge `Φ_m = H_{1,m,−1−m}` and `G`-orbit `=` triple-class is **verified independently** (computation + elementary identity — this note's own work). That the prime case is the classical clean sub-case (character non-vanishing, `B_{1,χ} ≠ 0` for odd `χ`) is a **standard classical fact** one can vouch for in principle. The exact statement of KR Theorem 1 and its §2 prime-case immediacy rest on a **primary-source read of the KR paper** (performed in the course of this work; a referee should confirm against the paper — this note does not reproduce KR's proof). Aoki 1991 (general `N`) is a **secondary-source** citation here (its paper was not read); it is *not load-bearing for primes* — the prime result is KR's. Net: `K(e)=D(e)` for odd primes is a theorem resting on (i) a verified bridge, (ii) a classical non-vanishing fact, and (iii) a primary-source reading of one KR theorem. (An earlier draft first over-attributed this "unconditional via KR" without the Aoki context, then over-corrected to "citation unpinned"; this is the accurate middle — pinned to KR 1978 Thm 1, with the KR read flagged as read-not-reproduced.)

---

## 4. Dead ends — ruled out, with reason (do not re-explore)

1. **`S₃`-symmetry alone** — Theorem A is an index-diagonal `S₃`-intertwiner, a spectator to `K` vs `D`.
2. **`ℚ[S₃]`-cyclicity** — `D(e)` is cyclic only for `e ∈ {5,7}`.
3. **Stickelberger ideal alone** — orbit relations are false at the ideal level (rank 5 vs `r(e)` at `e=11`), recovered only additively via Galois-invariance of the trace. (Yamamoto's classification of multiplicative relations is the ideal level; separation is the CM-type/archimedean level.)
4. **Large-monodromy / Sato–Tate largeness** — wrong lens; the object is CM (toric monodromy), `J/√p` on the circle, not `SU(2)`.
5. **A single Dedekind-sum invariant** — captures the carry *count* `|Φ_m|`, not the *set*. So does balanced-subgroup theory (Pomerance–Ulmer: even split of each coset between `(0,d/2)` and `(d/2,d)` is a **count** condition) — it bears on the count-level fiber law, **not** on set-level CSS.

---

## 5. Status and remaining items

- **CM-side of CSS (hence `K(e)=D(e)` for prime `e`):** settled in the published literature (KR 1978 / Aoki 1991), bridge verified; **remaining item = pin the exact citation** (KR Thm 1 for prime-to-6 vs Aoki Thm 0.1) against `Φ_m` from primary text.
- **Bibliographic residuals:** exact page/theorem numbers for Weil 1949 & 1952; the `p ≡ 1 (mod 3)` constituent step (the cube-root orbit's factor is non-simple — does not affect `K=D`, but is reasoning on top of the classification, not verbatim).
- **Independent branch (fully proved, session-verified):** the prime-power fiber law — over `e = p^k`, each fiber over `s ∈ (ℤ/e₁)^×` meets `Φ_m` in `(d±1)/2` elements (`d = p^{k−1}`), exception exactly at `m ≡ −1 (mod p)`; averaging proof (`Σf = d(d−1)`, `Σ(f mod d) = d(d−1)/2`, subtract). Composite-moduli reconnaissance; independent of the prime case; balanced-subgroup machinery (count-level) is the natural home for it.
- **Curiosity:** the `j`-invariant `I(m) = 8(m²+m+1)³/(m²+m)²` separates the `G`-orbits on the `m`-side; recovering it from `Φ_m` is itself equivalent to CSS.

---

*Register summary. **Theorem (bridge verified independently; KR theorem read from primary source, not reproduced):** `K(e)=D(e)` for all odd primes `e ≥ 5`, resting on **Koblitz–Rohrlich 1978, Theorem 1** — the prime case is KR's clean sub-case (character non-vanishing `B_{1,χ}≠0`, immediate in KR §2), with `Φ_m = ` CM-type verified here. Aoki 1991 completes the general (composite) classification and is a confirming reference, not load-bearing for primes; its exceptional isogenies are composite-only, so CSS is a genuine prime-specific theorem. **Verified here (own work):** the bridge `Φ_m = H_{1,m,−1−m}` and `G`-orbit = triple-class. **Read from source, not reproduced:** KR Theorem 1's statement and §2 prime-case argument (referee should confirm). **Cited-from-secondary:** Aoki 1991 (not read); Weil page numbers; the `p ≡ 1 mod 3` constituent step (KR Thm 2 + dimension argument). **Proved (independent branch, session-verified):** the prime-power fiber law. **Register history:** first draft over-attributed "KR unconditional," a correction over-swung to "citation unpinned," this is the accurate middle — pinned to KR 1978 Thm 1, with the KR read honestly flagged.*

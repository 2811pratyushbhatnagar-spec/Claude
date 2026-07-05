# The character lemma — an OCR-free proof of the CM-side

*This supersedes the "proof via Aoki Theorem 0.3" route. That route depended on transcribing Aoki's
nine-family classification from a garbled OCR (load-bearing, unverified). The character lemma below
replaces it: it proves the same conclusion directly from the T′ condition, using only classical
character theory, with no appeal to the nine-family list. The only remaining cited-not-read dependency
is Aoki's Proposition 1.4 (the isogeny criterion), which is more basic and whose form is corroborated.*

---

## Theorem (CM-side of Carry-Set Separation, uniform in prime e)

For every odd prime $e \ge 5$, distinct anharmonic $G$-orbits give **pairwise non-isogenous**
Fermat–Jacobian factors. Equivalently: $G$-orbit $=$ isogeny class; no cross-orbit isogenies.
Consequently (with Theorem A + Weil + Chebotarev + Brauer–Nesbitt) $K(e)=D(e)$.

## The chain

1. **(Aoki, Prop. 1.4 — CITED, form corroborated, exact statement not read here.)**
   $A_{[\alpha]} \sim A_{[\alpha']} \iff \alpha*(-\alpha') \in T'_e$, where for a 6-tuple $v$ of nonzero
   residues, $v \in T'_e \iff \sum_i \langle t\,v_i/e\rangle = 3$ for every unit $t$, and
   $\langle a/e\rangle = (a \bmod e)/e$. ("for some representatives" — but $T'$-membership is
   scale-invariant, see the remark, so this does not affect what follows.)

2. **(Character Lemma — PROVED below, session-verified.)** For prime $e$, every $v \in T'_e$ is
   **negation-symmetric**: the multiset $\{v_i\}$ equals $\{-v_i\}$.

3. **(Negation-symmetry sublemma — ELEMENTARY.)** If $v = \alpha*(-\alpha') = (a,b,c,-a',-b',-c')$
   with $a+b+c\equiv 0 \equiv a'+b'+c'$, all entries nonzero, and $v=-v$, then $\{a',b',c'\}=\{a,b,c\}$
   (up to permutation): $\alpha' \sim \alpha$, the **same** orbit.

4. **(Slice $=$ index set — ELEMENTARY.)** At prime $e$, every admissible triple $(a,b,c)$ with
   $a+b+c\equiv 0$ is scaling-equivalent to $(1,\lambda,-1-\lambda)$ (scale by $a^{-1}$, a unit); and
   scaling+permutation on $(1,\lambda,-1-\lambda)$ generates exactly the anharmonic $G$-action.

**Chain:** $\alpha*(-\alpha') \in T'_e \Rightarrow$ (2) negation-symmetric $\Rightarrow$ (3) same orbit.
Contrapositive: distinct $G$-orbits $\Rightarrow \alpha*(-\alpha') \notin T'_e \Rightarrow$ (1)
non-isogenous. $\blacksquare$ (modulo the Prop. 1.4 citation)

## Proof of the Character Lemma

Write the sawtooth $((x)) = \langle x\rangle - \tfrac12$ (for $x\notin\mathbb Z$), an odd function.
Since each $v_i \not\equiv 0$ and $t$ is a unit, $tv_i \not\equiv 0$, so
$\langle t v_i/e\rangle = ((tv_i/e)) + \tfrac12$. Hence

$$\sum_i \langle t v_i/e\rangle = 3 \quad\Longleftrightarrow\quad \sum_i (( t v_i/e )) = 0 \ \ \forall\, t\in(\mathbb Z/e)^\times.$$

Expand $a \mapsto ((a/e))$, an odd function on $(\mathbb Z/e)^\times$, in Dirichlet characters mod $e$:

$$(( a/e )) = \sum_{\chi\ \text{odd}} b_\chi\, \chi(a), \qquad
  b_\chi = \tfrac{1}{e-1}\sum_a ((a/e))\,\overline{\chi}(a) \ \propto\ B_{1,\overline\chi}.$$

Only odd $\chi$ appear (the function is odd), and **$b_\chi \neq 0$ for every odd $\chi$** — this is the
classical non-vanishing $B_{1,\chi}\neq 0$ for odd $\chi$ (for prime $e$ every nontrivial character is
primitive, so it applies to all odd $\chi$). *[Verified computationally: $\min_\chi |b_\chi| \in
[0.57, 1.08]$ for all primes $e \le 47$.]*

Then for all units $t$:
$$0 = \sum_i (( t v_i/e )) = \sum_{\chi\ \text{odd}} b_\chi\, \chi(t)\Big(\sum_i \chi(v_i)\Big).$$
The characters $\{\chi(t)\}$ are linearly independent as functions of $t$, so each coefficient vanishes:
$b_\chi \sum_i \chi(v_i) = 0$. Since $b_\chi \neq 0$, we get $\sum_i \chi(v_i) = 0$ for **every odd** $\chi$.

Let $n_a$ be the multiplicity of $a$ in $v$. Then $\sum_a n_a \chi(a) = 0$ for all odd $\chi$. Writing
$n_a = n_a^{+} + n_a^{-}$ (even/odd parts under $a\mapsto -a$), the even part is annihilated by odd $\chi$,
so $\sum_a n_a^{-}(a)\chi(a) = 0$ for all odd $\chi$. But $n^{-}$ is an odd function and the odd
characters form a basis of the odd functions on $(\mathbb Z/e)^\times$, so $n^{-} \equiv 0$: i.e.
$n_a = n_{-a}$ for all $a$. That is exactly $v = -v$. $\blacksquare$

## Remark (scale-invariance)

$T'$-membership is invariant under scaling $v \mapsto uv$ by a unit (as $t$ ranges over units so does
$tu$), and so is negation-symmetry. Hence Prop. 1.4's "for some representatives" quantifier is
immaterial to the lemma: it applies to the whole $T'$ condition directly.

## Corrected composite-$m$ mechanism (a misdiagnosis, fixed)

An earlier draft claimed composite $m$ admits cross-orbit isogenies because "an imprimitive odd $\chi$
has $B_{1,\chi}=0$, so non-symmetric tuples are allowed." **That is wrong.** Restricted to **unit**
multisets, composite $m$ (checked $m=16,25,35$) admits **no** non-symmetric $T'$-tuple — it behaves like
a prime. The real mechanism: the character lemma is a statement about *unit* multisets; at prime $e$
every nonzero residue is a unit, so it covers every factor-triple, but at composite $m$ the factor-triples
may contain **non-unit** entries (e.g. $m/2$), which the lemma does not cover — and that is exactly where
Aoki's exceptional cross-orbit isogenies live. Simpler and correct.

## Dependency ledger

- **Proved here / session-verified:** the Character Lemma (both load-bearing facts run in-session — odd-character non-vanishing to $e\le47$; exhaustive $T'\Rightarrow$ neg-sym at primes $5$–$43$); the scale-invariance remark; the corrected composite mechanism.
- **Elementary:** slice $=$ index set; negation-symmetry $\Rightarrow$ same orbit.
- **Classical (textbook):** $B_{1,\chi}\neq 0$ for odd $\chi$; character orthogonality / linear independence; Chebotarev; Brauer–Nesbitt; Weil's Jacobi-sum $=$ Frobenius-trace identification; Theorem A (proved earlier).
- **Aoki 1991, Proposition 1.4** (the T′ isogeny criterion): verbatim statement is **verbatim-inaccessible** (Amer. J. Math. paywalled; the secondary sources that cite it — Ulmer math/0609716 §3.4, and two Mumford–Tate papers — do not reproduce it). Its *form* is corroborated (Rohrlich's period computation; the $H_{r,s,t}$ fractional-part condition, read verbatim in kr.txt) and validated against Koblitz–Rohrlich's composite pairs. **But — key point — Prop. 1.4 is NOT load-bearing for the prime case** (see Status).

**Status — corrected.** For the prime case the CM-side does **not** depend on Aoki Prop. 1.4. It has two supports: **(1)** Koblitz–Rohrlich 1978, **Theorem 1** — for $N$ prime to 6 (⊇ every odd prime $e\ge5$), the CM types coincide iff the triples are equivalent, and the only isogenies are the obvious ones; read verbatim from the primary source (kr.txt). **(2)** The **character lemma above** (proved + session-verified, OCR-free), which independently proves the CM-type–coincidence structure at primes via character non-vanishing — a *different* mechanism than KR's Carlitz–Olson argument — and, with classical Shimura–Taniyama CM theory (distinct CM type $\Rightarrow$ non-isogenous), gives the same conclusion. So $K(e)=D(e)$ for all odd primes $e\ge5$ rests on **KR 1978 Thm 1 (verbatim-read) + this character lemma (proved here)**; the OCR dependency on Aoki Theorem 0.3 is eliminated, and Aoki Prop. 1.4 — though verbatim-inaccessible — is not needed for primes. The one residual debt is that the KR Thm 1 read is relayed (kr.txt, not independently reachable), corroborated by the independent character lemma; a referee should confirm KR Thm 1 against the paper.

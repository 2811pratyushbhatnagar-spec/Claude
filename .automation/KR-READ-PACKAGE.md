# KR Theorem 1 — your first-party read, made concrete   [non-canon · prep only]

*Goal: close the one open verification on the K(e)=D(e) result. Everything is already proved or
independently verified EXCEPT one thing: the exact statement of a 1978 theorem was read for us by a relayed
file (kr.txt), not by a human with the paper open. Your read closes it. This is a **statement-level** read —
you do NOT need to understand the proofs. Realistic effort: 30–60 minutes with the tutor prompt below.*

---

## 1. What this is about, in plain terms

Your MSF/carry-set work produced a family of numbers `N_m(p)` (counting solutions of a congruence) and a
question: **are the known linear relations among them (the "orbit relations", span = `D(e)`) ALL the
relations there are (`K(e)`)?** The claim `K(e) = D(e)` — "no hidden coincidences" — was reduced, through a
verified bridge, to a statement about **Fermat curves**: the pieces (CM factors) of the Jacobian of
`x^e + y^e = z^e` are pairwise non-isogenous — no two pieces are secretly the same. That statement is
**Carry-Set Separation (CSS)**, and for prime `e` it is exactly what a 1978 paper by **Koblitz and
Rohrlich** proved. Our note pinned everything to their **Theorem 1**.

**What is already solid (independently verified, ours):** the bridge `Φ_m = H_{1,m,−1−m}` (CM type = carry
set) — computed and proved this side; the character lemma; the space-certificate for small e.
**The single soft spot:** what KR's Theorem 1 *actually says on the printed page* was relayed, not
first-party. If the relayed statement is right, `K(e)=D(e)` holds unconditionally for all odd primes `e≥5`.
Your eyes on two passages close the loop.

## 2. The exact object

> **N. Koblitz and D. Rohrlich, "Simple factors in the Jacobian of a Fermat curve,"**
> *Canadian Journal of Mathematics* **30** (1978), no. 6, pp. 1183–1205.

Where to get it (open access): the Canadian Journal of Mathematics back archive is free on **Cambridge
Core** — search: `Koblitz Rohrlich "Simple factors in the Jacobian of a Fermat curve"` — or via
`cms.math.ca`. (If you hit a wall, the paper is also findable via Google Scholar; tell me and I'll help.)

## 3. Exactly what to confirm — two checks, nothing more

**CHECK 1 — the statement of Theorem 1** (early in the paper, §1 or §2).
What we relied on: *for N prime to 6, two CM factors of the Fermat Jacobian have coinciding CM types if and
only if their defining triples are equivalent — equivalently, the only isogenies among the factors are the
"obvious" ones.* Every odd prime `e ≥ 5` is prime to 6, so this hypothesis covers our whole case.
→ **Your task:** find Theorem 1. Transcribe it verbatim into the form below. Answer: does the printed
hypothesis say "N prime to 6" (or equivalent)? Does the printed conclusion match the italicized statement
above in substance? (Notation may differ — triples may be written `(a,b,c)` with `a+b+c ≡ 0 mod N`; "CM
type" may be phrased via sets `H_{a,b,c}`; that's fine. What matters: *distinct triples-up-to-equivalence ⟹
non-isogenous / distinct CM types*.)

**CHECK 2 — the prime case is the "clean" case** (§2).
What we relied on: for prime (or prime-power) N, the separation follows quickly from a classical
non-vanishing fact (`B_{1,χ} ≠ 0` for odd characters χ — equivalently, linear independence of characters),
and KR indicate a reader interested only in this case can stop there — the heavy machinery in the rest of
the paper is for *composite* N only.
→ **Your task:** in §2, confirm (a) there is a short argument settling the prime(-power) case, and (b) some
remark to the effect that the composite case is where the real work is / the reader interested in the
prime-power case "need proceed no further" (any equivalent phrasing counts; transcribe whatever sentence
plays that role).

**You are NOT confirming:** the proof's correctness (refereed 48 years ago), the Jacobian machinery, Aoki
1991, or anything about composite N. Statement-level only.

## 4. Fill-in confirmation form (becomes the Ledger E row when done)

```
KR 1978 read — first-party confirmation (date: ______ )
CHECK 1  Theorem 1 verbatim: "________________________________________________"
         Hypothesis covers all odd primes e≥5 (N prime to 6)?   YES / NO / UNCLEAR
         Conclusion matches "distinct triples ⟹ non-isogenous"?  YES / NO / UNCLEAR
CHECK 2  Prime(-power) case settled quickly in §2?               YES / NO / UNCLEAR
         "Need proceed no further"-type remark (verbatim): "____________________"
Verdict: the relayed statement was  FAITHFUL / DIFFERS (how: _________________ )
```

Any UNCLEAR is fine — bring it back and we resolve it together. A "DIFFERS" would be important: it would
re-open the K(e)=D(e) row, which is exactly why this read matters.

## 5. Paste-ready prompt for a fresh ChatGPT instance (your reading tutor)

Copy everything between the lines into a NEW ChatGPT chat, then read the paper alongside it:

---------------------------------------------------------------
You are my reading tutor for exactly one task. I am not a professional number theorist; explain at the
level of a smart, patient undergraduate course, defining every symbol the moment it appears.

The paper: N. Koblitz and D. Rohrlich, "Simple factors in the Jacobian of a Fermat curve," Canadian
Journal of Mathematics 30 (1978), no. 6, 1183–1205.

My only goal — a statement-level read, not proofs:
(1) find Theorem 1, understand what its hypothesis "N prime to 6" and its conclusion mean, well enough to
    transcribe it and judge whether it says: for such N, the CM factors of the Fermat Jacobian J(N) have
    coinciding CM types only when their defining triples (a,b,c), a+b+c ≡ 0 (mod N), are equivalent (under
    the standard scaling/permutation action) — i.e., the only isogenies among factors are the obvious ones.
(2) in §2, confirm the prime-power case is settled early and cheaply (via non-vanishing of generalized
    Bernoulli numbers B_{1,χ} ≠ 0 for odd χ / linear independence of characters), and locate any remark
    that a reader who only needs the prime-power case can stop there.

Please: (a) give me a 15-minute background briefing: Fermat curve, Jacobian, what a CM abelian variety and
a CM type are (intuition over rigor), what "isogenous" means, what the triples (a,b,c) index, and why
"distinct CM types ⟹ non-isogenous" is the useful direction; (b) then walk me through locating and reading
Theorem 1 and the relevant §2 passage, translating each sentence; (c) quiz me briefly at the end so I can
honestly certify I confirmed the two checks with my own eyes. Do not summarize the theorem FOR me from your
training data — your job is to help ME read the printed page; flag clearly anything where your memory and
the page might differ, and defer to the page.
---------------------------------------------------------------

*Prepared 2026-07-05. Non-canon. When your form is filled, I turn it into the Ledger E append and the
priorities row closes.*

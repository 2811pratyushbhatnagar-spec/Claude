# Priority 5 — information causality: the point of contact with compression (ChatGPT cross-check)   [non-canon · candidate]

*Brought the CHSH tiering + the supply-vs-import question on information causality to ChatGPT. This records the verdict:
a genuine **point of contact** between the framework's compression core and IC, a register-careful refined research
question, and the named computable check. Tier-3; canon read-only; nothing promoted.*

## CHSH tiering — confirmed standard
Local classical `≤ 2`; complex quantum `≤ 2√2` (Tsirelson); no-signalling / PR boxes `≤ 4`; and `2 < 2√2 < 4`.
Placement correct: quantum is the **Tsirelson-bounded** sub-theory — entanglement, but forbidding PR boxes.

## The point of contact (the genuine, honest lead)
Compression/minimal-realization and information causality are **not** the same theorem, but ChatGPT places both in a
single **family of principles**:

> **"No operational task should outperform the information actually made available by the allowed interface."**

- **Compression** asks: *what is the smallest internal representation preserving specified observations?* (single-system, internal.)
- **Information causality** asks: *a receiver cannot learn more about a sender's database than the number of transmitted bits.* (multi-party, communication.)

Same family (interface-limited information), different theorems. **Whether the framework can generate an IC-type
constraint depends on it acquiring what it currently lacks — composition, multiple agents, message channels,
conditional information — none of which exist in a single `(S,F,O)`.**

## The refined research question (register-careful — ChatGPT's phrasing)
> **Can a compression-and-capacity framework naturally generate an Information-Causality-type constraint once
> composition and communication are added?**

Precise, bounded, genuinely open. It avoids claiming compression *already contains* IC, while naming the plausible
point of contact. Honest status: **open, no evidence yet** — but this is the framework's *best* candidate contribution,
precisely because its strongest supply-claim (compression) is itself a capacity/information principle.

## The computable check (named)
The **Information-Causality random-access-code game** (Pawłowski et al. 2009). Alice holds an `N`-bit string; Bob picks
one index `b`; Alice sends `m` classical bits; Bob guesses `a_b`. Compute
`I = Σ_{k=1}^N I(a_k : β | b=k)`.  **IC requires `I ≤ m`.**
- classical resources: **satisfy** (`I ≤ m`);
- quantum resources: **satisfy** (`I ≤ m`);
- **PR box: violates** — for `N=2, m=1`, the van Dam protocol gives a *perfect* random-access code ⇒ `I = 2 > 1 = m`.

A single scalar says whether a theory crosses the IC boundary.

**Computed (`ic_rac_game.py`, N=2, m=1):** `I(classical, best) = 1.0000` (saturates the bound), `I(quantum, optimal) =
0.7982` (`p_q = ½(1+1/√2) = 0.8536`), `I(PR box, van Dam) = 2.0000`. So `I ≤ m = 1` **holds** for classical (tight) and
quantum, and **breaks** for the PR box (verified exhaustively: the van Dam protocol recovers `a_b` perfectly for all 8
inputs, `p = 1` for both `b`). The single scalar cleanly separates quantum from super-quantum.

## Caution (recorded)
Information causality is **one of several** principles that recover — or *nearly* recover — the quantum correlation
boundary under additional assumptions. It is a powerful discriminator against PR boxes, but **not** generally regarded
as the unique or final explanation of Tsirelson's bound. So even deriving IC would not, by itself, reconstruct quantum
theory.

## Register / holds
Cross-check recorded · CHSH tiering confirmed standard · IC placed as the framework's **best candidate contribution**
(the compression↔capacity family), phrased as an open question, not a result · computable check named (IC RAC game,
`I ≤ m`) · **no current evidence** the framework supplies IC · non-canon · Tier-3 · canon read-only. Provenance:
2026-07-10; ChatGPT https://chatgpt.com/c/6a4ffe2d-aa78-83ee-b6b1-de0d8defb14a; builds on `PRIORITY-5-CHSH-TIERS-2026-07-10.md`.

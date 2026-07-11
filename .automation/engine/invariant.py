"""Structural invariant + stability math for the stability-convergence engine.

Model-free core: an agent's answer is reduced to a set of claim tokens. The
invariant is the set of claims asserted by at least N *independent* paths.
Independence is counted over (model, evidence_path) pairs -- so two agents on
the SAME model AND SAME path count as one (the echo pathology, in code)."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Optional

def _neg(c: str) -> str:
    return c[4:] if c.startswith("not ") else "not " + c

@dataclass(frozen=True)
class Representation:
    agent_id: str
    model: str            # "claude", "chatgpt" -> the model-level independence axis
    evidence_path: str    # "first-principles", "literature", "counterexample", ...
    role: str             # Construction | Refutation | Integration | Diversity
    claims: frozenset     # claim tokens; "not X" is the negation of "X"

    @property
    def path(self):
        return (self.model, self.evidence_path)

@dataclass
class Invariant:
    claims: frozenset
    representation_specific: frozenset
    disagreements: frozenset
    independent_paths: int

def independent_paths(reps: Iterable[Representation]):
    return {r.path for r in reps}

def extract_invariant(reps, n_independent: int) -> Invariant:
    reps = list(reps)
    support = {}                         # claim -> set of distinct paths asserting it
    for r in reps:
        for c in r.claims:
            support.setdefault(c, set()).add(r.path)
    invariant, specific = set(), set()
    for c, paths in support.items():
        (invariant if len(paths) >= n_independent else specific).add(c)
    disagreements = {c for c in support if _neg(c) in support}
    invariant -= disagreements           # a contested claim is never in the invariant
    specific  -= disagreements
    return Invariant(frozenset(invariant), frozenset(specific),
                     frozenset(disagreements), len(independent_paths(reps)))

def stability(prev: Optional[Invariant], new: Invariant) -> float:
    """Jaccard distance between successive invariant claim-sets, in [0,1].
    1.0 = no prior / total change; 0.0 = identical."""
    if prev is None:
        return 1.0
    a, b = prev.claims, new.claims
    if not a and not b:
        return 0.0
    return len(a ^ b) / len(a | b)

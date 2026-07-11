"""Priority-1, pole N3: when does the minimal observation-preserving quotient FAIL
to exist / be unique?  Cleanest computable reading = 'best (most precise sound)
abstraction of X in a family F of allowed abstractions'.
Result (verified): the best abstraction exists & is unique  <=>  F is meet-closed
(a Moore family). If F is not meet-closed, some X has several incomparable minimal
sound over-approximations = NO best abstraction (N3 non-existence). Reproduce:
  python3 N3_best_abstraction.py"""

def minimal_sound(F, X):
    sound = [A for A in F if X <= A]                       # sound over-approximations
    minimal = [A for A in sound if not any(B < A for B in sound)]
    return sound, minimal

def meet_closed(F):
    Fs = set(F)
    for A in F:
        for B in F:
            if (A & B) not in Fs:
                return False, (A, B, A & B)
    return True, None

def show(name, F, X):
    fs = lambda s: "{" + ",".join(sorted(s)) + "}" if s else "{}"
    mc, wit = meet_closed(F)
    _, minimal = minimal_sound(F, X)
    print(f"=== {name} ===")
    print("  F            :", [fs(A) for A in F])
    print("  meet-closed  :", mc, ("" if mc else f"(witness {fs(wit[0])} & {fs(wit[1])} = {fs(wit[2])} not in F)"))
    print(f"  target X     : {fs(X)}")
    print("  minimal sound over-approx:", [fs(A) for A in minimal])
    if len(minimal) == 1:
        print("  => BEST abstraction EXISTS & UNIQUE:", fs(minimal[0]), " (quotient exists)")
    else:
        print(f"  => NO best abstraction: {len(minimal)} incomparable minimal sound sets  ==>  N3 (non-existence)")
    print()

if __name__ == "__main__":
    a, b, c = 'a', 'b', 'c'
    S = frozenset
    F1 = [S({a, b}), S({a, c}), S({a, b, c})]              # NOT meet-closed ({a,b}&{a,c}={a} not in F1)
    show("F1 (not meet-closed) -> N3", F1, S({a}))
    F2 = F1 + [S({a})]                                     # Moore completion -> meet-closed
    show("F2 = F1 + meet {a} (Moore family) -> exists", F2, S({a}))

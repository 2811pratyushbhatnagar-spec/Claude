#!/usr/bin/env python3
"""O-Conjecture v0.2 — Tier-1 verification, exact integer arithmetic in Z[omega].

Elements of Z[omega] are pairs (a, b) meaning a + b*omega, with omega^2 = -1 - omega.
No floats anywhere: every check is an identity in the ring or an exhaustive
finite enumeration. Exit code 0 iff all checks pass.
"""

# ---------- exact ring Z[omega] ----------
def add(x, y): return (x[0] + y[0], x[1] + y[1])
def neg(x):    return (-x[0], -x[1])
def sub(x, y): return add(x, neg(y))
def mul(x, y):
    a, b = x; c, d = y
    # (a + b w)(c + d w) = ac + (ad+bc) w + bd w^2 ;  w^2 = -1 - w
    return (a * c - b * d, a * d + b * c - b * d)
def conj(x):
    a, b = x
    # conj(w) = w^2 = -1 - w
    return (a - b, -b)
def norm(x):
    a, b = x
    return a * a - a * b + b * b   # N(a+bw) = a^2 - ab + b^2

ONE   = (1, 0)
OMEGA = (0, 1)
LAM   = sub(OMEGA, ONE)        # lambda = omega - 1   (non-return defect, h=1)
U     = add(ONE, (0, 2))       # u = 1 + 2*omega      (orientability cycle element)

failures = []
def check(name, ok):
    print(f"  {name:46s} {'PASS' if ok else 'FAIL'}")
    if not ok:
        failures.append(name)

print("=" * 72)
print("TIER 1 — arithmetic identities in Z[omega] (exact)")

# u is a unit-associate of the defect: u = -omega * lambda
check("u == -omega * lambda", U == neg(mul(OMEGA, LAM)))

# lambda^2 = -3 omega  =>  (lambda)^2 = (3)
check("lambda^2 == -3*omega", mul(LAM, LAM) == (0, -3))

# u^2 = -3 = disc Q(omega)
check("u^2 == -3", mul(U, U) == (-3, 0))

# N(lambda) = N(u) = 3 : both generate the ramified prime p over 3
check("N(lambda) == 3", norm(LAM) == 3)
check("N(u) == 3", norm(U) == 3)

# conj(lambda) = lambda * (omega + 1): the prime is ramified (p-bar = p)
check("conj(lambda) == lambda*(omega+1)",
      conj(LAM) == mul(LAM, add(OMEGA, ONE)))

# 3 = lambda^2 * (-omega)^-1 ... equivalently  lambda^2 * conj(omega)... check 3 in (lambda^2):
# 3 = -omega^2 * lambda^2  since  lambda^2 = -3 omega and omega^3 = 1
check("3 == -omega^2 * lambda^2",
      (3, 0) == neg(mul(mul(OMEGA, OMEGA), mul(LAM, LAM))))

# residue weights x_h = N(omega^h - 1): x_0 = 0, x_1 = x_2 = 3 = N(p)
pow_om = {0: ONE, 1: OMEGA, 2: mul(OMEGA, OMEGA)}
xs = [norm(sub(pow_om[h], ONE)) for h in (0, 1, 2)]
check("x_h = N(omega^h - 1) == [0, 3, 3]", xs == [0, 3, 3])

print("=" * 72)
print("TIER 1 — residue field Z[omega]/(lambda) ~ F_3 (exhaustive on a window)")

# The map r(a + b*omega) = (a + b) mod 3 is a ring hom with kernel (lambda):
# ring-hom property exhaustively on a window, kernel check both directions.
def r(x): return (x[0] + x[1]) % 3

W = range(-6, 7)
hom_ok = all(
    r(mul((a, b), (c, d))) == (r((a, b)) * r((c, d))) % 3
    and r(add((a, b), (c, d))) == (r((a, b)) + r((c, d))) % 3
    for a in W for b in W for c in W for d in W)
check("r(x)=(a+b) mod 3 is a ring hom onto F_3", hom_ok)

# kernel = (lambda): x in ker r  <=>  x = lambda * y for some y (window search)
def in_ideal_lambda(x):
    # x = lambda * y  =>  y = x * conj(lambda) / N(lambda) = x * conj(lambda) / 3
    p = mul(x, conj(LAM))
    return p[0] % 3 == 0 and p[1] % 3 == 0

ker_ok = all((r((a, b)) == 0) == in_ideal_lambda((a, b)) for a in W for b in W)
check("ker r == (lambda) on the window", ker_ok)

# omega == 1 mod lambda: faces fuse on the residue field (sigma = sigma-bar at p)
check("omega == 1 mod lambda", r(OMEGA) == r(ONE))
check("conj acts trivially on F_3",
      all(r(conj((a, b))) == r((a, b)) for a in W for b in W))

print("=" * 72)
print("TIER 1 — unit action: mu_6 / {+-1} ~ Z_3 (exhaustive)")

mu6 = [ONE, neg(ONE), OMEGA, neg(OMEGA), mul(OMEGA, OMEGA), neg(mul(OMEGA, OMEGA))]
check("mu_6 closed under multiplication",
      all(mul(x, y) in mu6 for x in mu6 for y in mu6))
check("all mu_6 elements have norm 1", all(norm(x) == 1 for x in mu6))
# quotient by {+-1}: classes {1,-1},{w,-w},{w^2,-w^2}; class of omega generates
cls = lambda x: frozenset({x, neg(x)})
classes = {cls(x) for x in mu6}
check("mu_6/{+-1} has exactly 3 classes", len(classes) == 3)
check("class(omega) has order 3",
      cls(mul(OMEGA, mul(OMEGA, OMEGA))) == cls(ONE) and cls(mul(OMEGA, OMEGA)) != cls(ONE))

print("=" * 72)
print("TIER 1 — intrinsic mode: shifted table is torsor transport (exhaustive)")

# x*y = x+y+1 mod 3 ; phi(x) = x+1 is an isomorphism onto (Z_3, +); identity e = 2
star = lambda x, y: (x + y + 1) % 3
phi  = lambda x: (x + 1) % 3
check("phi(x*y) == phi(x)+phi(y) for all x,y",
      all(phi(star(x, y)) == (phi(x) + phi(y)) % 3 for x in range(3) for y in range(3)))
check("identity of * is e = 2 (derived, not stipulated)",
      all(star(x, 2) == x and star(2, x) == x for x in range(3)))

print("=" * 72)
print("TIER 2 CANDIDATE LEMMA — two-face frame excludes Z[i] (exact)")

# Two faces (embedding set of size 2) => phi(n) = 2 => candidates Z[i], Z[omega]
# (Z[zeta_6] = Z[omega]).  Gaussian case: ramified prime (1+i) over 2, residue
# field F_2 => additive recurrence period 2, excluded by T^2(n) != n.
# Eisenstein case: residue field F_3 => period 3, the least surviving.
Ni = 1 * 1 + 1 * 1               # N(1+i) = a^2 + b^2 = 2
check("N(1+i) == 2  (Gaussian residue field F_2)", Ni == 2)
check("F_2 additive recurrence violates T^2(n) != n", (0 + 1 + 1) % 2 == 0)
check("F_3 additive recurrence satisfies T^2(n) != n and T^3(n) == n",
      (0 + 1 + 1) % 3 != 0 and (0 + 1 + 1 + 1) % 3 == 0)

print("=" * 72)
if failures:
    print(f"RESULT: {len(failures)} FAILURE(S): {failures}")
    raise SystemExit(1)
print("RESULT: ALL CHECKS PASS (exact integer arithmetic / exhaustive enumeration)")

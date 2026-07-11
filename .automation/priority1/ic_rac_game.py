"""Priority-5.5 (the named computable check): the Information-Causality random-access-code game.
Alice has 2 uniform bits (a0,a1); Bob picks b in {0,1}; Alice sends m=1 classical bit; Bob guesses a_b.
IC quantity  I = I(a0:beta | b=0) + I(a1:beta | b=1);  Information Causality requires  I <= m = 1.
Compute I for classical (best), quantum-optimal RAC, and a PR box (van Dam protocol) — watch the bound break
ONLY for the PR box. Requires numpy. Reproduce: python3 ic_rac_game.py"""
import itertools
import numpy as np

def H(p):
    return 0.0 if p <= 0 or p >= 1 else float(-p * np.log2(p) - (1 - p) * np.log2(1 - p))
def mi_uniform_bsc(p):        # I(X:Y): X a uniform bit, Y = X recovered with success prob p (binary symmetric channel)
    return 1.0 - H(p)

# --- PR box, van Dam protocol: exhaustively verify PERFECT recovery of a_b for every (a0,a1,b) ---
def van_dam(a0, a1, b, alpha=0):
    beta_box = alpha ^ ((a0 ^ a1) & b)   # PR box:  alpha XOR beta_box = x AND y,  with x=a0^a1, y=b
    msg = a0 ^ alpha                      # Alice's single transmitted bit
    return msg ^ beta_box                 # Bob's guess
succ = {0: [], 1: []}
for a0, a1, b in itertools.product([0, 1], repeat=3):
    target = a0 if b == 0 else a1
    succ[b].append(van_dam(a0, a1, b) == target)
p_pr0, p_pr1 = float(np.mean(succ[0])), float(np.mean(succ[1]))
I_pr = mi_uniform_bsc(p_pr0) + mi_uniform_bsc(p_pr1)

# --- classical best (send a0 exactly): b=0 perfect, b=1 carries no info about a1 ---
I_cl = mi_uniform_bsc(1.0) + mi_uniform_bsc(0.5)          # 1 + 0 = 1  (saturates m)

# --- quantum optimal 2->1 RAC: each bit recovered with p = 1/2 (1 + 1/sqrt2) ---
p_q = 0.5 * (1 + 1 / np.sqrt(2))
I_q = 2 * mi_uniform_bsc(p_q)

if __name__ == "__main__":
    m = 1
    print(f"PR box (van Dam): per-bit success  p(b=0)={p_pr0:.3f}, p(b=1)={p_pr1:.3f}   (perfect random-access code)")
    print(f"\n  I(classical, best)   = {I_cl:.4f}    <= m={m} ?  {I_cl <= m + 1e-9}    (saturates the bound)")
    print(f"  I(quantum, optimal)  = {I_q:.4f}    <= m={m} ?  {I_q <= m + 1e-9}    (p_q = {p_q:.4f})")
    print(f"  I(PR box, van Dam)   = {I_pr:.4f}    <= m={m} ?  {I_pr <= m + 1e-9}    <-- VIOLATES")
    print("\nPIN: Information Causality (I <= m) HOLDS for classical (=1, tight) and quantum (~0.80), and BREAKS for the")
    print("     PR box (I=2). A single scalar separates quantum from super-quantum: IC is a powerful discriminator")
    print("     against PR boxes (one candidate principle, NOT the unique/final explanation of Tsirelson). Whether an")
    print("     (S,F,O) compression/capacity framework SUPPLIES an IC-type bound once composition + communication are")
    print("     added is the open research question.")

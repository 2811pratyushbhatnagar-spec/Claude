"""Priority-5.5 (ChatGPT's calibrated target): the SQUARE BIT ('gbit') composite.
Add the convex structure — probability = [0,1] = nothing..everything — and compute the ONE number ChatGPT named:
the AFFINE DIMENSION of the composite state space, dim(Omega_AB), vs (dim Omega_A + 1)(dim Omega_B + 1) - 1.

Single gbit: two fiducial binary measurements X,Z; a normalized state = (P(X=0), P(Z=0)) in the unit SQUARE [0,1]^2
(affine dimension 2 — convex but NOT a simplex). GPT state vector v = (1, x, z); 4 pure states = the corners; K=3.

Computed:
 (1) dim(Omega_AB) = affine rank of the 16 product states = (2+1)(2+1)-1 = 8  =>  LOCAL TOMOGRAPHY HOLDS
     (the gbit composite adds dimension like classical & complex QM — unlike real QM's E7 failure 9<10).
 (2) a PR-box no-signalling state is NOT in the convex hull of product states (LP infeasible) => a genuine
     non-product EXTREME point exists = ENTANGLEMENT in the (max) tensor.
 => the gbit is a LOCALLY-TOMOGRAPHIC theory that nonetheless HAS entanglement, sitting between the classical
    simplex (no entanglement) and quantum. Confirms: local tomography is NOT classicality; it is the R-vs-C test (E7),
    reached only after adding the [0,1] convex structure (simplex first), then a non-Cartesian tensor.
Requires numpy, scipy.  Reproduce: python3 gbit_composite.py"""
import numpy as np
from scipy.optimize import linprog

corners = [(0, 0), (0, 1), (1, 0), (1, 1)]
def vec(x, z): return np.array([1.0, float(x), float(z)])
local_pure = [vec(x, z) for (x, z) in corners]
prod_states = [np.outer(vi, vj).flatten() for vi in local_pure for vj in local_pure]  # 16 x 9

def affine_rank(points):
    P = np.array(points)
    return int(np.linalg.matrix_rank(P - P[0], tol=1e-9))

if __name__ == "__main__":
    dA = affine_rank(local_pure); dB = dA
    dAB = affine_rank(prod_states)
    predicted = (dA + 1) * (dB + 1) - 1
    print(f"dim Omega_A = {dA}   (unit square — convex, NOT a simplex)")
    print(f"dim(Omega_AB) = affine rank of the 16 product states = {dAB}")
    print(f"(dim A + 1)(dim B + 1) - 1 = {predicted}   ->  local tomography {'HOLDS' if dAB == predicted else 'FAILS'}")

    # PR box: M[i,j] = <effect_i^A, effect_j^B> over fiducial effects {u, X=0, Z=0}. Marginals all 1/2;
    # correlations are those of the Popescu-Rohrlich box  P(ab|xy)=1/2 if a xor b = x and y.
    PR = np.array([[1.0, .5, .5],
                   [.5, .5, .5],
                   [.5, .5, 0.]]).flatten()
    A_eq = np.vstack([np.array(prod_states).T, np.ones(16)])      # 10 x 16
    b_eq = np.concatenate([PR, [1.0]])
    res = linprog(c=np.zeros(16), A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * 16, method='highs')
    sep = res.success
    print(f"\nPR-box a convex combination of product (separable) states?  {'YES -> separable' if sep else 'NO -> genuine ENTANGLEMENT (non-product extreme point)'}")

    print("\nPIN: adding [0,1] convex structure (nothing..everything) to the square bit, the composite is 8-dimensional")
    print(f"     = (2+1)(2+1)-1  =>  LOCAL TOMOGRAPHY HOLDS (like classical & complex QM; unlike real QM/E7 where 9<10),")
    print("     yet the theory HAS entanglement (PR box outside the separable hull). So local tomography is NOT")
    print("     classicality — it is E7's R-vs-C test — and the gbit sits strictly between the simplex and quantum.")

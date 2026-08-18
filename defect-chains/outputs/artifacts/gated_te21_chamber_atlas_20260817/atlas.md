# Gated TE(2=1) Chamber Atlas and Exact Certificates

**Status: COMPLETE for the actual normalized guarded-V domain; FAILED-AT if the four displayed gate clauses are read as the entire formal endpoint domain.**

The actual V relations also prove `B<=D` and `B<=F`; after swapping q,r we may assume `D<=F`, and the overlap gate then gives `E<=D`. Translating D to 0 gives `A=-x, B=-y, C0=-c, D=0, E=-e, F=f` with `x>y>=0,c>=1,e>=0,f>=1`. The 31 chambers below are exactly this gated/WLOG domain. The four-clause gate alone admits the exact obstruction `[1,2],[0,1],[0,2]`, recorded below; it is not silently admitted.

## Exact ledger literals

For closed intervals, `Gamma={(i,j,k): i<=j and i<=k}` and `W=1+[j=k]`. Let `X_<` count `j<k`, `X_>` count `k<j`, and `Y` count `j=k`, all unweighted. Then `N=X_<+X_>+2Y`, `O(q<r)=X_<+Y`, `O(r<q)=X_>+Y`. The exact r30 pin literals are `H=U_p(A)=mass(i>A)`, `L=L_q(D)=mass(j<D)`, and the branch violations are `N-3H` and `N-3L`; hence the certificate left sides are `3H-N` and `3L-N`.

The direct finite-sum formulas used for every replay are
`X_<=sum_{j=C0}^D ((j-A+1)_+-(j-B)_+)((F-j)_+-(E-1-j)_+)`,
`X_>=sum_{k=E}^F ((k-A+1)_+-(k-B)_+)((D-k)_+-(C0-1-k)_+)`,
`Y=sum_{h=max(C0,E)}^{min(D,F)} ((h-A+1)_+-(h-B)_+)`, with an interval-level zero guard.
These are the corrected closed-boundary formulas; equality is in the weak/right chain orientation.

## Chamber exhaustion

Exact weak-order enumeration returned `PATTERN_COUNT 31` and the ordered list is the banked list 0--30. Each row uses nonnegative integer variables `u,z_i,v`; every strict level gap is `1+z_i`, and `F=1+v`. Thus every strict/weak gate inequality is encoded, and conversely every normalized endpoint tuple has a unique row and unique slacks.

## Complete certificate table

For branch H the identity is `3H-N = alpha*(N-3L)+beta*(N-3H)+R_H`; for branch L it is `3L-N = alpha*(N-3L)+beta*(N-3H)+R_L`. Every displayed residual coefficient is nonnegative.

### 0: `y|xce`
Variables: `u, z0, v >= 0`; blocks `[['y'], ['x', 'c', 'e']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - 1`, `B=-u`, `C0=-u - z0 - 1`, `D=0`, `E=-u - z0 - 1`, `F=v + 1`
Polynomials: `N=11 + 3*v + 67/6*z0 + 5/2*z0*v + 7/2*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 10*u + 2*u*v + 7*u*z0 + u*z0*v + u*z0^2 + 2*u^2 + u^2*z0`; `H=3 + v + 31/6*z0 + 3/2*z0*v + 5/2*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 4*u + u*v + 5*u*z0 + u*z0*v + u*z0^2 + u^2 + u^2*z0`; `L=4 + v + 20/3*z0 + 3/2*z0*v + 3*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 8*u + 2*u*v + 6*u*z0 + u*z0*v + u*z0^2 + 2*u^2 + u^2*z0`.
Certificate H: `alpha=2, beta=0`; `R=22*z0 + 6*z0*v + 15*z0^2 + 3*z0^2*v + 2*z0^3 + 30*u + 9*u*v + 30*u*z0 + 6*u*z0*v + 6*u*z0^2 + 9*u^2 + 6*u^2*z0`.
Certificate L: `alpha=0, beta=0`; `R=1 + 53/6*z0 + 2*z0*v + 11/2*z0^2 + z0^2*v + 2/3*z0^3 + 14*u + 4*u*v + 11*u*z0 + 2*u*z0*v + 2*u*z0^2 + 4*u^2 + 2*u^2*z0`.

### 1: `yc|xe`
Variables: `u, z0, v >= 0`; blocks `[['y', 'c'], ['x', 'e']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - 2`, `B=-u - 1`, `C0=-u - 1`, `D=0`, `E=-u - z0 - 2`, `F=v + 1`
Polynomials: `N=18 + 4*v + 11*z0 + 2*z0*v + z0^2 + 13*u + 2*u*v + 15/2*u*z0 + u*z0*v + 1/2*u*z0^2 + 2*u^2 + u^2*z0`; `H=8 + 2*v + 9*z0 + 2*z0*v + z0^2 + 6*u + u*v + 13/2*u*z0 + u*z0*v + 1/2*u*z0^2 + u^2 + u^2*z0`; `L=9 + 2*v + 11/2*z0 + z0*v + 1/2*z0^2 + 11*u + 2*u*v + 13/2*u*z0 + u*z0*v + 1/2*u*z0^2 + 2*u^2 + u^2*z0`.
Certificate H: `alpha=0, beta=0`; `R=6 + 2*v + 16*z0 + 4*z0*v + 2*z0^2 + 5*u + u*v + 12*u*z0 + 2*u*z0*v + u*z0^2 + u^2 + 2*u^2*z0`.
Certificate L: `alpha=0, beta=0`; `R=9 + 2*v + 11/2*z0 + z0*v + 1/2*z0^2 + 20*u + 4*u*v + 12*u*z0 + 2*u*z0*v + u*z0^2 + 4*u^2 + 2*u^2*z0`.

### 2: `yce|x`
Variables: `u, z0, v >= 0`; blocks `[['y', 'c', 'e'], ['x']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - 2`, `B=-u - 1`, `C0=-u - 1`, `D=0`, `E=-u - 1`, `F=v + 1`
Polynomials: `N=16 + 4*v + 8*z0 + 2*z0*v + 12*u + 2*u*v + 6*u*z0 + u*z0*v + 2*u^2 + u^2*z0`; `H=8 + 2*v + 8*z0 + 2*z0*v + 6*u + u*v + 6*u*z0 + u*z0*v + u^2 + u^2*z0`; `L=8 + 2*v + 4*z0 + z0*v + 10*u + 2*u*v + 5*u*z0 + u*z0*v + 2*u^2 + u^2*z0`.
Certificate H: `alpha=0, beta=0`; `R=8 + 2*v + 16*z0 + 4*z0*v + 6*u + u*v + 12*u*z0 + 2*u*z0*v + u^2 + 2*u^2*z0`.
Certificate L: `alpha=0, beta=0`; `R=8 + 2*v + 4*z0 + z0*v + 18*u + 4*u*v + 9*u*z0 + 2*u*z0*v + 4*u^2 + 2*u^2*z0`.

### 3: `ye|xc`
Variables: `u, z0, v >= 0`; blocks `[['y', 'e'], ['x', 'c']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - 1`, `B=-u`, `C0=-u - z0 - 1`, `D=0`, `E=-u`, `F=v + 1`
Polynomials: `N=8 + 3*v + 6*z0 + 5/2*z0*v + z0^2 + 1/2*z0^2*v + 9*u + 2*u*v + 11/2*u*z0 + u*z0*v + 1/2*u*z0^2 + 2*u^2 + u^2*z0`; `H=3 + v + 4*z0 + 3/2*z0*v + z0^2 + 1/2*z0^2*v + 4*u + u*v + 9/2*u*z0 + u*z0*v + 1/2*u*z0^2 + u^2 + u^2*z0`; `L=2 + v + 3*z0 + 3/2*z0*v + z0^2 + 1/2*z0^2*v + 7*u + 2*u*v + 9/2*u*z0 + u*z0*v + 1/2*u*z0^2 + 2*u^2 + u^2*z0`.
Certificate H: `alpha=0, beta=0`; `R=1 + 6*z0 + 2*z0*v + 2*z0^2 + z0^2*v + 3*u + u*v + 8*u*z0 + 2*u*z0*v + u*z0^2 + u^2 + 2*u^2*z0`.
Certificate L: `alpha=0, beta=2`; `R=15*z0 + 6*z0*v + 6*z0^2 + 3*z0^2*v + 18*u + 6*u*v + 24*u*z0 + 6*u*z0*v + 3*u*z0^2 + 6*u^2 + 6*u^2*z0`.

### 4: `c|y|xe`
Variables: `u, z0, z1, v >= 0`; blocks `[['c'], ['y'], ['x', 'e']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - 3`, `B=-u - z0 - 2`, `C0=-u - 1`, `D=0`, `E=-u - z0 - z1 - 3`, `F=v + 1`
Polynomials: `N=22 + 4*v + 13*z1 + 2*z1*v + z1^2 + 4*z0 + 2*z0*z1 + 15*u + 2*u*v + 17/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 2*u*z0 + u*z0*z1 + 2*u^2 + u^2*z1`; `H=10 + 2*v + 11*z1 + 2*z1*v + z1^2 + 2*z0 + 2*z0*z1 + 7*u + u*v + 15/2*u*z1 + u*z1*v + 1/2*u*z1^2 + u*z0 + u*z0*z1 + u^2 + u^2*z1`; `L=11 + 2*v + 13/2*z1 + z1*v + 1/2*z1^2 + 2*z0 + z0*z1 + 13*u + 2*u*v + 15/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 2*u*z0 + u*z0*z1 + 2*u^2 + u^2*z1`.
Certificate H: `alpha=0, beta=0`; `R=8 + 2*v + 20*z1 + 4*z1*v + 2*z1^2 + 2*z0 + 4*z0*z1 + 6*u + u*v + 14*u*z1 + 2*u*z1*v + u*z1^2 + u*z0 + 2*u*z0*z1 + u^2 + 2*u^2*z1`.
Certificate L: `alpha=0, beta=0`; `R=11 + 2*v + 13/2*z1 + z1*v + 1/2*z1^2 + 2*z0 + z0*z1 + 24*u + 4*u*v + 14*u*z1 + 2*u*z1*v + u*z1^2 + 4*u*z0 + 2*u*z0*z1 + 4*u^2 + 2*u^2*z1`.

### 5: `c|ye|x`
Variables: `u, z0, z1, v >= 0`; blocks `[['c'], ['y', 'e'], ['x']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - 3`, `B=-u - z0 - 2`, `C0=-u - 1`, `D=0`, `E=-u - z0 - 2`, `F=v + 1`
Polynomials: `N=20 + 4*v + 10*z1 + 2*z1*v + 4*z0 + 2*z0*z1 + 14*u + 2*u*v + 7*u*z1 + u*z1*v + 2*u*z0 + u*z0*z1 + 2*u^2 + u^2*z1`; `H=10 + 2*v + 10*z1 + 2*z1*v + 2*z0 + 2*z0*z1 + 7*u + u*v + 7*u*z1 + u*z1*v + u*z0 + u*z0*z1 + u^2 + u^2*z1`; `L=10 + 2*v + 5*z1 + z1*v + 2*z0 + z0*z1 + 12*u + 2*u*v + 6*u*z1 + u*z1*v + 2*u*z0 + u*z0*z1 + 2*u^2 + u^2*z1`.
Certificate H: `alpha=0, beta=0`; `R=10 + 2*v + 20*z1 + 4*z1*v + 2*z0 + 4*z0*z1 + 7*u + u*v + 14*u*z1 + 2*u*z1*v + u*z0 + 2*u*z0*z1 + u^2 + 2*u^2*z1`.
Certificate L: `alpha=0, beta=0`; `R=10 + 2*v + 5*z1 + z1*v + 2*z0 + z0*z1 + 22*u + 4*u*v + 11*u*z1 + 2*u*z1*v + 4*u*z0 + 2*u*z0*z1 + 4*u^2 + 2*u^2*z1`.

### 6: `ce|y|x`
Variables: `u, z0, z1, v >= 0`; blocks `[['c', 'e'], ['y'], ['x']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - 3`, `B=-u - z0 - 2`, `C0=-u - 1`, `D=0`, `E=-u - 1`, `F=v + 1`
Polynomials: `N=16 + 4*v + 8*z1 + 2*z1*v + 12*u + 2*u*v + 6*u*z1 + u*z1*v + 2*u^2 + u^2*z1`; `H=8 + 2*v + 8*z1 + 2*z1*v + 6*u + u*v + 6*u*z1 + u*z1*v + u^2 + u^2*z1`; `L=8 + 2*v + 4*z1 + z1*v + 10*u + 2*u*v + 5*u*z1 + u*z1*v + 2*u^2 + u^2*z1`.
Certificate H: `alpha=0, beta=0`; `R=8 + 2*v + 16*z1 + 4*z1*v + 6*u + u*v + 12*u*z1 + 2*u*z1*v + u^2 + 2*u^2*z1`.
Certificate L: `alpha=0, beta=0`; `R=8 + 2*v + 4*z1 + z1*v + 18*u + 4*u*v + 9*u*z1 + 2*u*z1*v + 4*u^2 + 2*u^2*z1`.

### 7: `e|y|xc`
Variables: `u, z0, z1, v >= 0`; blocks `[['e'], ['y'], ['x', 'c']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - 2`, `B=-u - z0 - 1`, `C0=-u - z0 - z1 - 2`, `D=0`, `E=-u`, `F=v + 1`
Polynomials: `N=12 + 5*v + 8*z1 + 7/2*z1*v + z1^2 + 1/2*z1^2*v + 4*z0 + 2*z0*v + 2*z0*z1 + z0*z1*v + 11*u + 2*u*v + 13/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 2*u*z0 + u*z0*z1 + 2*u^2 + u^2*z1`; `H=5 + 2*v + 6*z1 + 5/2*z1*v + z1^2 + 1/2*z1^2*v + 2*z0 + z0*v + 2*z0*z1 + z0*z1*v + 5*u + u*v + 11/2*u*z1 + u*z1*v + 1/2*u*z1^2 + u*z0 + u*z0*z1 + u^2 + u^2*z1`; `L=6 + 3*v + 5*z1 + 5/2*z1*v + z1^2 + 1/2*z1^2*v + 4*z0 + 2*z0*v + 2*z0*z1 + z0*z1*v + 9*u + 2*u*v + 11/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 2*u*z0 + u*z0*z1 + 2*u^2 + u^2*z1`.
Certificate H: `alpha=0, beta=0`; `R=3 + v + 10*z1 + 4*z1*v + 2*z1^2 + z1^2*v + 2*z0 + z0*v + 4*z0*z1 + 2*z0*z1*v + 4*u + u*v + 10*u*z1 + 2*u*z1*v + u*z1^2 + u*z0 + 2*u*z0*z1 + u^2 + 2*u^2*z1`.
Certificate L: `alpha=0, beta=0`; `R=6 + 4*v + 7*z1 + 4*z1*v + 2*z1^2 + z1^2*v + 8*z0 + 4*z0*v + 4*z0*z1 + 2*z0*z1*v + 16*u + 4*u*v + 10*u*z1 + 2*u*z1*v + u*z1^2 + 4*u*z0 + 2*u*z0*z1 + 4*u^2 + 2*u^2*z1`.

### 8: `e|yc|x`
Variables: `u, z0, z1, v >= 0`; blocks `[['e'], ['y', 'c'], ['x']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - 2`, `B=-u - z0 - 1`, `C0=-u - z0 - 1`, `D=0`, `E=-u`, `F=v + 1`
Polynomials: `N=10 + 4*v + 5*z1 + 2*z1*v + 4*z0 + 2*z0*v + 2*z0*z1 + z0*z1*v + 10*u + 2*u*v + 5*u*z1 + u*z1*v + 2*u*z0 + u*z0*z1 + 2*u^2 + u^2*z1`; `H=5 + 2*v + 5*z1 + 2*z1*v + 2*z0 + z0*v + 2*z0*z1 + z0*z1*v + 5*u + u*v + 5*u*z1 + u*z1*v + u*z0 + u*z0*z1 + u^2 + u^2*z1`; `L=4 + 2*v + 2*z1 + z1*v + 4*z0 + 2*z0*v + 2*z0*z1 + z0*z1*v + 8*u + 2*u*v + 4*u*z1 + u*z1*v + 2*u*z0 + u*z0*z1 + 2*u^2 + u^2*z1`.
Certificate H: `alpha=0, beta=0`; `R=5 + 2*v + 10*z1 + 4*z1*v + 2*z0 + z0*v + 4*z0*z1 + 2*z0*z1*v + 5*u + u*v + 10*u*z1 + 2*u*z1*v + u*z0 + 2*u*z0*z1 + u^2 + 2*u^2*z1`.
Certificate L: `alpha=0, beta=0`; `R=2 + 2*v + z1 + z1*v + 8*z0 + 4*z0*v + 4*z0*z1 + 2*z0*z1*v + 14*u + 4*u*v + 7*u*z1 + 2*u*z1*v + 4*u*z0 + 2*u*z0*z1 + 4*u^2 + 2*u^2*z1`.

### 9: `y|c|xe`
Variables: `u, z0, z1, v >= 0`; blocks `[['y'], ['c'], ['x', 'e']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - 2`, `B=-u`, `C0=-u - z0 - 1`, `D=0`, `E=-u - z0 - z1 - 2`, `F=v + 1`
Polynomials: `N=21 + 5*v + 11*z1 + 2*z1*v + z1^2 + 109/6*z0 + 7/2*z0*v + 15/2*z0*z1 + z0*z1*v + 1/2*z0*z1^2 + 9/2*z0^2 + 1/2*z0^2*v + z0^2*z1 + 1/3*z0^3 + 17*u + 3*u*v + 15/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 9*u*z0 + u*z0*v + 2*u*z0*z1 + u*z0^2 + 3*u^2 + u^2*z1 + u^2*z0`; `H=11 + 3*v + 9*z1 + 2*z1*v + z1^2 + 67/6*z0 + 5/2*z0*v + 13/2*z0*z1 + z0*z1*v + 1/2*z0*z1^2 + 7/2*z0^2 + 1/2*z0^2*v + z0^2*z1 + 1/3*z0^3 + 10*u + 2*u*v + 13/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 7*u*z0 + u*z0*v + 2*u*z0*z1 + u*z0^2 + 2*u^2 + u^2*z1 + u^2*z0`; `L=9 + 2*v + 11/2*z1 + z1*v + 1/2*z1^2 + 38/3*z0 + 5/2*z0*v + 13/2*z0*z1 + z0*z1*v + 1/2*z0*z1^2 + 4*z0^2 + 1/2*z0^2*v + z0^2*z1 + 1/3*z0^3 + 14*u + 3*u*v + 13/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 8*u*z0 + u*z0*v + 2*u*z0*z1 + u*z0^2 + 3*u^2 + u^2*z1 + u^2*z0`.
Certificate H: `alpha=0, beta=0`; `R=12 + 4*v + 16*z1 + 4*z1*v + 2*z1^2 + 46/3*z0 + 4*z0*v + 12*z0*z1 + 2*z0*z1*v + z0*z1^2 + 6*z0^2 + z0^2*v + 2*z0^2*z1 + 2/3*z0^3 + 13*u + 3*u*v + 12*u*z1 + 2*u*z1*v + u*z1^2 + 12*u*z0 + 2*u*z0*v + 4*u*z0*z1 + 2*u*z0^2 + 3*u^2 + 2*u^2*z1 + 2*u^2*z0`.
Certificate L: `alpha=0, beta=0`; `R=6 + v + 11/2*z1 + z1*v + 1/2*z1^2 + 119/6*z0 + 4*z0*v + 12*z0*z1 + 2*z0*z1*v + z0*z1^2 + 15/2*z0^2 + z0^2*v + 2*z0^2*z1 + 2/3*z0^3 + 25*u + 6*u*v + 12*u*z1 + 2*u*z1*v + u*z1^2 + 15*u*z0 + 2*u*z0*v + 4*u*z0*z1 + 2*u*z0^2 + 6*u^2 + 2*u^2*z1 + 2*u^2*z0`.

### 10: `y|ce|x`
Variables: `u, z0, z1, v >= 0`; blocks `[['y'], ['c', 'e'], ['x']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - 2`, `B=-u`, `C0=-u - z0 - 1`, `D=0`, `E=-u - z0 - 1`, `F=v + 1`
Polynomials: `N=19 + 5*v + 8*z1 + 2*z1*v + 103/6*z0 + 7/2*z0*v + 6*z0*z1 + z0*z1*v + 9/2*z0^2 + 1/2*z0^2*v + z0^2*z1 + 1/3*z0^3 + 16*u + 3*u*v + 6*u*z1 + u*z1*v + 9*u*z0 + u*z0*v + 2*u*z0*z1 + u*z0^2 + 3*u^2 + u^2*z1 + u^2*z0`; `H=11 + 3*v + 8*z1 + 2*z1*v + 67/6*z0 + 5/2*z0*v + 6*z0*z1 + z0*z1*v + 7/2*z0^2 + 1/2*z0^2*v + z0^2*z1 + 1/3*z0^3 + 10*u + 2*u*v + 6*u*z1 + u*z1*v + 7*u*z0 + u*z0*v + 2*u*z0*z1 + u*z0^2 + 2*u^2 + u^2*z1 + u^2*z0`; `L=8 + 2*v + 4*z1 + z1*v + 35/3*z0 + 5/2*z0*v + 5*z0*z1 + z0*z1*v + 4*z0^2 + 1/2*z0^2*v + z0^2*z1 + 1/3*z0^3 + 13*u + 3*u*v + 5*u*z1 + u*z1*v + 8*u*z0 + u*z0*v + 2*u*z0*z1 + u*z0^2 + 3*u^2 + u^2*z1 + u^2*z0`.
Certificate H: `alpha=0, beta=0`; `R=14 + 4*v + 16*z1 + 4*z1*v + 49/3*z0 + 4*z0*v + 12*z0*z1 + 2*z0*z1*v + 6*z0^2 + z0^2*v + 2*z0^2*z1 + 2/3*z0^3 + 14*u + 3*u*v + 12*u*z1 + 2*u*z1*v + 12*u*z0 + 2*u*z0*v + 4*u*z0*z1 + 2*u*z0^2 + 3*u^2 + 2*u^2*z1 + 2*u^2*z0`.
Certificate L: `alpha=0, beta=0`; `R=5 + v + 4*z1 + z1*v + 107/6*z0 + 4*z0*v + 9*z0*z1 + 2*z0*z1*v + 15/2*z0^2 + z0^2*v + 2*z0^2*z1 + 2/3*z0^3 + 23*u + 6*u*v + 9*u*z1 + 2*u*z1*v + 15*u*z0 + 2*u*z0*v + 4*u*z0*z1 + 2*u*z0^2 + 6*u^2 + 2*u^2*z1 + 2*u^2*z0`.

### 11: `y|e|xc`
Variables: `u, z0, z1, v >= 0`; blocks `[['y'], ['e'], ['x', 'c']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - 2`, `B=-u`, `C0=-u - z0 - z1 - 2`, `D=0`, `E=-u - z0 - 1`, `F=v + 1`
Polynomials: `N=22 + 6*v + 25/2*z1 + 7/2*z1*v + 3/2*z1^2 + 1/2*z1^2*v + 109/6*z0 + 7/2*z0*v + 15/2*z0*z1 + z0*z1*v + 1/2*z0*z1^2 + 9/2*z0^2 + 1/2*z0^2*v + z0^2*z1 + 1/3*z0^3 + 17*u + 3*u*v + 15/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 9*u*z0 + u*z0*v + 2*u*z0*z1 + u*z0^2 + 3*u^2 + u^2*z1 + u^2*z0`; `H=11 + 3*v + 19/2*z1 + 5/2*z1*v + 3/2*z1^2 + 1/2*z1^2*v + 67/6*z0 + 5/2*z0*v + 13/2*z0*z1 + z0*z1*v + 1/2*z0*z1^2 + 7/2*z0^2 + 1/2*z0^2*v + z0^2*z1 + 1/3*z0^3 + 10*u + 2*u*v + 13/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 7*u*z0 + u*z0*v + 2*u*z0*z1 + u*z0^2 + 2*u^2 + u^2*z1 + u^2*z0`; `L=11 + 3*v + 17/2*z1 + 5/2*z1*v + 3/2*z1^2 + 1/2*z1^2*v + 38/3*z0 + 5/2*z0*v + 13/2*z0*z1 + z0*z1*v + 1/2*z0*z1^2 + 4*z0^2 + 1/2*z0^2*v + z0^2*z1 + 1/3*z0^3 + 14*u + 3*u*v + 13/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 8*u*z0 + u*z0*v + 2*u*z0*z1 + u*z0^2 + 3*u^2 + u^2*z1 + u^2*z0`.
Certificate H: `alpha=0, beta=0`; `R=11 + 3*v + 16*z1 + 4*z1*v + 3*z1^2 + z1^2*v + 46/3*z0 + 4*z0*v + 12*z0*z1 + 2*z0*z1*v + z0*z1^2 + 6*z0^2 + z0^2*v + 2*z0^2*z1 + 2/3*z0^3 + 13*u + 3*u*v + 12*u*z1 + 2*u*z1*v + u*z1^2 + 12*u*z0 + 2*u*z0*v + 4*u*z0*z1 + 2*u*z0^2 + 3*u^2 + 2*u^2*z1 + 2*u^2*z0`.
Certificate L: `alpha=0, beta=0`; `R=11 + 3*v + 13*z1 + 4*z1*v + 3*z1^2 + z1^2*v + 119/6*z0 + 4*z0*v + 12*z0*z1 + 2*z0*z1*v + z0*z1^2 + 15/2*z0^2 + z0^2*v + 2*z0^2*z1 + 2/3*z0^3 + 25*u + 6*u*v + 12*u*z1 + 2*u*z1*v + u*z1^2 + 15*u*z0 + 2*u*z0*v + 4*u*z0*z1 + 2*u*z0^2 + 6*u^2 + 2*u^2*z1 + 2*u^2*z0`.

### 12: `y|x|ce`
Variables: `u, z0, z1, v >= 0`; blocks `[['y'], ['x'], ['c', 'e']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - 1`, `B=-u`, `C0=-u - z0 - z1 - 2`, `D=0`, `E=-u - z0 - z1 - 2`, `F=v + 1`
Polynomials: `N=11 + 3*v + 67/6*z0 + 5/2*z0*v + 7/2*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 10*u + 2*u*v + 7*u*z0 + u*z0*v + u*z0^2 + 2*u^2 + u^2*z0`; `H=3 + v + 31/6*z0 + 3/2*z0*v + 5/2*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 4*u + u*v + 5*u*z0 + u*z0*v + u*z0^2 + u^2 + u^2*z0`; `L=4 + v + 20/3*z0 + 3/2*z0*v + 3*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 8*u + 2*u*v + 6*u*z0 + u*z0*v + u*z0^2 + 2*u^2 + u^2*z0`.
Certificate H: `alpha=2, beta=0`; `R=22*z0 + 6*z0*v + 15*z0^2 + 3*z0^2*v + 2*z0^3 + 30*u + 9*u*v + 30*u*z0 + 6*u*z0*v + 6*u*z0^2 + 9*u^2 + 6*u^2*z0`.
Certificate L: `alpha=0, beta=0`; `R=1 + 53/6*z0 + 2*z0*v + 11/2*z0^2 + z0^2*v + 2/3*z0^3 + 14*u + 4*u*v + 11*u*z0 + 2*u*z0*v + 2*u*z0^2 + 4*u^2 + 2*u^2*z0`.

### 13: `y|xc|e`
Variables: `u, z0, z1, v >= 0`; blocks `[['y'], ['x', 'c'], ['e']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - 1`, `B=-u`, `C0=-u - z0 - 1`, `D=0`, `E=-u - z0 - z1 - 2`, `F=v + 1`
Polynomials: `N=11 + 3*v + 67/6*z0 + 5/2*z0*v + 7/2*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 10*u + 2*u*v + 7*u*z0 + u*z0*v + u*z0^2 + 2*u^2 + u^2*z0`; `H=3 + v + 31/6*z0 + 3/2*z0*v + 5/2*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 4*u + u*v + 5*u*z0 + u*z0*v + u*z0^2 + u^2 + u^2*z0`; `L=4 + v + 20/3*z0 + 3/2*z0*v + 3*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 8*u + 2*u*v + 6*u*z0 + u*z0*v + u*z0^2 + 2*u^2 + u^2*z0`.
Certificate H: `alpha=2, beta=0`; `R=22*z0 + 6*z0*v + 15*z0^2 + 3*z0^2*v + 2*z0^3 + 30*u + 9*u*v + 30*u*z0 + 6*u*z0*v + 6*u*z0^2 + 9*u^2 + 6*u^2*z0`.
Certificate L: `alpha=0, beta=0`; `R=1 + 53/6*z0 + 2*z0*v + 11/2*z0^2 + z0^2*v + 2/3*z0^3 + 14*u + 4*u*v + 11*u*z0 + 2*u*z0*v + 2*u*z0^2 + 4*u^2 + 2*u^2*z0`.

### 14: `y|xe|c`
Variables: `u, z0, z1, v >= 0`; blocks `[['y'], ['x', 'e'], ['c']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - 1`, `B=-u`, `C0=-u - z0 - z1 - 2`, `D=0`, `E=-u - z0 - 1`, `F=v + 1`
Polynomials: `N=11 + 3*v + 67/6*z0 + 5/2*z0*v + 7/2*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 10*u + 2*u*v + 7*u*z0 + u*z0*v + u*z0^2 + 2*u^2 + u^2*z0`; `H=3 + v + 31/6*z0 + 3/2*z0*v + 5/2*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 4*u + u*v + 5*u*z0 + u*z0*v + u*z0^2 + u^2 + u^2*z0`; `L=4 + v + 20/3*z0 + 3/2*z0*v + 3*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 8*u + 2*u*v + 6*u*z0 + u*z0*v + u*z0^2 + 2*u^2 + u^2*z0`.
Certificate H: `alpha=2, beta=0`; `R=22*z0 + 6*z0*v + 15*z0^2 + 3*z0^2*v + 2*z0^3 + 30*u + 9*u*v + 30*u*z0 + 6*u*z0*v + 6*u*z0^2 + 9*u^2 + 6*u^2*z0`.
Certificate L: `alpha=0, beta=0`; `R=1 + 53/6*z0 + 2*z0*v + 11/2*z0^2 + z0^2*v + 2/3*z0^3 + 14*u + 4*u*v + 11*u*z0 + 2*u*z0*v + 2*u*z0^2 + 4*u^2 + 2*u^2*z0`.

### 15: `yc|e|x`
Variables: `u, z0, z1, v >= 0`; blocks `[['y', 'c'], ['e'], ['x']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - 3`, `B=-u - 1`, `C0=-u - 1`, `D=0`, `E=-u - z0 - 2`, `F=v + 1`
Polynomials: `N=28 + 6*v + 10*z1 + 2*z1*v + 13*z0 + 2*z0*v + 2*z0*z1 + z0^2 + 20*u + 3*u*v + 7*u*z1 + u*z1*v + 17/2*u*z0 + u*z0*v + u*z0*z1 + 1/2*u*z0^2 + 3*u^2 + u^2*z1 + u^2*z0`; `H=18 + 4*v + 10*z1 + 2*z1*v + 11*z0 + 2*z0*v + 2*z0*z1 + z0^2 + 13*u + 2*u*v + 7*u*z1 + u*z1*v + 15/2*u*z0 + u*z0*v + u*z0*z1 + 1/2*u*z0^2 + 2*u^2 + u^2*z1 + u^2*z0`; `L=14 + 3*v + 5*z1 + z1*v + 13/2*z0 + z0*v + z0*z1 + 1/2*z0^2 + 17*u + 3*u*v + 6*u*z1 + u*z1*v + 15/2*u*z0 + u*z0*v + u*z0*z1 + 1/2*u*z0^2 + 3*u^2 + u^2*z1 + u^2*z0`.
Certificate H: `alpha=0, beta=0`; `R=26 + 6*v + 20*z1 + 4*z1*v + 20*z0 + 4*z0*v + 4*z0*z1 + 2*z0^2 + 19*u + 3*u*v + 14*u*z1 + 2*u*z1*v + 14*u*z0 + 2*u*z0*v + 2*u*z0*z1 + u*z0^2 + 3*u^2 + 2*u^2*z1 + 2*u^2*z0`.
Certificate L: `alpha=0, beta=0`; `R=14 + 3*v + 5*z1 + z1*v + 13/2*z0 + z0*v + z0*z1 + 1/2*z0^2 + 31*u + 6*u*v + 11*u*z1 + 2*u*z1*v + 14*u*z0 + 2*u*z0*v + 2*u*z0*z1 + u*z0^2 + 6*u^2 + 2*u^2*z1 + 2*u^2*z0`.

### 16: `yc|x|e`
Variables: `u, z0, z1, v >= 0`; blocks `[['y', 'c'], ['x'], ['e']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - 2`, `B=-u - 1`, `C0=-u - 1`, `D=0`, `E=-u - z0 - z1 - 3`, `F=v + 1`
Polynomials: `N=18 + 4*v + 11*z0 + 2*z0*v + z0^2 + 13*u + 2*u*v + 15/2*u*z0 + u*z0*v + 1/2*u*z0^2 + 2*u^2 + u^2*z0`; `H=8 + 2*v + 9*z0 + 2*z0*v + z0^2 + 6*u + u*v + 13/2*u*z0 + u*z0*v + 1/2*u*z0^2 + u^2 + u^2*z0`; `L=9 + 2*v + 11/2*z0 + z0*v + 1/2*z0^2 + 11*u + 2*u*v + 13/2*u*z0 + u*z0*v + 1/2*u*z0^2 + 2*u^2 + u^2*z0`.
Certificate H: `alpha=0, beta=0`; `R=6 + 2*v + 16*z0 + 4*z0*v + 2*z0^2 + 5*u + u*v + 12*u*z0 + 2*u*z0*v + u*z0^2 + u^2 + 2*u^2*z0`.
Certificate L: `alpha=0, beta=0`; `R=9 + 2*v + 11/2*z0 + z0*v + 1/2*z0^2 + 20*u + 4*u*v + 12*u*z0 + 2*u*z0*v + u*z0^2 + 4*u^2 + 2*u^2*z0`.

### 17: `ye|c|x`
Variables: `u, z0, z1, v >= 0`; blocks `[['y', 'e'], ['c'], ['x']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - 2`, `B=-u`, `C0=-u - z0 - 1`, `D=0`, `E=-u`, `F=v + 1`
Polynomials: `N=13 + 5*v + 5*z1 + 2*z1*v + 8*z0 + 7/2*z0*v + 2*z0*z1 + z0*z1*v + z0^2 + 1/2*z0^2*v + 14*u + 3*u*v + 5*u*z1 + u*z1*v + 13/2*u*z0 + u*z0*v + u*z0*z1 + 1/2*u*z0^2 + 3*u^2 + u^2*z1 + u^2*z0`; `H=8 + 3*v + 5*z1 + 2*z1*v + 6*z0 + 5/2*z0*v + 2*z0*z1 + z0*z1*v + z0^2 + 1/2*z0^2*v + 9*u + 2*u*v + 5*u*z1 + u*z1*v + 11/2*u*z0 + u*z0*v + u*z0*z1 + 1/2*u*z0^2 + 2*u^2 + u^2*z1 + u^2*z0`; `L=4 + 2*v + 2*z1 + z1*v + 5*z0 + 5/2*z0*v + 2*z0*z1 + z0*z1*v + z0^2 + 1/2*z0^2*v + 11*u + 3*u*v + 4*u*z1 + u*z1*v + 11/2*u*z0 + u*z0*v + u*z0*z1 + 1/2*u*z0^2 + 3*u^2 + u^2*z1 + u^2*z0`.
Certificate H: `alpha=0, beta=0`; `R=11 + 4*v + 10*z1 + 4*z1*v + 10*z0 + 4*z0*v + 4*z0*z1 + 2*z0*z1*v + 2*z0^2 + z0^2*v + 13*u + 3*u*v + 10*u*z1 + 2*u*z1*v + 10*u*z0 + 2*u*z0*v + 2*u*z0*z1 + u*z0^2 + 3*u^2 + 2*u^2*z1 + 2*u^2*z0`.
Certificate L: `alpha=0, beta=1/11`; `R=15/11*v + 21/11*z1 + 15/11*z1*v + 87/11*z0 + 48/11*z0*v + 48/11*z0*z1 + 24/11*z0*z1*v + 24/11*z0^2 + 12/11*z0^2*v + 222/11*u + 69/11*u*v + 87/11*u*z1 + 24/11*u*z1*v + 120/11*u*z0 + 24/11*u*z0*v + 24/11*u*z0*z1 + 12/11*u*z0^2 + 69/11*u^2 + 24/11*u^2*z1 + 24/11*u^2*z0`.

### 18: `ye|x|c`
Variables: `u, z0, z1, v >= 0`; blocks `[['y', 'e'], ['x'], ['c']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - 1`, `B=-u`, `C0=-u - z0 - z1 - 2`, `D=0`, `E=-u`, `F=v + 1`
Polynomials: `N=8 + 3*v + 6*z0 + 5/2*z0*v + z0^2 + 1/2*z0^2*v + 9*u + 2*u*v + 11/2*u*z0 + u*z0*v + 1/2*u*z0^2 + 2*u^2 + u^2*z0`; `H=3 + v + 4*z0 + 3/2*z0*v + z0^2 + 1/2*z0^2*v + 4*u + u*v + 9/2*u*z0 + u*z0*v + 1/2*u*z0^2 + u^2 + u^2*z0`; `L=2 + v + 3*z0 + 3/2*z0*v + z0^2 + 1/2*z0^2*v + 7*u + 2*u*v + 9/2*u*z0 + u*z0*v + 1/2*u*z0^2 + 2*u^2 + u^2*z0`.
Certificate H: `alpha=0, beta=0`; `R=1 + 6*z0 + 2*z0*v + 2*z0^2 + z0^2*v + 3*u + u*v + 8*u*z0 + 2*u*z0*v + u*z0^2 + u^2 + 2*u^2*z0`.
Certificate L: `alpha=0, beta=2`; `R=15*z0 + 6*z0*v + 6*z0^2 + 3*z0^2*v + 18*u + 6*u*v + 24*u*z0 + 6*u*z0*v + 3*u*z0^2 + 6*u^2 + 6*u^2*z0`.

### 19: `c|e|y|x`
Variables: `u, z0, z1, z2, v >= 0`; blocks `[['c'], ['e'], ['y'], ['x']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - z2 - 4`, `B=-u - z0 - z1 - 3`, `C0=-u - 1`, `D=0`, `E=-u - z0 - 2`, `F=v + 1`
Polynomials: `N=20 + 4*v + 10*z2 + 2*z2*v + 4*z0 + 2*z0*z2 + 14*u + 2*u*v + 7*u*z2 + u*z2*v + 2*u*z0 + u*z0*z2 + 2*u^2 + u^2*z2`; `H=10 + 2*v + 10*z2 + 2*z2*v + 2*z0 + 2*z0*z2 + 7*u + u*v + 7*u*z2 + u*z2*v + u*z0 + u*z0*z2 + u^2 + u^2*z2`; `L=10 + 2*v + 5*z2 + z2*v + 2*z0 + z0*z2 + 12*u + 2*u*v + 6*u*z2 + u*z2*v + 2*u*z0 + u*z0*z2 + 2*u^2 + u^2*z2`.
Certificate H: `alpha=0, beta=0`; `R=10 + 2*v + 20*z2 + 4*z2*v + 2*z0 + 4*z0*z2 + 7*u + u*v + 14*u*z2 + 2*u*z2*v + u*z0 + 2*u*z0*z2 + u^2 + 2*u^2*z2`.
Certificate L: `alpha=0, beta=0`; `R=10 + 2*v + 5*z2 + z2*v + 2*z0 + z0*z2 + 22*u + 4*u*v + 11*u*z2 + 2*u*z2*v + 4*u*z0 + 2*u*z0*z2 + 4*u^2 + 2*u^2*z2`.

### 20: `c|y|e|x`
Variables: `u, z0, z1, z2, v >= 0`; blocks `[['c'], ['y'], ['e'], ['x']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - z2 - 4`, `B=-u - z0 - 2`, `C0=-u - 1`, `D=0`, `E=-u - z0 - z1 - 3`, `F=v + 1`
Polynomials: `N=34 + 6*v + 12*z2 + 2*z2*v + 15*z1 + 2*z1*v + 2*z1*z2 + z1^2 + 6*z0 + 2*z0*z2 + 2*z0*z1 + 23*u + 3*u*v + 8*u*z2 + u*z2*v + 19/2*u*z1 + u*z1*v + u*z1*z2 + 1/2*u*z1^2 + 3*u*z0 + u*z0*z2 + u*z0*z1 + 3*u^2 + u^2*z2 + u^2*z1`; `H=22 + 4*v + 12*z2 + 2*z2*v + 13*z1 + 2*z1*v + 2*z1*z2 + z1^2 + 4*z0 + 2*z0*z2 + 2*z0*z1 + 15*u + 2*u*v + 8*u*z2 + u*z2*v + 17/2*u*z1 + u*z1*v + u*z1*z2 + 1/2*u*z1^2 + 2*u*z0 + u*z0*z2 + u*z0*z1 + 2*u^2 + u^2*z2 + u^2*z1`; `L=17 + 3*v + 6*z2 + z2*v + 15/2*z1 + z1*v + z1*z2 + 1/2*z1^2 + 3*z0 + z0*z2 + z0*z1 + 20*u + 3*u*v + 7*u*z2 + u*z2*v + 17/2*u*z1 + u*z1*v + u*z1*z2 + 1/2*u*z1^2 + 3*u*z0 + u*z0*z2 + u*z0*z1 + 3*u^2 + u^2*z2 + u^2*z1`.
Certificate H: `alpha=0, beta=0`; `R=32 + 6*v + 24*z2 + 4*z2*v + 24*z1 + 4*z1*v + 4*z1*z2 + 2*z1^2 + 6*z0 + 4*z0*z2 + 4*z0*z1 + 22*u + 3*u*v + 16*u*z2 + 2*u*z2*v + 16*u*z1 + 2*u*z1*v + 2*u*z1*z2 + u*z1^2 + 3*u*z0 + 2*u*z0*z2 + 2*u*z0*z1 + 3*u^2 + 2*u^2*z2 + 2*u^2*z1`.
Certificate L: `alpha=0, beta=0`; `R=17 + 3*v + 6*z2 + z2*v + 15/2*z1 + z1*v + z1*z2 + 1/2*z1^2 + 3*z0 + z0*z2 + z0*z1 + 37*u + 6*u*v + 13*u*z2 + 2*u*z2*v + 16*u*z1 + 2*u*z1*v + 2*u*z1*z2 + u*z1^2 + 6*u*z0 + 2*u*z0*z2 + 2*u*z0*z1 + 6*u^2 + 2*u^2*z2 + 2*u^2*z1`.

### 21: `c|y|x|e`
Variables: `u, z0, z1, z2, v >= 0`; blocks `[['c'], ['y'], ['x'], ['e']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - 3`, `B=-u - z0 - 2`, `C0=-u - 1`, `D=0`, `E=-u - z0 - z1 - z2 - 4`, `F=v + 1`
Polynomials: `N=22 + 4*v + 13*z1 + 2*z1*v + z1^2 + 4*z0 + 2*z0*z1 + 15*u + 2*u*v + 17/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 2*u*z0 + u*z0*z1 + 2*u^2 + u^2*z1`; `H=10 + 2*v + 11*z1 + 2*z1*v + z1^2 + 2*z0 + 2*z0*z1 + 7*u + u*v + 15/2*u*z1 + u*z1*v + 1/2*u*z1^2 + u*z0 + u*z0*z1 + u^2 + u^2*z1`; `L=11 + 2*v + 13/2*z1 + z1*v + 1/2*z1^2 + 2*z0 + z0*z1 + 13*u + 2*u*v + 15/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 2*u*z0 + u*z0*z1 + 2*u^2 + u^2*z1`.
Certificate H: `alpha=0, beta=0`; `R=8 + 2*v + 20*z1 + 4*z1*v + 2*z1^2 + 2*z0 + 4*z0*z1 + 6*u + u*v + 14*u*z1 + 2*u*z1*v + u*z1^2 + u*z0 + 2*u*z0*z1 + u^2 + 2*u^2*z1`.
Certificate L: `alpha=0, beta=0`; `R=11 + 2*v + 13/2*z1 + z1*v + 1/2*z1^2 + 2*z0 + z0*z1 + 24*u + 4*u*v + 14*u*z1 + 2*u*z1*v + u*z1^2 + 4*u*z0 + 2*u*z0*z1 + 4*u^2 + 2*u^2*z1`.

### 22: `e|c|y|x`
Variables: `u, z0, z1, z2, v >= 0`; blocks `[['e'], ['c'], ['y'], ['x']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - z2 - 3`, `B=-u - z0 - z1 - 2`, `C0=-u - z0 - 1`, `D=0`, `E=-u`, `F=v + 1`
Polynomials: `N=10 + 4*v + 5*z2 + 2*z2*v + 4*z0 + 2*z0*v + 2*z0*z2 + z0*z2*v + 10*u + 2*u*v + 5*u*z2 + u*z2*v + 2*u*z0 + u*z0*z2 + 2*u^2 + u^2*z2`; `H=5 + 2*v + 5*z2 + 2*z2*v + 2*z0 + z0*v + 2*z0*z2 + z0*z2*v + 5*u + u*v + 5*u*z2 + u*z2*v + u*z0 + u*z0*z2 + u^2 + u^2*z2`; `L=4 + 2*v + 2*z2 + z2*v + 4*z0 + 2*z0*v + 2*z0*z2 + z0*z2*v + 8*u + 2*u*v + 4*u*z2 + u*z2*v + 2*u*z0 + u*z0*z2 + 2*u^2 + u^2*z2`.
Certificate H: `alpha=0, beta=0`; `R=5 + 2*v + 10*z2 + 4*z2*v + 2*z0 + z0*v + 4*z0*z2 + 2*z0*z2*v + 5*u + u*v + 10*u*z2 + 2*u*z2*v + u*z0 + 2*u*z0*z2 + u^2 + 2*u^2*z2`.
Certificate L: `alpha=0, beta=0`; `R=2 + 2*v + z2 + z2*v + 8*z0 + 4*z0*v + 4*z0*z2 + 2*z0*z2*v + 14*u + 4*u*v + 7*u*z2 + 2*u*z2*v + 4*u*z0 + 2*u*z0*z2 + 4*u^2 + 2*u^2*z2`.

### 23: `e|y|c|x`
Variables: `u, z0, z1, z2, v >= 0`; blocks `[['e'], ['y'], ['c'], ['x']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - z2 - 3`, `B=-u - z0 - 1`, `C0=-u - z0 - z1 - 2`, `D=0`, `E=-u`, `F=v + 1`
Polynomials: `N=19 + 8*v + 7*z2 + 3*z2*v + 10*z1 + 9/2*z1*v + 2*z1*z2 + z1*z2*v + z1^2 + 1/2*z1^2*v + 6*z0 + 3*z0*v + 2*z0*z2 + z0*z2*v + 2*z0*z1 + z0*z1*v + 17*u + 3*u*v + 6*u*z2 + u*z2*v + 15/2*u*z1 + u*z1*v + u*z1*z2 + 1/2*u*z1^2 + 3*u*z0 + u*z0*z2 + u*z0*z1 + 3*u^2 + u^2*z2 + u^2*z1`; `H=12 + 5*v + 7*z2 + 3*z2*v + 8*z1 + 7/2*z1*v + 2*z1*z2 + z1*z2*v + z1^2 + 1/2*z1^2*v + 4*z0 + 2*z0*v + 2*z0*z2 + z0*z2*v + 2*z0*z1 + z0*z1*v + 11*u + 2*u*v + 6*u*z2 + u*z2*v + 13/2*u*z1 + u*z1*v + u*z1*z2 + 1/2*u*z1^2 + 2*u*z0 + u*z0*z2 + u*z0*z1 + 2*u^2 + u^2*z2 + u^2*z1`; `L=10 + 5*v + 4*z2 + 2*z2*v + 7*z1 + 7/2*z1*v + 2*z1*z2 + z1*z2*v + z1^2 + 1/2*z1^2*v + 6*z0 + 3*z0*v + 2*z0*z2 + z0*z2*v + 2*z0*z1 + z0*z1*v + 14*u + 3*u*v + 5*u*z2 + u*z2*v + 13/2*u*z1 + u*z1*v + u*z1*z2 + 1/2*u*z1^2 + 3*u*z0 + u*z0*z2 + u*z0*z1 + 3*u^2 + u^2*z2 + u^2*z1`.
Certificate H: `alpha=0, beta=0`; `R=17 + 7*v + 14*z2 + 6*z2*v + 14*z1 + 6*z1*v + 4*z1*z2 + 2*z1*z2*v + 2*z1^2 + z1^2*v + 6*z0 + 3*z0*v + 4*z0*z2 + 2*z0*z2*v + 4*z0*z1 + 2*z0*z1*v + 16*u + 3*u*v + 12*u*z2 + 2*u*z2*v + 12*u*z1 + 2*u*z1*v + 2*u*z1*z2 + u*z1^2 + 3*u*z0 + 2*u*z0*z2 + 2*u*z0*z1 + 3*u^2 + 2*u^2*z2 + 2*u^2*z1`.
Certificate L: `alpha=0, beta=0`; `R=11 + 7*v + 5*z2 + 3*z2*v + 11*z1 + 6*z1*v + 4*z1*z2 + 2*z1*z2*v + 2*z1^2 + z1^2*v + 12*z0 + 6*z0*v + 4*z0*z2 + 2*z0*z2*v + 4*z0*z1 + 2*z0*z1*v + 25*u + 6*u*v + 9*u*z2 + 2*u*z2*v + 12*u*z1 + 2*u*z1*v + 2*u*z1*z2 + u*z1^2 + 6*u*z0 + 2*u*z0*z2 + 2*u*z0*z1 + 6*u^2 + 2*u^2*z2 + 2*u^2*z1`.

### 24: `e|y|x|c`
Variables: `u, z0, z1, z2, v >= 0`; blocks `[['e'], ['y'], ['x'], ['c']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - 2`, `B=-u - z0 - 1`, `C0=-u - z0 - z1 - z2 - 3`, `D=0`, `E=-u`, `F=v + 1`
Polynomials: `N=12 + 5*v + 8*z1 + 7/2*z1*v + z1^2 + 1/2*z1^2*v + 4*z0 + 2*z0*v + 2*z0*z1 + z0*z1*v + 11*u + 2*u*v + 13/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 2*u*z0 + u*z0*z1 + 2*u^2 + u^2*z1`; `H=5 + 2*v + 6*z1 + 5/2*z1*v + z1^2 + 1/2*z1^2*v + 2*z0 + z0*v + 2*z0*z1 + z0*z1*v + 5*u + u*v + 11/2*u*z1 + u*z1*v + 1/2*u*z1^2 + u*z0 + u*z0*z1 + u^2 + u^2*z1`; `L=6 + 3*v + 5*z1 + 5/2*z1*v + z1^2 + 1/2*z1^2*v + 4*z0 + 2*z0*v + 2*z0*z1 + z0*z1*v + 9*u + 2*u*v + 11/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 2*u*z0 + u*z0*z1 + 2*u^2 + u^2*z1`.
Certificate H: `alpha=0, beta=0`; `R=3 + v + 10*z1 + 4*z1*v + 2*z1^2 + z1^2*v + 2*z0 + z0*v + 4*z0*z1 + 2*z0*z1*v + 4*u + u*v + 10*u*z1 + 2*u*z1*v + u*z1^2 + u*z0 + 2*u*z0*z1 + u^2 + 2*u^2*z1`.
Certificate L: `alpha=0, beta=0`; `R=6 + 4*v + 7*z1 + 4*z1*v + 2*z1^2 + z1^2*v + 8*z0 + 4*z0*v + 4*z0*z1 + 2*z0*z1*v + 16*u + 4*u*v + 10*u*z1 + 2*u*z1*v + u*z1^2 + 4*u*z0 + 2*u*z0*z1 + 4*u^2 + 2*u^2*z1`.

### 25: `y|c|e|x`
Variables: `u, z0, z1, z2, v >= 0`; blocks `[['y'], ['c'], ['e'], ['x']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - z2 - 3`, `B=-u`, `C0=-u - z0 - 1`, `D=0`, `E=-u - z0 - z1 - 2`, `F=v + 1`
Polynomials: `N=31 + 7*v + 10*z2 + 2*z2*v + 13*z1 + 2*z1*v + 2*z1*z2 + z1^2 + 151/6*z0 + 9/2*z0*v + 7*z0*z2 + z0*z2*v + 17/2*z0*z1 + z0*z1*v + z0*z1*z2 + 1/2*z0*z1^2 + 11/2*z0^2 + 1/2*z0^2*v + z0^2*z2 + z0^2*z1 + 1/3*z0^3 + 24*u + 4*u*v + 7*u*z2 + u*z2*v + 17/2*u*z1 + u*z1*v + u*z1*z2 + 1/2*u*z1^2 + 11*u*z0 + u*z0*v + 2*u*z0*z2 + 2*u*z0*z1 + u*z0^2 + 4*u^2 + u^2*z2 + u^2*z1 + u^2*z0`; `H=21 + 5*v + 10*z2 + 2*z2*v + 11*z1 + 2*z1*v + 2*z1*z2 + z1^2 + 109/6*z0 + 7/2*z0*v + 7*z0*z2 + z0*z2*v + 15/2*z0*z1 + z0*z1*v + z0*z1*z2 + 1/2*z0*z1^2 + 9/2*z0^2 + 1/2*z0^2*v + z0^2*z2 + z0^2*z1 + 1/3*z0^3 + 17*u + 3*u*v + 7*u*z2 + u*z2*v + 15/2*u*z1 + u*z1*v + u*z1*z2 + 1/2*u*z1^2 + 9*u*z0 + u*z0*v + 2*u*z0*z2 + 2*u*z0*z1 + u*z0^2 + 3*u^2 + u^2*z2 + u^2*z1 + u^2*z0`; `L=14 + 3*v + 5*z2 + z2*v + 13/2*z1 + z1*v + z1*z2 + 1/2*z1^2 + 56/3*z0 + 7/2*z0*v + 6*z0*z2 + z0*z2*v + 15/2*z0*z1 + z0*z1*v + z0*z1*z2 + 1/2*z0*z1^2 + 5*z0^2 + 1/2*z0^2*v + z0^2*z2 + z0^2*z1 + 1/3*z0^3 + 20*u + 4*u*v + 6*u*z2 + u*z2*v + 15/2*u*z1 + u*z1*v + u*z1*z2 + 1/2*u*z1^2 + 10*u*z0 + u*z0*v + 2*u*z0*z2 + 2*u*z0*z1 + u*z0^2 + 4*u^2 + u^2*z2 + u^2*z1 + u^2*z0`.
Certificate H: `alpha=0, beta=0`; `R=32 + 8*v + 20*z2 + 4*z2*v + 20*z1 + 4*z1*v + 4*z1*z2 + 2*z1^2 + 88/3*z0 + 6*z0*v + 14*z0*z2 + 2*z0*z2*v + 14*z0*z1 + 2*z0*z1*v + 2*z0*z1*z2 + z0*z1^2 + 8*z0^2 + z0^2*v + 2*z0^2*z2 + 2*z0^2*z1 + 2/3*z0^3 + 27*u + 5*u*v + 14*u*z2 + 2*u*z2*v + 14*u*z1 + 2*u*z1*v + 2*u*z1*z2 + u*z1^2 + 16*u*z0 + 2*u*z0*v + 4*u*z0*z2 + 4*u*z0*z1 + 2*u*z0^2 + 5*u^2 + 2*u^2*z2 + 2*u^2*z1 + 2*u^2*z0`.
Certificate L: `alpha=0, beta=0`; `R=11 + 2*v + 5*z2 + z2*v + 13/2*z1 + z1*v + z1*z2 + 1/2*z1^2 + 185/6*z0 + 6*z0*v + 11*z0*z2 + 2*z0*z2*v + 14*z0*z1 + 2*z0*z1*v + 2*z0*z1*z2 + z0*z1^2 + 19/2*z0^2 + z0^2*v + 2*z0^2*z2 + 2*z0^2*z1 + 2/3*z0^3 + 36*u + 8*u*v + 11*u*z2 + 2*u*z2*v + 14*u*z1 + 2*u*z1*v + 2*u*z1*z2 + u*z1^2 + 19*u*z0 + 2*u*z0*v + 4*u*z0*z2 + 4*u*z0*z1 + 2*u*z0^2 + 8*u^2 + 2*u^2*z2 + 2*u^2*z1 + 2*u^2*z0`.

### 26: `y|c|x|e`
Variables: `u, z0, z1, z2, v >= 0`; blocks `[['y'], ['c'], ['x'], ['e']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - 2`, `B=-u`, `C0=-u - z0 - 1`, `D=0`, `E=-u - z0 - z1 - z2 - 3`, `F=v + 1`
Polynomials: `N=21 + 5*v + 11*z1 + 2*z1*v + z1^2 + 109/6*z0 + 7/2*z0*v + 15/2*z0*z1 + z0*z1*v + 1/2*z0*z1^2 + 9/2*z0^2 + 1/2*z0^2*v + z0^2*z1 + 1/3*z0^3 + 17*u + 3*u*v + 15/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 9*u*z0 + u*z0*v + 2*u*z0*z1 + u*z0^2 + 3*u^2 + u^2*z1 + u^2*z0`; `H=11 + 3*v + 9*z1 + 2*z1*v + z1^2 + 67/6*z0 + 5/2*z0*v + 13/2*z0*z1 + z0*z1*v + 1/2*z0*z1^2 + 7/2*z0^2 + 1/2*z0^2*v + z0^2*z1 + 1/3*z0^3 + 10*u + 2*u*v + 13/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 7*u*z0 + u*z0*v + 2*u*z0*z1 + u*z0^2 + 2*u^2 + u^2*z1 + u^2*z0`; `L=9 + 2*v + 11/2*z1 + z1*v + 1/2*z1^2 + 38/3*z0 + 5/2*z0*v + 13/2*z0*z1 + z0*z1*v + 1/2*z0*z1^2 + 4*z0^2 + 1/2*z0^2*v + z0^2*z1 + 1/3*z0^3 + 14*u + 3*u*v + 13/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 8*u*z0 + u*z0*v + 2*u*z0*z1 + u*z0^2 + 3*u^2 + u^2*z1 + u^2*z0`.
Certificate H: `alpha=0, beta=0`; `R=12 + 4*v + 16*z1 + 4*z1*v + 2*z1^2 + 46/3*z0 + 4*z0*v + 12*z0*z1 + 2*z0*z1*v + z0*z1^2 + 6*z0^2 + z0^2*v + 2*z0^2*z1 + 2/3*z0^3 + 13*u + 3*u*v + 12*u*z1 + 2*u*z1*v + u*z1^2 + 12*u*z0 + 2*u*z0*v + 4*u*z0*z1 + 2*u*z0^2 + 3*u^2 + 2*u^2*z1 + 2*u^2*z0`.
Certificate L: `alpha=0, beta=0`; `R=6 + v + 11/2*z1 + z1*v + 1/2*z1^2 + 119/6*z0 + 4*z0*v + 12*z0*z1 + 2*z0*z1*v + z0*z1^2 + 15/2*z0^2 + z0^2*v + 2*z0^2*z1 + 2/3*z0^3 + 25*u + 6*u*v + 12*u*z1 + 2*u*z1*v + u*z1^2 + 15*u*z0 + 2*u*z0*v + 4*u*z0*z1 + 2*u*z0^2 + 6*u^2 + 2*u^2*z1 + 2*u^2*z0`.

### 27: `y|e|c|x`
Variables: `u, z0, z1, z2, v >= 0`; blocks `[['y'], ['e'], ['c'], ['x']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - z2 - 3`, `B=-u`, `C0=-u - z0 - z1 - 2`, `D=0`, `E=-u - z0 - 1`, `F=v + 1`
Polynomials: `N=33 + 9*v + 11*z2 + 3*z2*v + 31/2*z1 + 9/2*z1*v + 3*z1*z2 + z1*z2*v + 3/2*z1^2 + 1/2*z1^2*v + 151/6*z0 + 9/2*z0*v + 7*z0*z2 + z0*z2*v + 17/2*z0*z1 + z0*z1*v + z0*z1*z2 + 1/2*z0*z1^2 + 11/2*z0^2 + 1/2*z0^2*v + z0^2*z2 + z0^2*z1 + 1/3*z0^3 + 24*u + 4*u*v + 7*u*z2 + u*z2*v + 17/2*u*z1 + u*z1*v + u*z1*z2 + 1/2*u*z1^2 + 11*u*z0 + u*z0*v + 2*u*z0*z2 + 2*u*z0*z1 + u*z0^2 + 4*u^2 + u^2*z2 + u^2*z1 + u^2*z0`; `H=22 + 6*v + 11*z2 + 3*z2*v + 25/2*z1 + 7/2*z1*v + 3*z1*z2 + z1*z2*v + 3/2*z1^2 + 1/2*z1^2*v + 109/6*z0 + 7/2*z0*v + 7*z0*z2 + z0*z2*v + 15/2*z0*z1 + z0*z1*v + z0*z1*z2 + 1/2*z0*z1^2 + 9/2*z0^2 + 1/2*z0^2*v + z0^2*z2 + z0^2*z1 + 1/3*z0^3 + 17*u + 3*u*v + 7*u*z2 + u*z2*v + 15/2*u*z1 + u*z1*v + u*z1*z2 + 1/2*u*z1^2 + 9*u*z0 + u*z0*v + 2*u*z0*z2 + 2*u*z0*z1 + u*z0^2 + 3*u^2 + u^2*z2 + u^2*z1 + u^2*z0`; `L=18 + 5*v + 7*z2 + 2*z2*v + 23/2*z1 + 7/2*z1*v + 3*z1*z2 + z1*z2*v + 3/2*z1^2 + 1/2*z1^2*v + 56/3*z0 + 7/2*z0*v + 6*z0*z2 + z0*z2*v + 15/2*z0*z1 + z0*z1*v + z0*z1*z2 + 1/2*z0*z1^2 + 5*z0^2 + 1/2*z0^2*v + z0^2*z2 + z0^2*z1 + 1/3*z0^3 + 20*u + 4*u*v + 6*u*z2 + u*z2*v + 15/2*u*z1 + u*z1*v + u*z1*z2 + 1/2*u*z1^2 + 10*u*z0 + u*z0*v + 2*u*z0*z2 + 2*u*z0*z1 + u*z0^2 + 4*u^2 + u^2*z2 + u^2*z1 + u^2*z0`.
Certificate H: `alpha=0, beta=0`; `R=33 + 9*v + 22*z2 + 6*z2*v + 22*z1 + 6*z1*v + 6*z1*z2 + 2*z1*z2*v + 3*z1^2 + z1^2*v + 88/3*z0 + 6*z0*v + 14*z0*z2 + 2*z0*z2*v + 14*z0*z1 + 2*z0*z1*v + 2*z0*z1*z2 + z0*z1^2 + 8*z0^2 + z0^2*v + 2*z0^2*z2 + 2*z0^2*z1 + 2/3*z0^3 + 27*u + 5*u*v + 14*u*z2 + 2*u*z2*v + 14*u*z1 + 2*u*z1*v + 2*u*z1*z2 + u*z1^2 + 16*u*z0 + 2*u*z0*v + 4*u*z0*z2 + 4*u*z0*z1 + 2*u*z0^2 + 5*u^2 + 2*u^2*z2 + 2*u^2*z1 + 2*u^2*z0`.
Certificate L: `alpha=0, beta=0`; `R=21 + 6*v + 10*z2 + 3*z2*v + 19*z1 + 6*z1*v + 6*z1*z2 + 2*z1*z2*v + 3*z1^2 + z1^2*v + 185/6*z0 + 6*z0*v + 11*z0*z2 + 2*z0*z2*v + 14*z0*z1 + 2*z0*z1*v + 2*z0*z1*z2 + z0*z1^2 + 19/2*z0^2 + z0^2*v + 2*z0^2*z2 + 2*z0^2*z1 + 2/3*z0^3 + 36*u + 8*u*v + 11*u*z2 + 2*u*z2*v + 14*u*z1 + 2*u*z1*v + 2*u*z1*z2 + u*z1^2 + 19*u*z0 + 2*u*z0*v + 4*u*z0*z2 + 4*u*z0*z1 + 2*u*z0^2 + 8*u^2 + 2*u^2*z2 + 2*u^2*z1 + 2*u^2*z0`.

### 28: `y|e|x|c`
Variables: `u, z0, z1, z2, v >= 0`; blocks `[['y'], ['e'], ['x'], ['c']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - z1 - 2`, `B=-u`, `C0=-u - z0 - z1 - z2 - 3`, `D=0`, `E=-u - z0 - 1`, `F=v + 1`
Polynomials: `N=22 + 6*v + 25/2*z1 + 7/2*z1*v + 3/2*z1^2 + 1/2*z1^2*v + 109/6*z0 + 7/2*z0*v + 15/2*z0*z1 + z0*z1*v + 1/2*z0*z1^2 + 9/2*z0^2 + 1/2*z0^2*v + z0^2*z1 + 1/3*z0^3 + 17*u + 3*u*v + 15/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 9*u*z0 + u*z0*v + 2*u*z0*z1 + u*z0^2 + 3*u^2 + u^2*z1 + u^2*z0`; `H=11 + 3*v + 19/2*z1 + 5/2*z1*v + 3/2*z1^2 + 1/2*z1^2*v + 67/6*z0 + 5/2*z0*v + 13/2*z0*z1 + z0*z1*v + 1/2*z0*z1^2 + 7/2*z0^2 + 1/2*z0^2*v + z0^2*z1 + 1/3*z0^3 + 10*u + 2*u*v + 13/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 7*u*z0 + u*z0*v + 2*u*z0*z1 + u*z0^2 + 2*u^2 + u^2*z1 + u^2*z0`; `L=11 + 3*v + 17/2*z1 + 5/2*z1*v + 3/2*z1^2 + 1/2*z1^2*v + 38/3*z0 + 5/2*z0*v + 13/2*z0*z1 + z0*z1*v + 1/2*z0*z1^2 + 4*z0^2 + 1/2*z0^2*v + z0^2*z1 + 1/3*z0^3 + 14*u + 3*u*v + 13/2*u*z1 + u*z1*v + 1/2*u*z1^2 + 8*u*z0 + u*z0*v + 2*u*z0*z1 + u*z0^2 + 3*u^2 + u^2*z1 + u^2*z0`.
Certificate H: `alpha=0, beta=0`; `R=11 + 3*v + 16*z1 + 4*z1*v + 3*z1^2 + z1^2*v + 46/3*z0 + 4*z0*v + 12*z0*z1 + 2*z0*z1*v + z0*z1^2 + 6*z0^2 + z0^2*v + 2*z0^2*z1 + 2/3*z0^3 + 13*u + 3*u*v + 12*u*z1 + 2*u*z1*v + u*z1^2 + 12*u*z0 + 2*u*z0*v + 4*u*z0*z1 + 2*u*z0^2 + 3*u^2 + 2*u^2*z1 + 2*u^2*z0`.
Certificate L: `alpha=0, beta=0`; `R=11 + 3*v + 13*z1 + 4*z1*v + 3*z1^2 + z1^2*v + 119/6*z0 + 4*z0*v + 12*z0*z1 + 2*z0*z1*v + z0*z1^2 + 15/2*z0^2 + z0^2*v + 2*z0^2*z1 + 2/3*z0^3 + 25*u + 6*u*v + 12*u*z1 + 2*u*z1*v + u*z1^2 + 15*u*z0 + 2*u*z0*v + 4*u*z0*z1 + 2*u*z0^2 + 6*u^2 + 2*u^2*z1 + 2*u^2*z0`.

### 29: `y|x|c|e`
Variables: `u, z0, z1, z2, v >= 0`; blocks `[['y'], ['x'], ['c'], ['e']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - 1`, `B=-u`, `C0=-u - z0 - z1 - 2`, `D=0`, `E=-u - z0 - z1 - z2 - 3`, `F=v + 1`
Polynomials: `N=11 + 3*v + 67/6*z0 + 5/2*z0*v + 7/2*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 10*u + 2*u*v + 7*u*z0 + u*z0*v + u*z0^2 + 2*u^2 + u^2*z0`; `H=3 + v + 31/6*z0 + 3/2*z0*v + 5/2*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 4*u + u*v + 5*u*z0 + u*z0*v + u*z0^2 + u^2 + u^2*z0`; `L=4 + v + 20/3*z0 + 3/2*z0*v + 3*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 8*u + 2*u*v + 6*u*z0 + u*z0*v + u*z0^2 + 2*u^2 + u^2*z0`.
Certificate H: `alpha=2, beta=0`; `R=22*z0 + 6*z0*v + 15*z0^2 + 3*z0^2*v + 2*z0^3 + 30*u + 9*u*v + 30*u*z0 + 6*u*z0*v + 6*u*z0^2 + 9*u^2 + 6*u^2*z0`.
Certificate L: `alpha=0, beta=0`; `R=1 + 53/6*z0 + 2*z0*v + 11/2*z0^2 + z0^2*v + 2/3*z0^3 + 14*u + 4*u*v + 11*u*z0 + 2*u*z0*v + 2*u*z0^2 + 4*u^2 + 2*u^2*z0`.

### 30: `y|x|e|c`
Variables: `u, z0, z1, z2, v >= 0`; blocks `[['y'], ['x'], ['e'], ['c']]`; strict gaps use `1+z_i`; `F=1+v`.
Endpoints: `A=-u - z0 - 1`, `B=-u`, `C0=-u - z0 - z1 - z2 - 3`, `D=0`, `E=-u - z0 - z1 - 2`, `F=v + 1`
Polynomials: `N=11 + 3*v + 67/6*z0 + 5/2*z0*v + 7/2*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 10*u + 2*u*v + 7*u*z0 + u*z0*v + u*z0^2 + 2*u^2 + u^2*z0`; `H=3 + v + 31/6*z0 + 3/2*z0*v + 5/2*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 4*u + u*v + 5*u*z0 + u*z0*v + u*z0^2 + u^2 + u^2*z0`; `L=4 + v + 20/3*z0 + 3/2*z0*v + 3*z0^2 + 1/2*z0^2*v + 1/3*z0^3 + 8*u + 2*u*v + 6*u*z0 + u*z0*v + u*z0^2 + 2*u^2 + u^2*z0`.
Certificate H: `alpha=2, beta=0`; `R=22*z0 + 6*z0*v + 15*z0^2 + 3*z0^2*v + 2*z0^3 + 30*u + 9*u*v + 30*u*z0 + 6*u*z0*v + 6*u*z0^2 + 9*u^2 + 6*u^2*z0`.
Certificate L: `alpha=0, beta=0`; `R=1 + 53/6*z0 + 2*z0*v + 11/2*z0^2 + z0^2*v + 2/3*z0^3 + 14*u + 4*u*v + 11*u*z0 + 2*u*z0*v + 2*u*z0^2 + 4*u^2 + 2*u^2*z0`.

## Independent exact replays

Polynomial/direct-ledger replay: `49152` exact value checks; coefficient identities had zero mismatches. Numeric spot checks: `142125` exact checks, all passed.
Round-32 closed-boundary `(0,3)` replay: `COUNT=70`, `ALL_GATE=True`, `ALL_H_L_ZERO=True`, `N_VALUES=[3]`, `INTERIOR_COUNT=0`.
Every one of the 70 rows has at least one equality face and no interior middle-third hit. Equality-event counts: `{'chain:c2<r': 8, 'chain:c3<r': 18, 'chain:c4<r': 24, 'chain:c5<r': 20, 'chain:r<c2': 8, 'chain:r<c3': 18, 'chain:r<c4': 24, 'chain:r<c5': 20, 'sibling:q<r': 70}`. Rebuilt-row SHA-256: `f63ffa11ced10fec42edc3c97d979144d75148372619bce21e1ad58aa14f1a91`.
The complete machine-readable list of all 70 rows, including every equality event, is in the JSON artifact.

## First precise obstruction for the literal four-clause gate

The exact gate-only witness is `Ip=[1,2], Iq=[0,1], Ir=[0,2]`. It satisfies `A<B, C0<D, E<F` and sibling overlap, but has `B>D`. Direct replay gives `N=3,H=L=0`; therefore `3H-N=3L-N=-3` while `N-3H=N-3L=3`. For any `alpha,beta>=0` and coefficientwise nonnegative `R`, the mandated right side is nonnegative, so neither branch identity can hold. This is the first algebraic obstruction and explains why this formal gate-only chamber is not admitted to the actual normalized atlas. It is also the first member of the 70 equality-face near-misses.

## Exhaustion proof

The relations p<q and p<r imply every legal p gap is no later than every legal q/r gap, hence B<=D and B<=F. Swapping q,r makes D<=F. The overlap gate max(C0,E)<=min(D,F) then reduces to E<=D, while C0<D and D<=F are already present. Translation by D gives the four-variable inequalities above. A finite weak-order pattern is an ordered partition of x,y,c,e respecting x>y; enumeration of all such partitions gives exactly the 31 listed rows. The level/slack construction is bijective, so no row is empty and no outside unrestricted row is admitted.

Labels: ledger identities and exhaustion are **PROVED-HERE** from the exact finite model and proved endpoint consequences; polynomial expansions, certificate coefficients, and replays are **COMPUTED** exact; the four-clause-only interpretation is **FAILED-AT** at the displayed witness.

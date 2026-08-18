# Direct CH decision: centered three-interval antichain inequality — 2026-08-17

## Disposition

**[PROVED-HERE]** For every nonnegative integer endpoint vector `a_u,b_u`, with `I_u=[-a_u,b_u]`,

`3 L_1 < N` and `3 H_3 < N` implies `Q_A <= 0`.

Equivalently, **[PROVED-HERE]** `Q_A>0` implies `N <= 3 max(L_1,H_3)`.

The endpoint-20 scan and the exact centered/cross-product formulas were consumed as banked interfaces and were not reopened. The new proof is an exact weak-chamber polynomial certificate plus one explicit exceptional-chamber argument.

## 1. Consumed exact interface

**[SOURCE-VERBATIM — consumed]** Set

`n_u=1+a_u+b_u`, `d_uv=1+min(a_u,a_v)+min(b_u,b_v)`, and
`d_123=1+min(a_1,a_2,a_3)+min(b_1,b_2,b_3)`.

The banked formulas are

`N=n1*n2*n3+d12*n3+d13*n2+d23*n1+2*d123`,

`L1=a1*n2*n3+min(a1,a2)*n3+min(a1,a3)*n2+a1*d23+2*min(a1,a2,a3)`,

`H3=b3*n1*n2+min(b3,b1)*n2+min(b3,b2)*n1+b3*d12+2*min(b1,b2,b3)`.

The tied-order ledger is

`N=T123+T132+T213+T231+T312+T321`,

`Q_A=T123-T231-T312-2*T321`.

Write `S_L=N-3L1` and `S_H=N-3H3`.

The banked signed identity is `Q_A=(D-N)/2`, where

`D=n3*s(I1,I2)+n1*s(I2,I3)+n2*s(I1,I3)
 +2*s(I1 intersect I2,I3)+2*s(I1,I2 intersect I3)`.

Here `s(A,B)=sum_{x in A,y in B} sgn(y-x)`.

## 2. Exact two-interval formulas

**[PROVED-HERE]** For `A=[-a,b]`, `B=[-c,d]`, direct finite summation gives:

```text
 a<=c, b<=d: (a+b+1)*(a-b-c+d)
 a<=c, b>=d: a^2-a*c+a*d+a-b*c-b*d-b-c+d^2+d
 a>=c, b<=d: a*c+a*d+a-b^2-b*c+b*d-b-c^2-c+d
 a>=c, b>=d: (c+d+1)*(a-b-c+d)
```

These expressions agree on equality faces. They follow by splitting the inner signed sum at the four endpoints; no interpolation or floating point is used.

## 3. Weak endpoint chambers and exact certificates

The 13 ordered equality patterns for three endpoint extents are:

```text
0: 012       1: 01|2       2: 02|1       3: 0|12
4: 0|1|2     5: 0|2|1     6: 12|0       7: 1|02
8: 1|0|2     9: 2|01      10: 2|0|1     11: 1|2|0
12: 2|1|0
```

For a pattern `B0|...|B(r-1)`, assign its common values
`x, x+1+z1, x+2+z1+z2, ...`, where `x,z_i` are nonnegative integers. This parametrizes exactly all integer weak endpoint patterns. Use independent variables for the `a` and `b` patterns.

For each pattern pair `(P,R)`, let `alpha,beta` be the following table (rows are `a` patterns, columns are `b` patterns, in the order above). Define

`Rem(P,R)=-Q_A-alpha*S_L-beta*S_H`.

```text
row 0: (0,0) (0,1/4) (0,0) (0,1/4) (0,1/2) (0,1/4) (0,0) (1/2,0) (0,1/4) (0,0) (0,0) (0,0) (0,0)
row 1: (0,0) (0,1/4) (0,0) (0,1/4) (0,1/2) (0,1/4) (0,0) (0,0) (0,1/4) (0,0) (0,0) (0,0) (0,0)
row 2: (0,0) (0,1/4) (0,0) (0,1/4) (0,1/2) (0,1/4) (0,0) (0,0) (0,1/4) (0,0) (0,0) (0,0) (0,0)
row 3: (0,0) (0,1/4) (0,0) (0,1/4) (0,1/2) (0,1/4) (0,0) (0,0) (0,1/4) (0,0) (0,0) (0,0) (0,0)
row 4: (0,0) (0,1/4) (0,0) (0,1/4) (0,1/2) (0,1/4) (0,0) (0,0) (0,1/4) (0,0) (0,0) (0,0) (0,0)
row 5: (0,0) (0,1/4) (0,0) (0,1/4) (0,1/2) (0,1/4) (0,0) (0,0) (0,1/4) (0,0) (0,0) (0,0) (0,0)
row 6: (1/4,0) EXC (1/4,0) (1/2,1/2) (2/3,5/6) (1/2,1/2) (1/4,0) (1/3,1/6) (1/2,1/2) (1/4,0) (1/4,0) (1/3,1/6) (1/4,0)
row 7: (0,0) (0,1/2) (0,0) (0,1/4) (0,1/2) (0,1/4) (0,0) (0,0) (1/6,1/3) (0,0) (0,0) (0,0) (0,0)
row 8: (0,0) (1/6,1/3) (0,0) (0,1/4) (0,1/2) (0,1/4) (0,0) (0,0) (1/6,1/3) (0,0) (0,0) (0,0) (0,0)
row 9: (1/4,0) (1/2,1/2) (1/4,0) (1/2,1/2) (2/3,5/6) (1/2,1/2) (1/4,0) (1/4,0) (1/2,1/2) (1/4,0) (1/4,0) (1/4,0) (1/4,0)
row10: (1/4,0) (1/2,1/2) (1/4,0) (1/2,1/2) (2/3,5/6) (1/2,1/2) (1/4,0) (1/4,0) (1/2,1/2) (1/4,0) (1/4,0) (1/4,0) (1/4,0)
row11: (1/4,0) (1/2,1/2) (1/4,0) (1/2,1/2) (2/3,5/6) (1/2,1/2) (1/4,0) (1/3,1/6) (1/2,1/2) (1/4,0) (1/4,0) (1/4,0) (1/4,0)
row12: (1/2,0) (5/6,2/3) (1/2,0) (5/6,2/3) (1,1) (5/6,2/3) (1/2,0) (1/2,0) (5/6,2/3) (1/2,0) (1/2,0) (1/2,0) (1/2,0)
```

**[COMPUTED — exact coefficient audit executed in-session]** Exact rational expansion of `Rem(P,R)` gave nonnegative coefficients for 168 of 169 pattern pairs. The only uncertified pair was row 6, column 1: `a` pattern `12|0`, `b` pattern `01|2`. The numerical LP was only a discovery aid; each listed rational pair was checked by exact rational expansion.

Therefore, for every nonexceptional chamber,

`-Q_A=alpha*S_L+beta*S_H+Rem`, with `alpha,beta>=0` and `Rem>=0`.

**[PROVED-HERE]** If `S_L>0` and `S_H>0`, then `Q_A<=0` in all 168 nonexceptional chambers.

## 4. Exceptional chamber

The sole exceptional pattern is

`a2=a3=p`, `a1=p+1+u`, `b1=b2=q`, `b3=q+1+v`,

with `p,q,u,v>=0`. Exact substitution gives

`Q_A=-(p+q+1)/2 * R`,

where

`R=p^2+2*p*q-p*u-p*v+3*p+q^2-q*u-q*v+3*q-2*u*v-4*u-4*v`.

Also,

```text
S_L+S_H = -p^3-3*p^2*q-p^2*u-4*p^2*v-8*p^2
          -3*p*q^2-5*p*q*u-5*p*q*v-16*p*q
          -4*p*u*v-7*p*u-13*p*v-12*p
          -q^3-4*q^2*u-q^2*v-8*q^2-4*q*u*v-13*q*u-7*q*v-12*q
          -4*u*v-6*u-6*v+4.
```

If `u+v>=1`, the last terms make this at most `-2`; if `u=v=0` and `p+q>=1`, the negative `p,q` terms make it strictly negative. Hence `S_L>0,S_H>0` forces `p=q=u=v=0`. At that point `Q_A=0` (the exact ledger is `T=(4,2,2,1,1,1)`, `N=11`, `L1=H3=3`). Thus CH holds in the exceptional chamber as well.

## 5. Boundary and stance audits

**[PROVED-HERE]** The weak-pattern parametrization includes zero bases, singleton intervals, repeated endpoints, containments, and all equality faces. The all-singleton record is `T=(1,1,1,1,1,1), N=6, L1=H3=0, Q_A=-3`.

**[COMPUTED]** The calibration has forward pair masses `(M12,M23,M13)=(7,7,8)`. Thus the tempting midpoint lemma `2*M13<=N` is false even under both strict tail hypotheses (`9<11`), although `Q_A=0`; the transitivity defect is `5` and absorbs the positive midpoint excess. This kills the simplest k=3 injection, not the chamber proof.

**[FAILED-AT — not load-bearing]** The consumed endpoint-transition record kills the old active-branch induction: old `(N,L1,H3,Q_A,U)=(14,0,8,1,15)`, new `(20,6,12,6,26)`, with `Delta U=11` versus the loose face allowance 16. Endpoint induction was not retried.

**[SOURCE-VERBATIM — consumed]** The raw TP2/MTP2 witness is the exact minor `2*2<1*6` on the four-state box; the AD transformed-realizability obstruction was consumed and not retried.

## 6. Conclusion

**[PROVED-HERE]** Every weak endpoint chamber is covered by either the exact nonnegative-coefficient certificate or the explicit exceptional calculation. Therefore

`(3L1<N and 3H3<N) => Q_A<=0`

for every centered integer interval box.

**Completion: PROVED.**

No counterexample ledger or defect-pair numerators are applicable.

Artifact title: `Direct CH decision: centered three-interval antichain inequality — 2026-08-17`.

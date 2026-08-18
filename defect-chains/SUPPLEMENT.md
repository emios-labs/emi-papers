# Supplement: the banked derivations
## The Two- and Three-Defect Chain Theorems

This document accompanies the paper and contains, VERBATIM, the durable proof records
behind every theorem the paper states at citation level. Each record was banked by the
research harness at proof time and is reproduced here without editing; the paper's
theorem statements are projections of these records. Labels inside the records
([PROVED-HERE], [ARGUED], [COMPUTED], [FAILED-AT]) are the original at-proof-time
audit labels; [COMPUTED] items are corroborating finite checks, never premises.
Certificate corpora referenced by SHA-256 ship in the same repository (see SHA256SUMS).

Theorem numbering follows the paper (draft of 2026-08-18).

---


# Theorem 8.1 (Strong order)

---

## Banked record: `closed-third-strong-order-rigidity`

# closed-third-strong-order-rigidity

title: Closed-third Strong-Order Rigidity
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Use the pointwise implication 1_{u<v}+1_{v<w}\le1+1_{u<w}, complementarity of incomparable orientations, and the closed-third dichotomy.
[graph-node: kgn_32f15269de96 — this page is a PROJECTION; truth lives in the research KG]

## Statement

Assume every incomparable pair u,v of a finite poset P has orientation probability outside the closed interval [1/3,2/3]. Defining u\prec v when Pr(u<_L v)>2/3 yields a strict total order extending P. If u\prec v and v\prec w, then Pr(u<_L w)\ge Pr(u<_L v)+Pr(v<_L w)-1>1/3; the avoidance hypothesis upgrades this to Pr(u<_L w)>2/3 whenever u and w are incomparable, while comparable cases are forced by P.

## Content

Assume every incomparable pair u,v of a finite poset P has orientation probability outside the closed interval [1/3,2/3]. Defining u\prec v when Pr(u<_L v)>2/3 yields a strict total order extending P. If u\prec v and v\prec w, then Pr(u<_L w)\ge Pr(u<_L v)+Pr(v<_L w)-1>1/3; the avoidance hypothesis upgrades this to Pr(u<_L w)>2/3 whenever u and w are incomparable, while comparable cases are forced by P.

## Provenance

- supervisor | work_b0645a21fc07 | banked per finding at effort end



---

## Banked record: `corrected-strong-order-theorem-under-closed-third-avoidance`

# corrected-strong-order-theorem-under-closed-third-avoidance

title: Corrected Strong-Order Theorem Under Closed-Third Avoidance
type: claim | label: mixed | verification: unverified
namespace: third23
mechanism: Totality follows because complementary orientation probabilities sum to one and the forbidden closed interval forces exactly one direction above 2/3. Transitivity follows from the union bound: two events each having probability greater than 2/3 intersect with probability greater than 1/3, and their intersection implies the endpoint ordering. The adjacent-pair conclusion follows because if every adjacent strong-order pair were comparable in the poset, the strong order would coincide with a chain order.
[graph-node: kgn_c87861396ce4 — this page is a PROJECTION; truth lives in the research KG]

## Statement

For a finite poset whose incomparable-pair orientation probabilities avoid the closed interval [1/3, 2/3], the relation u ≺ v defined by Pr(u<v)>2/3 is a strict total order extending the poset order. If the poset is not a chain, at least one adjacent pair in this strong order is incomparable in the poset. The entry also records computed finite ledgers and isolates one mathematically inconsistent charge detail as failed.

## Content

# Corrected Strong-Order Theorem Under CLOSED-THIRD Avoidance — Independent Verification

# Corrected Strong-Order Theorem Under CLOSED-THIRD Avoidance

**Campaign:** THIRD23 Round 12  
**Date:** 2026-08-17  
**Status:** The closed-third strong-order theorem and its adjacent-pair consequence are **PROVED-HERE**. The finite ledgers are **COMPUTED**. One literal detail in the charge is mathematically inconsistent; it is isolated and marked **FAILED** rather than silently changed.

## 1. Exact statement, scope, and notation

Let \(P\) be a finite poset on \(X\), let \(\mathcal L(P)\) be its set of linear extensions, and put
\[
N=e(P)=|\mathcal L(P)|\ge 1.
\]
For distinct \(u,v\), write
\[
\Pr(u<v):=\frac{|\{L\in\mathcal L(P):u<_{L}v\}|}{N}.
\]
Here \(u<_{L}v\) means that \(u\) occurs before \(v\) in the total order \(L\). This is exactly the probability interface in the pool-verified artifact `linear-extensions-and-pair-probability`.

The hypothesis used here is the **closed-third avoidance** condition
\[
\tag{H\_closed}
\Pr(u<v)\notin[1/3,2/3]
\quad\text{for every orientation of every incomparable pair }\{u,v\}.
\]
Equivalently, for each such orientation,
\[
\Pr(u<v)<1/3\quad\text{or}\quad \Pr(u<v)>2/3.
\]
For a comparable pair, if \(u<_P v\), every linear extension has \(u<_{L}v\), so \(\Pr(u<v)=1\) and \(\Pr(v<u)=0\).

Define, for distinct elements,
\[
 u\prec v\quad\Longleftrightarrow\quad \Pr(u<v)>2/3,
\]
and declare \(u\not\prec u\). The theorem is:

> **[PROVED-HERE] Corrected strong-order theorem.** Under \((H_{\rm closed})\), \(\prec\) is a strict total order on \(X\) extending the strict order of \(P\). If \(P\) is not a chain, some adjacent pair in the \(\prec\)-order is \(P\)-incomparable.

No triple-event hypothesis is needed for this order theorem or for the adjacent-pair conclusion conditional on “\(P\) is not a chain.” If the campaign’s separate H2 is the existence of a pairwise-incomparable triple with an event \(\Pr(x<y<z)>1/3\), that H2 is outside the proof below; the proof only uses the two strict-majority inequalities when checking transitivity. No balance theorem, heavy-gap theorem, or two-defect theorem is asserted here.

## 2. Authorized uniform-gap dependencies (cited, not re-proved)

The proof of the order theorem is pair-probabilistic and does not need the gap decomposition. The uniform-gap framework is nevertheless recorded at its exact permitted interface:

* **[ARGUED — imported dependency, not re-proved here]** `uniform_gap_map_bijection_and_weight_identity` supplies the canonical bijection between linear extensions and feasible isotone gap maps relative to a fixed chain, the block decomposition of each fiber, and
  \[
  W(g)=\prod_r e(Q_r),\qquad e(P)=\sum_{g\in\mathcal G}W(g).
  \]
* **[ARGUED — imported dependency, not re-proved here]** `uniform_gap_exact_tied_event_formulas` supplies the exact tied-fiber numerator
  \[
  \#\{L\in\mathcal L_g(P):u<_{L}v\}
  =e(Q_r;u<v)\prod_{s\ne r}e(Q_s)
  \quad\text{when }g(u)=g(v)=r,
  \]
  together with the exact chain-cut formula
  \[
  \#\{L:x<_{L}c_t\}
  =\sum_{g:g(x)<t}W(g).
  \]
  These formulas make no symmetry assumption for a tied block. They are cited only; their proofs are not repeated here.
* **[ARGUED — imported definition]** `linear-extensions-and-pair-probability` identifies each probability with the corresponding linear-extension count divided by \(N\), and uses the fact that every linear extension totally orders each distinct pair.

The boundary computation in Section 6 also has a gap ledger, but the main theorem does not infer any strict inequality from a gap formula.

## 3. Totality and extension of \(P\)

**[PROVED-HERE]** Fix distinct \(u,v\).

If \(u<_P v\), then \(u<_{L}v\) in every linear extension, hence \(\Pr(u<v)=1>2/3\), so \(u\prec v\). If \(v<_P u\), the reverse orientation is the one with probability one, so \(v\prec u\).

Now suppose \(u\parallel_P v\). Since every \(L\in\mathcal L(P)\) is a total order, exactly one of \(u<_{L}v\) and \(v<_{L}u\) holds. Thus the two events are disjoint and exhaustive, and
\[
\Pr(u<v)+\Pr(v<u)=1. \tag{3.1}
\]
This is the required antisymmetry/asymmetry fact for linear extensions.

By \((H_{\rm closed})\), \(\Pr(u<v)\) is either below \(1/3\) or above \(2/3\). In the first case (3.1) gives \(\Pr(v<u)>2/3\); in the second, \(u\prec v\). The boundary values \(1/3\) and \(2/3\) are not permitted. Therefore exactly one of \(u\prec v\) and \(v\prec u\) holds for every distinct incomparable pair. Both directions cannot hold because their events are disjoint (and, in any event, their probabilities cannot both exceed \(2/3\)).

Consequently \(\prec\) is irreflexive and total on distinct elements, and it extends \(P\). It remains only to prove transitivity.

## 4. Complete transitivity proof and case audit

Assume
\[
 x\prec y\quad\text{and}\quad y\prec z.
\]
Let
\[
 A=\{L:x<_{L}y\},\qquad B=\{L:y<_{L}z\}.
\]
The two hypotheses give \(|A|>2N/3\) and \(|B|>2N/3\). Applying the union bound to the complements gives
\[
\begin{aligned}
 |A\cap B|
 &=N-|A^c\cup B^c|\\
 &\ge N-|A^c|-|B^c|\\
 &=|A|+|B|-N\\
 &>\frac{2N}{3}+\frac{2N}{3}-N
 =\frac N3. \tag{4.1}
\end{aligned}
\]
Every member of \(A\cap B\) has \(x<_{L}y<_{L}z\), and transitivity of the total order \(L\) gives \(x<_{L}z\). Hence
\[
\#\{L:x<_{L}z\}>N/3,
\qquad\text{i.e.}\qquad \Pr(x<z)>1/3. \tag{4.2}
\]
If \(x=z\), the strict event \(x<_{L}z\) is empty, contradicting (4.2); so the endpoint pair is distinct, as required for a strict relation.

The following dispatch is exhaustive.

### 4.1 Reverse comparabilities on the two assumed edges

* If \(y<_P x\), then no linear extension has \(x<_{L}y\), so \(A=\varnothing\), contradicting \(x\prec y\).
* If \(z<_P y\), then no linear extension has \(y<_{L}z\), so \(B=\varnothing\), contradicting \(y\prec z\).

Thus the first assumed edge is either \(x<_P y\) or \(x\parallel_P y\), and the second is either \(y<_P z\) or \(y\parallel_P z\). These are the four possible premise configurations:

\[
\begin{array}{c|c|c}
\text{first edge}&\text{second edge}&\text{endpoint consequences}\\ \hline
x<_P y&y<_P z&x<_P z\text{ by transitivity of }P\\
x<_P y&y\parallel_P z&z<_P x\text{ would imply }z<_P y;\text{ so }x<_P z\text{ or }x\parallel_P z\\
x\parallel_P y&y<_P z&z<_P x\text{ would imply }y<_P x;\text{ so }x<_P z\text{ or }x\parallel_P z\\
x\parallel_P y&y\parallel_P z&x<_P z,\ z<_P x,\text{ or }x\parallel_P z\text{ are all initially possible.}
\end{array}
\tag{4.3}
\]
The first row is already settled: \(x<_P z\), so \(\Pr(x<z)=1\) and \(x\prec z\). The remaining rows are dispatched by the endpoint comparison below; the table explicitly includes every forced/incomparable combination of the two assumed edges.

### 4.2 Every possible endpoint comparison \(x\) versus \(z\)

* **[PROVED-HERE] Forward endpoint, \(x<_P z\).** Every linear extension has \(x<_{L}z\), so \(\Pr(x<z)=1>2/3\), and therefore \(x\prec z\). This covers this endpoint in every row of (4.3), including all cases where one or both assumed edges are incomparable.

* **[PROVED-HERE] Reverse endpoint, \(z<_P x\).** Every linear extension has \(z<_{L}x\), so the event \(x<_{L}y<_{L}z\) is impossible: its intersection \(A\cap B\) is empty. This contradicts the strict lower bound \(|A\cap B|>N/3\) in (4.1). Thus the requested endpoint case \(z<_P x\) is dispatched by the event/intersection argument, not by an informal appeal to transitivity.

* **[PROVED-HERE] Incomparable endpoint, \(x\parallel_P z\).** Equation (4.2) gives \(\Pr(x<z)>1/3\). Closed-third avoidance says this probability is either strictly below \(1/3\) or strictly above \(2/3\). The former is impossible by (4.2), and equality at \(1/3\) is explicitly excluded. Hence \(\Pr(x<z)>2/3\), so \(x\prec z\).

Together with the reverse-edge exclusions, (4.3), and the three endpoint cases, this handles \(x<_P y\), \(y<_P z\), \(x<_P z\), all reverse comparabilities, and every incomparable endpoint configuration. Therefore \(\prec\) is transitive. Along with irreflexivity and totality, this proves that \(\prec\) is a strict total order extending \(P\).

## 5. Adjacent \(P\)-incomparable pair

**[PROVED-HERE]** List the elements in their \(\prec\)-order:
\[
 m_1\prec m_2\prec\cdots\prec m_n.
\]
Assume for contradiction that every adjacent pair \(\{m_i,m_{i+1}\}\) is \(P\)-comparable. Because \(\prec\) extends \(P\), the comparable direction cannot be \(m_{i+1}<_P m_i\): that would force \(m_{i+1}\prec m_i\), contrary to the displayed \(\prec\)-order. Therefore
\[
 m_i<_P m_{i+1}\qquad (1\le i<n).
\]
Transitivity of \(P\) now gives \(m_i<_P m_j\) for every \(i<j\). Thus every pair is comparable in \(P\), so \(P\) is a chain, contradicting the hypothesis that \(P\) is not a chain. Hence, whenever \(P\) is not a chain, at least one adjacent pair in the strict total order \(\prec\) is \(P\)-incomparable.

This is a pure consequence of “strict total order extending \(P\)”; no probability estimate beyond the strong-order theorem is used in the adjacent-pair step.

## 6. Independently recomputed open-third boundary ledger

Here “OPEN-third avoidance” means avoidance of the open interval
\[
(1/3,2/3),
\]
so the boundary values \(1/3\) and \(2/3\) are allowed. Strict-majority totality uses the stricter relation \(uMv\iff\Pr(u<v)>2/3\); at probabilities exactly \(1/3\) and \(2/3\), neither direction is in \(M\).

### 6.1 Literal four-element chain-plus-isolated-poset in the charge

The literal requested poset is
\[
 a<_P b<_P c,
 \qquad d\parallel_P a,b,c.
\]
Its four linear extensions, independently enumerated, are
\[
 dabc,\quad adbc,\quad abdc,\quad abcd
\]
(the same set as `['abcd', 'abdc', 'adbc', 'dabc']` in lexicographic output). The exact relevant ledger is
\[
\begin{array}{c|cc|cc}
\text{pair}&\#(u<d)&\Pr(u<d)&\#(d<u)&\Pr(d<u)\\ \hline
 a,d&3&3/4&1&1/4\\
 b,d&2&1/2&2&1/2\\
 c,d&1&1/4&3&3/4
\end{array}
\]
The chain pairs \(a,b\), \(b,c\), and \(a,c\) have probability one in the displayed chain direction.

**[COMPUTED]** The persisted run `outputs/corrected-strong-order-theorem/open_ledger.py` returned, among other exact lines,
```
literal_chain_plus_isolated
extensions ['abcd', 'abdc', 'adbc', 'dabc']
N 4
a<d: counts 3,1; probabilities 3/4,1/4
b<d: counts 2,2; probabilities 1/2,1/2
c<d: counts 1,3; probabilities 1/4,3/4
literal_denominator_can_equal_thirds []
literal_open_middle_third_avoidance False
```
Thus this literal poset **fails** OPEN-third avoidance because \(\Pr(b<d)=\Pr(d<b)=1/2\in(1/3,2/3)\). Also, since \(N=4\), every probability is \(k/4\), and no \(k/4\) equals \(1/3\) or \(2/3\); the exact requested boundary values cannot occur in this four-extension model.

**[FAILED — exact stall for the literal ledger request]** The phrase “the four-element poset consisting of a 3-chain \(a<b<c\) and isolated \(d\)” cannot at the same time demand exact \(1/3\) and \(2/3\) orientation probabilities under the cited uniform-linear-extension definition. Direct enumeration gives the four extensions and the \(1/2\) middle orientation above, while denominator arithmetic rules out \(1/3\) and \(2/3\). I therefore do not mislabel this poset as an OPEN-third boundary witness.

### 6.2 Recovered exact boundary witness from the existing banked ledger

The existing artifact **“Majority Relation: Open-Third Boundary Audit”** contains the actual four-element boundary witness:
\[
 X=\{r,a,b,c\},
 \qquad r<_P a<_P b,
 \qquad r<_P c,
\]
with no further comparabilities. Thus \(a\parallel_P c\) and \(b\parallel_P c\). This is a 3-element two-chain-plus-isolated block with a new least element, not a 3-chain plus an isolated element.

Its complete set of linear extensions is
\[
 rabc,\qquad racb,\qquad rcab,
 \qquad N=3.
\]
The exact orientation table is
\[
\begin{array}{c|cc|cc}
\text{pair}&\#(u<v)&\Pr(u<v)&\#(v<u)&\Pr(v<u)\\ \hline
 r,a&3&1&0&0\\
 r,b&3&1&0&0\\
 r,c&3&1&0&0\\
 a,b&3&1&0&0\\
 a,c&2&2/3&1&1/3\\
 b,c&1&1/3&2&2/3
\end{array}
\]
Therefore every incomparable orientation avoids the OPEN interval \((1/3,2/3)\), but the exact boundary values are allowed. CLOSED-third avoidance fails. The strict-majority relation is exactly
\[
 M=\{rMa,rMb,rMc,aMb\},
\]
and neither orientation of \(\{a,c\}\) nor of \(\{b,c\}\) belongs to \(M\). Strict-majority totality therefore fails at the first conclusion.

The event used in the existing audit is also exact:
\[
 \#\{L:r<_{L}a<_{L}c\}=2,
 \qquad \Pr(r<a<c)=2/3>1/3.
\]

Relative to the maximum chain \(C=(r<a<b)\), the defect \(c\) has gaps
\[
\begin{array}{c|c|c}
L&g(c)&W(g)\\ \hline
rabc&3&1\\
racb&2&1\\
rcab&1&1
\end{array}
\]
so the fiber weights sum to \(1+1+1=3=N\). The exact chain cuts are
\[
\#(c<a)=1,
\qquad \#(c<b)=2,
\]
matching the \(1/3\) and \(2/3\) entries. This is the recovered boundary ledger, and it is consistent with the cited gap-map, fiber-weight, tied-event, and chain-cut interfaces.

**[COMPUTED]** The persisted run `outputs/corrected-strong-order-theorem/open_ledger.py` returned exactly
```
recovered_boundary_witness_r<a<b_and_r<c
extensions ['rabc', 'racb', 'rcab']
N 3
a<c: counts 2,1; probabilities 2/3,1/3
b<c: counts 1,2; probabilities 1/3,2/3
boundary_open_middle_third_avoidance True
boundary_closed_middle_third_avoidance False
boundary_strict_majority_edges [('r', 'a'), ('r', 'b'), ('r', 'c'), ('a', 'b')]
boundary_event_r<a<c 2 2/3
boundary_gap_ledger [('rabc', 3), ('racb', 2), ('rcab', 1)]
denominator_4_exact_thirds []
```
This independently recovers the decisive exact boundary ledger already banked under **“Majority Relation: Open-Third Boundary Audit.”**

### 6.3 Finite audit of the discrepancy and theorem at four elements

**[COMPUTED — sanity check only, not a proof of the general theorem]** Exhausting all \(3^6\) possible orientations/omissions of the six unordered pairs on four labeled elements, retaining the transitive relations, gave 219 labeled posets. The persisted output `outputs/corrected-strong-order-theorem/exhaustive_four_posets.stdout.txt` records
```
labeled_posets_on_4 219
open_avoiders 72
open_avoiders_with_strict_majority_missing_pair 48
closed_avoiders 24
open_failure_extension_histogram {3: 48}
literal_chain_plus_isolated_in_open_avoiders False
literal_b_vs_d_probability 1/2
```
A separate persisted check of all 219 labeled four-element posets returned
```
labeled_posets_on_4 219
closed_avoiding_cases_n4 24
closed_avoidance_theorem_failures_n4 0
boundary_witness_extensions ['rabc', 'racb', 'rcab']
a<c 2 2/3
b<c 1 1/3
k_over_4_equal_1_or_2_over_3 []
```
These computations corroborate, but do not replace, the proof in Sections 3–5.

## 7. Final status and audit flags

* **[PROVED-HERE]** Closed-third avoidance \(\Pr(u<v)\notin[1/3,2/3]\) for every incomparable orientation makes the relation \(u\prec v\iff\Pr(u<v)>2/3\) a strict total order extending \(P\). The transitivity proof uses the strict union-bound lower bound \(\Pr(x<y<z)>1/3\), and explicitly dispatches \(z<_P x\) as impossible.
* **[PROVED-HERE]** Any strict total order extending a non-chain finite poset has an adjacent \(P\)-incomparable pair.
* **[COMPUTED]** The actual four-element OPEN-third boundary witness is \(r<_P a<_P b\) together with \(r<_P c\), with three extensions and exact \(1/3,2/3\) orientations.
* **[FAILED — exact stall stated in Section 6.1]** The additionally specified “3-chain \(a<b<c\) plus isolated \(d\)” has four extensions and probabilities \(1/4,1/2,3/4\), not exact \(1/3,2/3\), and it does not satisfy OPEN-third avoidance. The two descriptions must not be conflated.

The artifact proves only the corrected strong-order/adjacency statement and records the boundary audit. It does not prove the global 1/3–2/3 conjecture or any balance, concentration, or two-defect theorem.


---
provenance: actor=work_math_manager_streaming work_id=work_c08a464d5b8b node_id=strong_order_closed_avoidance_independent_verification banked=2026-08-17T07:31:28Z

## Edges

- conditional-V-Lambda-three-chain-distinct-heavy-exclusion-recovery (kgn_0e5494ada788) -depends_on-> this
- Conditional V–Lambda–Three-Chain Distinct-Heavy Exclusion (kgn_b64db58c8f39) -depends_on-> this

## Provenance

- work_math_manager_streaming | work_c08a464d5b8b | strong_order_closed_avoidance_independent_verification | imported from wiki entry corrected-strong-order-theorem-under-closed-third-avoidance




# Theorem 8.4 (Heavy-gap rigidity)

---

## Banked record: `maximum-chain-heavy-gap-rigidity`

# maximum-chain-heavy-gap-rigidity

title: Maximum-chain Heavy-gap Rigidity
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Apply the monotone cumulative chain-cut counts, with virtual endpoint cuts and direct treatment of singleton windows, to force one jump carrying more than N/3 while excluding mass in either strict tail from reaching N/3.
[graph-node: kgn_abc85041c93d — this page is a PROJECTION; truth lives in the research KG]

## Statement

Let C be a maximum chain, let N=e(P), and assume closed-third avoidance for every incomparable pair. For each defect u, define μ_u(r)=\sum_{g:g(u)=r}W(g). Then there is a unique legal gap ρ_u with μ_u(ρ_u)>N/3, and both strict tails satisfy \sum_{r<ρ_u}μ_u(r)<N/3 and \sum_{r>ρ_u}μ_u(r)<N/3. The conclusion includes endpoint gaps, singleton legal windows, and equality at the closed-third boundaries.

## Content

Let C be a maximum chain, let N=e(P), and assume closed-third avoidance for every incomparable pair. For each defect u, define μ_u(r)=\sum_{g:g(u)=r}W(g). Then there is a unique legal gap ρ_u with μ_u(ρ_u)>N/3, and both strict tails satisfy \sum_{r<ρ_u}μ_u(r)<N/3 and \sum_{r>ρ_u}μ_u(r)<N/3. The conclusion includes endpoint gaps, singleton legal windows, and equality at the closed-third boundaries.

## Provenance

- supervisor | work_b0645a21fc07 | banked per finding at effort end



---

## Banked record: `heavy-gap-rigidity-under-closed-third-avoidance`

# heavy-gap-rigidity-under-closed-third-avoidance

title: Heavy-Gap Rigidity Under Closed-Third Avoidance
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Monotonicity of the CDF forces a unique first crossing from below 1/3 to above 2/3; the jump is the heavy atom, and the boundary values give the strict tail bounds.
[graph-node: kgn_61fdce45cbe7 — this page is a PROJECTION; truth lives in the research KG]

## Statement

Assume instead that every relevant chain-cut probability avoids the closed interval [1/3,2/3], equivalently every such probability is strictly below 1/3 or strictly above 2/3. For a fixed maximum chain and off-chain element x, let F(t)=Pr(G_x<t), with F=0 and F=1 at the legal-window boundaries. Then there is a unique gap r such that Pr(G_x=r)>1/3, and both outside tails satisfy Pr(G_x<r)<1/3 and Pr(G_x>r)<1/3. The argument includes singleton windows, zero-mass gaps, endpoint gaps, and jumps at either endpoint.

## Content

Assume instead that every relevant chain-cut probability avoids the closed interval [1/3,2/3], equivalently every such probability is strictly below 1/3 or strictly above 2/3. For a fixed maximum chain and off-chain element x, let F(t)=Pr(G_x<t), with F=0 and F=1 at the legal-window boundaries. Then there is a unique gap r such that Pr(G_x=r)>1/3, and both outside tails satisfy Pr(G_x<r)<1/3 and Pr(G_x>r)<1/3. The argument includes singleton windows, zero-mass gaps, endpoint gaps, and jumps at either endpoint.

## Edges

- corrected-antichain-distinct-heavy-index-exclusion-derivation (kgn_53d7a783f9a8) -depends_on-> this
- distinct-heavy-tail-or-pair-frontier-recovery-failed-at (kgn_ffcbc9dd8800) -depends_on-> this
- conditional-V-Lambda-three-chain-distinct-heavy-exclusion-recovery (kgn_0e5494ada788) -depends_on-> this
- Conditional V–Lambda–Three-Chain Distinct-Heavy Exclusion (kgn_b64db58c8f39) -depends_on-> this
- Corrected V/Lambda Three-Defect Foundation Audit (kgn_af072f7e8e57) -depends_on-> this

## Provenance

- supervisor | work_c08a464d5b8b | banked per finding at effort end




# Theorem 8.5 (Heavy-gap alignment)

---

## Banked record: `heavy-gap-alignment-corollary-under-closed-third-avoidance`

# heavy-gap-alignment-corollary-under-closed-third-avoidance

title: Heavy-gap alignment corollary under closed-third avoidance
type: claim | label: proved | verification: unverified
namespace: third23
[graph-node: kgn_cafbf5b0f587 — this page is a PROJECTION; truth lives in the research KG]

## Statement

Let P be finite, C=(c_1<...<c_m) a maximum chain, D=P\C, R=P[D], and assume every incomparable-pair orientation probability avoids the closed interval [1/3,2/3]. For each defect x let rho_x be its unique heavy gap, with mu_x(rho_x)>N/3 and both strict tails below N/3. Then rho_u<rho_v implies v is not <_R u. Moreover, if u and v are incomparable in R, then Pr(u<v)>2/3.

## Content

Recovered verbatim in substance from the completed artifact `heavy-gap-alignment-corollary-under-closed-third-avoidance`. Put a=rho_u<b=rho_v. If v<_R u, isotonicity gives G_v<=G_u in every extension, hence {G_v=b} subset {G_u>=b} subset {G_u>a}; therefore mu_v(b)<=Up_u<N/3, contradicting mu_v(b)>N/3. If u||_R v, then {v<u} subset {G_u>a} union {G_v<b}, so Pr(v<u)<2/3. Closed-third avoidance excludes both boundary values and forces Pr(v<u)<1/3, hence Pr(u<v)>2/3. Tied fibers cause no issue because on the complement one has G_u<=a<b<=G_v, a strict gap inequality. All inequalities are strict: equality at N/3 or 2N/3 is excluded by the closed-third hypothesis and the imported heavy-gap theorem. Endpoint heavy gaps rho=0,m use empty strict tails; no fictitious c_0 or c_{m+1} is invoked. No weaker correction is needed.

## Provenance

- agent | kg bank



---

## Banked record: `heavy-gap-probabilistic-alignment`

# heavy-gap-probabilistic-alignment

title: Heavy-Gap Probabilistic Alignment
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: The event {v<u} is contained in {G_u>\rho_u}\cup{G_v<\rho_v}, whose probability is strictly below 2/3. Closed-third avoidance then forces \Pr(v<u)<1/3, hence \Pr(u<v)>2/3.
[graph-node: kgn_6985e3d16fef — this page is a PROJECTION; truth lives in the research KG]

## Statement

Under the hypotheses of the maximum-chain unique-heavy-gap theorem, if \rho_u<\rho_v and u\parallel_R v, then \Pr(u<v)>2/3.

## Content

Under the hypotheses of the maximum-chain unique-heavy-gap theorem, if \rho_u<\rho_v and u\parallel_R v, then \Pr(u<v)>2/3.

## Provenance

- supervisor | work_e1226b1a6d4b | banked per finding at effort end




# Propositions 9.1-9.2 (Shape classification; three-chain reduction)

---

## Banked record: `three-defect-order-shape-classification`

# three-defect-order-shape-classification

title: Three-Defect Order-Shape Classification
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Classification by the number and transitive closure of comparabilities among three elements.
[graph-node: kgn_b8194f030ddd — this page is a PROJECTION; truth lives in the research KG]

## Statement

Up to order duality, the order induced by three off-chain elements has exactly four shapes relevant to the reduction atlas: the three-element antichain A, the one-relation poset Q, the V shape (including its dual Λ), and the three-element chain T.

## Content

Up to order duality, the order induced by three off-chain elements has exactly four shapes relevant to the reduction atlas: the three-element antichain A, the one-relation poset Q, the V shape (including its dual Λ), and the three-element chain T.

## Provenance

- supervisor | work_baac3d58cfc2 | banked per finding at effort end



---

## Banked record: `three-chain-defect-width-two-reduction`

# three-chain-defect-width-two-reduction

title: Three-Chain Defect Width-Two Reduction
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: The displayed partition is an explicit cover by two chains.
[graph-node: kgn_1e9cf47b59b3 — this page is a PROJECTION; truth lives in the research KG]

## Statement

If the three off-chain elements induce x<y<z, then P is the union of the two chains C and {x<y<z}. Hence P has an explicit two-chain cover, so the source-verbatim width-at-most-two balance theorem applies to this branch.

## Content

If the three off-chain elements induce x<y<z, then P is the union of the two chains C and {x<y<z}. Hence P has an explicit two-chain cover, so the source-verbatim width-at-most-two balance theorem applies to this branch.

## Provenance

- supervisor | work_baac3d58cfc2 | banked per finding at effort end



---

## Banked record: `strict-reduction-atlas-for-three-chain-defects`

# strict-reduction-atlas-for-three-chain-defects

title: Strict reduction atlas for three chain defects
type: claim | label: mixed | verification: unverified
namespace: third23
mechanism: Uses explicit chain covers, singleton absorption, threshold-gap analysis, deletion-weight formulas, duality, and a banked two-defect chain theorem plus width-at-most-two results. The artifact proves the stated reductions but records the generic A, Q, and V/Λ cases as unresolved rather than claiming a complete classification.
[graph-node: kgn_cb4d5ec5bdf2 — this page is a PROJECTION; truth lives in the research KG]

## Statement

For a finite poset with distinguished chain C and three off-chain elements, the T defect-order shape is strictly reduced via an explicit two-chain cover, and every singleton-gap branch is strictly reduced by absorbing the singleton into an enlarged chain. The all-non-singleton A, Q, and V/Λ branches remain unresolved, with their first missing maps and adversarial examples identified.

## Content

# Strict reduction atlas for three chain defects

# Strict reduction atlas for three chain defects

status: as labeled in the artifact (session deliverable, banked VERBATIM by the harness)

HEADLINE: DECOMPOSED contract. The three-chain shape T is strictly reduced by the explicit two-chain cover C ⊔ {x<y<z}, and every singleton-gap branch is strictly reduced by absorbing the singleton into an enlarged chain. The residual all-non-singleton A, Q, and V/Λ branches remain unresolved, with their first missing maps and adversarial examples identified exactly.

# Strict Reduction Atlas for Three Off-Chain Elements

## Outcome

**DECOMPOSED contract.** The T branch and every singleton-gap branch are reduced by explicit maps on the original poset. The generic all-non-singleton A, Q, and V/Λ branches are not declared reduced; their first exact missing maps are recorded below.

## 1. Definitions and strict reduction

Let P be finite, let C=(c₁<⋯<cₘ) be the distinguished chain, and let P−C={x,y,z}. Write L(P) for the linear extensions and e(P)=|L(P)|. For an incomparable pair a∥b, define n_P(a<b) as the number of linear extensions in which a occurs before b, and Pr_P(a<b)=n_P(a<b)/e(P).

**[PROVED-HERE — campaign definition.]** A balance witness is one fixed incomparable pair a∥b in the original P for which

e(P)/3 ≤ n_P(a<b) ≤ 2e(P)/3.

A strict reduction must be an explicit map from the original instance to one of these terminal certificates:

1. a fixed balance witness in P;
2. the banked Two-Defect Chain Theorem applied to the same P after exhibiting a chain C′ with |P−C′|=2;
3. an explicit partition P=A ⊔ B into two chains, followed by the SOURCE-VERBATIM width-at-most-two theorem; or
4. an explicit ordinal-sum factor map to a previously decided singleton or Q block, with the linear-extension concatenation map shown.

Thus reduced means reduced toward a certified witness or a previously decided class. It does not mean merely deleting an element. The campaign rank is 3 for an unresolved three-defect instance, 2 for a same-poset chain-plus-two-defect reclassification, 1 for a two-chain-cover certificate, and 0 for a balance witness or the chain convention.

**[PROVED-HERE.]** If P is a chain, there is no incomparable pair and the campaign convention is δ(P)=0.

## 2. Consumed banked inputs

**[ARGUED — SOURCE-VERBATIM.]** The attached source recovery states that width two means width at most two and that every finite width-at-most-two poset outside the direct-sum family generated by singleton posets and the three-element one-relation poset has balance greater than

1/3+1/105=12/35.

Linial 1984 is the original width-two proof named in the source deposit; Sah, arXiv:1811.01500v2, Theorem 1.4 is consumed at the deposited scope. No width-two proof is reproduced.

**[ARGUED — Aigner equality scope, banked.]** The banked literature record for Aigner 1985 is consumed as the equality audit: width-two equality at 1/3 occurs exactly for ordinal sums of singleton factors and Q blocks, where Q is a two-chain plus an isolated element.

**[ARGUED — banked Two-Defect Chain Theorem.]** A finite non-chain poset containing a chain whose complement has two elements has a balance witness. The incomparable-complement case is discharged by the banked overlapping insertion-interval model and Overlapping Two-Interval Balance Lemma; the comparable-complement case is width at most two.

**[ARGUED — banked duality.]** Order reversal bijects linear extensions, exchanges the two orientations of every incomparable pair, and preserves balance.

## 3. Raw insertion gaps, deletion, and duality

**[PROVED-HERE — raw threshold intervals.]** For each off-chain u, define

a_u=max({0}∪{i:c_i<u}),

b_u=min({m+1}∪{i:u<c_i})−1.

Then I_u=[a_u,b_u]⊆{0,…,m}, with

c_i<u for i≤a_u,
u<c_i for i>b_u,
u∥c_i for a_u<i≤b_u.

A singleton insertion gap is I_u=[k,k]. It means that u is comparable with every element of C; it does not determine the relation of u to the other two defects.

**[PROVED-HERE — deletion behavior.]** Deleting u gives d_u(P,C,U)=(P−u,C,U−{u}). Relations of the surviving defects to C, and hence their raw threshold intervals, are unchanged. However, if L′ is a linear extension of P−u and w_u(L′) is the number of legal insertion positions for u, then

e(P)=Σ_{L′∈L(P−u)} w_u(L′),

Pr_P(a<b)=Σ w_u(L′)·1_{a<b in L′} / Σ w_u(L′).

The deleted-poset probability uses uniform weights 1. Therefore deletion is not a strict reduction unless a constant-fiber or fixed-pair lifting argument is proved.

**[PROVED-HERE — dual map.]** In the dual P∨, use C∨=(cₘ∨<⋯<c₁∨). A gap k maps to m−k, so [a_u,b_u] maps to [m−b_u,m−a_u]. Q is sent to Q after swapping the endpoints of its unique relation; V is sent to Λ; T is sent to T after reversing its labels. The map reverses every linear extension and is probability-preserving up to exchanging orientations.

## 4. Defect-order classification up to duality

**[PROVED-HERE.]** Transitivity gives exactly these four shapes:

| Shape | Normal form | Dual |
|---|---|---|
| A | x∥y∥z pairwise | A |
| Q | x<y and z∥x,y | Q after endpoint relabeling |
| V/Λ | V: x<r, y<r, x∥y | Λ: r∨<x∨, r∨<y∨ |
| T | x<y<z | T after reversal |

Two relations with a common middle element force the third relation by transitivity, so they are T rather than an additional shape.

## 5. Explicit reduction of T

**[PROVED-HERE.]** For T define

A_T=C,

B_T=(x<y<z).

The explicit cover map is

χ_T(p)=0 if p∈C,
χ_T(p)=1 if p∈{x,y,z}.

The two fibers are chains and A_T ⊔ B_T=P. This covers every chain element and every off-chain element. Hence every antichain has at most one element in each fiber, so width(P)≤2.

If P is not a chain, apply the SOURCE-VERBATIM width-at-most-two theorem. If P lies in the exceptional direct-sum family, write P=B₁⊕⋯⊕B_s with each B_i a singleton or Q. For a non-chain P choose a Q block. Its three local extensions are abc, acb, cab; the pair {a,c} has counts 2 and 1. The explicit global map is

Φ(L₁,…,L_s)=L₁L₂⋯L_s,

with restriction as inverse. Thus the same pair has global probabilities 2/3 and 1/3. If every block is a singleton, P is a chain. This is a reduction of the original P, not a deletion.

## 6. Explicit singleton-gap absorption

**[PROVED-HERE.]** Suppose u has I_u=[k,k]. Define

C′=(c₁<⋯<c_k<u<c_{k+1}<⋯<cₘ).

The map

ρ_u:(P,C,{u,v,w}) ↦ (P,C′,{v,w})

is the identity on P and on every linear extension; only the distinguished chain changes. Since c_i<u for i≤k and u<c_i for i>k, C′ is a chain and |P−C′|=2.

For a surviving element v with old interval [a,b], the exact transformed interval relative to C′ is:

| Relation to u | Forced condition | New interval |
|---|---|---|
| v<u | b≤k | [a,b] |
| u<v | a≥k | [a+1,b+1] |
| v∥u | a≤k≤b | [a,b+1] |

The reason is that old gaps below k retain their coordinate, old gaps above k shift by one, and old gap k splits into the two positions before and after u precisely when v∥u. These formulas include k=0, k=m, and m=0.

The remaining order determines the terminal theorem:

| Original shape | Absorbed singleton | Remaining pair | Reduction |
|---|---|---|---|
| A | any defect | incomparable | ρ_u to the Two-Defect Chain Theorem |
| Q | z | x<y | ρ_z, then C′ and {x<y} are two chains |
| Q | x or y | other endpoint ∥ z | ρ_u to the Two-Defect Chain Theorem |
| V: x<r,y<r | r | x∥y | ρ_r to the Two-Defect Chain Theorem |
| V | x or y | other branch <r | ρ_u, then C′ and the comparable pair are two chains |
| T | any defect | remaining two comparable | ρ_u, then a two-chain cover |

For the incomparable remaining pair, the banked insertion-gap structural theorem supplies overlapping transformed intervals and the Two-Defect Chain Theorem applies. For a comparable remaining pair, the explicit cover is P=C′ ⊔ (v<w), covering every element. Λ is obtained by composing this map with duality.

## 7. Adversarial deletion and endpoint computations

**[COMPUTED.]** The in-session script outputs/code/strict_reduction_atlas/audit.py exited 0. Its exact output was:

one_third= 1/3 two_thirds= 2/3
one_third_plus_one_105= 12/35 equals_12_over_35= True
Q_extensions= ['abc', 'acb', 'cab'] e= 3 a_before_c= 2 b_before_c= 1
absorption_interval_cases= 1485 failures= 0
absorption_endpoint_samples= (0, 2) (1, 3) (1, 3) (0, 2)
A sub_e= 5 full_e= 18 sub_cut= 2/5 = 2/5 full_cut= 6/18 = 1/3 fiber_sizes= [3, 3, 4, 4, 4] fiber_size_multiplicities= [(3, 2), (4, 3)]
Q sub_e= 4 full_e= 14 sub_cut= 2/4 = 1/2 full_cut= 6/14 = 3/7 fiber_sizes= [3, 3, 4, 4] fiber_size_multiplicities= [(3, 2), (4, 2)]
V sub_e= 6 full_e= 8 sub_cut= 3/6 = 1/2 full_cut= 5/8 = 5/8 fiber_sizes= [1, 1, 1, 1, 2, 2] fiber_size_multiplicities= [(1, 4), (2, 2)]
A* interval_lengths= [2, 2, 2] max_chain,max_antichain= (2, 3) incomparability_components= [[0, 1, 2, 3, 4]]
Q* interval_lengths= [2, 2, 2] max_chain,max_antichain= (2, 3) incomparability_components= [[0, 1, 2, 3, 4]]
V* interval_lengths= [2, 3, 3] max_chain,max_antichain= (3, 3) incomparability_components= [[0, 1, 2, 3, 4, 5]]
AUDIT_OK

The deletion fibers are nonconstant. For example, in the A test deletion leaves a selected cut with probability 2/5, while the original poset has probability 6/18=1/3. The computation is not a counterexample to balance; it is an exact refutation of deletion-plus-inheritance as a reduction rule.

## 8. First exact missing maps for A, Q, and V

**[PROVED-HERE — closed atlas portion.]** The following branches are closed: all T instances; all A, Q, V, and Λ instances with at least one singleton raw gap; and any additional instance for which an actual two-chain cover or fixed balance count is explicitly displayed.

**[FAILED — exact first stall for A.]** Take m=2, I_x=[0,1], I_y=I_z=[1,2], with x∥y∥z. Every interval has length at least 2. The direct off-chain antichain has width 3; the audit gives maximum chain 2, maximum antichain 3, and a connected incomparability graph. Hence no two-chain cover is available, and no chain of size |P|−2=3 exists for a same-poset Two-Defect reclassification. The first missing map is

R_A: all-non-singleton A data → fixed balance witness, two-defect chain, or two-chain cover.

No such uniform map is claimed, and no counterexample is claimed.

**[FAILED — exact first stall for Q.]** Take m=2, I_x=[0,1], I_y=I_z=[1,2], with x<y and z∥x,y. Every interval has length at least 2. The audit gives maximum chain 2, maximum antichain 3, and a connected incomparability graph; an antichain is {y,z,c₂}. Thus neither a two-chain cover nor a chain of size |P|−2=3 is available in this first residual test. Deleting z reaches a width-two subposet but does not lift its probabilities. The first missing map is the fixed-pair or same-poset class map R_Q for asymmetric non-singleton Q data. The aligned common-window Q theorem is not silently imported.

**[FAILED — exact first stall for V.]** Up to duality, take m=3, I_x=[0,1], I_y=[0,2], I_r=[1,3], with x<r, y<r, x∥y. All intervals are non-singletons. The audit gives maximum chain 3, maximum antichain 3, and a connected incomparability graph. Since |P|=6, no chain of size |P|−2=4 exists; width 3 rules out a two-chain cover. The first missing map is the general non-singleton V map R_V to a fixed balance witness, two-defect reclassification, or two-chain cover. Λ has the dual missing map D R_V D⁻¹.

These residual examples only show that the mandatory reductions do not apply. They do not assert that balance witnesses fail to exist.

## 9. Final contract

**[PROVED-HERE.]** Up to duality, the strict prerequisite atlas is complete for the claimed mechanisms: T is reduced by an explicit two-chain cover, and every singleton-gap branch is reduced by explicit absorption, transformed intervals, and a verified remaining-pair terminal class.

**[FAILED — exact scope.]** The residual all-non-singleton A, Q, and V/Λ families are not solved. Their first missing maps are R_A, R_Q, and R_V; deletion is not an accepted substitute because its extension fibers are nonconstant.

**Single theorem-level outcome: DECOMPOSED contract.**

## Provenance

- kg_import | imported from wiki entry strict-reduction-atlas-for-three-chain-defects




# Theorem 9.3 (Canonical factorization and balance under ordinal sums)

---

## Banked record: `canonical-ordinal-sum-factorization-theorem-for-finite-poset`

# canonical-ordinal-sum-factorization-theorem-for-finite-poset

title: Canonical Ordinal-Sum Factorization Theorem for Finite Posets
type: claim | label: proved | verification: unverified
namespace: third23 | aliases: Canonical ordinal-sum factorization
mechanism: Distinct connected components of the incomparability graph have no incomparable cross-pairs, and incomparability-path arguments force all cross-comparisons to point uniformly in one direction; this induces a strict total order on the components. A poset is ordinal-sum-indecomposable exactly when its incomparability graph is connected, which also forces uniqueness of any factorization.
[graph-node: kgn_883bcb33ca3c — this page is a PROJECTION; truth lives in the research KG]

## Statement

Every finite nonempty poset factors uniquely as an ordinal sum of nonempty ordinal-sum-indecomposable induced subposets, namely the connected components of its incomparability graph, ordered so that every element of an earlier component is below every element of a later component. The factors are canonical for labeled posets and unique up to corresponding factor isomorphisms, including their order.

## Content

# Canonical Ordinal-Sum Factorization Theorem for Finite Posets

# Canonical Ordinal-Sum Factorization Theorem for Finite Posets

**Status and labels.** Every theorem/lemma/deduction below is marked **[PROVED-HERE]**. The finite enumeration audit at the end is marked **[COMPUTED]** and is a sanity check, not a logical premise.

## 1. Conventions and the quantity δ

A finite poset is a finite set X with a reflexive, antisymmetric, transitive order ≤. Write x<y for x≤y and x≠y, and write x∥y when x and y are incomparable. A chain is a poset in which every two elements are comparable.

A linear extension of P is a total ordering (equivalently, a list of all elements of X) in which x occurs before y whenever x<y. Let L(P) be the finite set of linear extensions, and choose one uniformly. For an incomparable pair {x,y}, Pr(x<y) means the probability that x occurs before y in this random list. (A finite poset has a linear extension by repeatedly choosing a minimal element of the remaining finite poset.)

Use the campaign definition, literally:

\[
\delta(P)=\max_{\{x,y\}\text{ unordered incomparable}}
 \min\{\Pr(x<y),\Pr(y<x)\}
\]

when P is not a chain, and **δ(P)=0 for chains**. The chain convention is part of the definition, so no maximum over an empty set is being taken for a chain.

## 2. Ordinal sum versus disjoint union

Let P=(X,≤P) and R=(Y,≤R), first replacing one ground set by an isomorphic copy if necessary so that X∩Y=∅. Their ordinal sum P⊕R is the poset on X⊔Y whose order is the old order inside X, the old order inside Y, and, in addition,

\[
 x<_{P\oplus R}y\quad\text{for every }x\in X,\ y\in Y.
\]

There are no elements of Y below elements of X. For a finite ordered list P1,…,Pk, define P1⊕⋯⊕Pk directly on the disjoint union by retaining each internal order and declaring every element of Pi below every element of Pj when i<j.

This is not the disjoint union. The disjoint union P⊔R retains only the two internal orders and declares every cross pair x∈X, y∈Y incomparable. Since both summands are nonempty, P⊕R and P⊔R have opposite behavior on every cross pair. In particular, writing an ordinal sum is not shorthand for putting posets side by side without relations.

## 3. Canonical factorization theorem

### Theorem [PROVED-HERE]

Let P be a finite nonempty poset, with ground set X. Form its incomparability graph G(P): its vertices are X, and two distinct vertices are adjacent exactly when they are incomparable in P. A one-vertex graph is regarded as connected. Let C1,…,Ck be the connected components of G(P), put the components in the unique order described below, and let Pi=P|Ci be the induced subposet on Ci. Then

\[
 P=P_1\oplus\cdots\oplus P_k,
\]

and every Pi is nonempty and ordinal-sum-indecomposable. This ordered list is canonical and is the unique factorization of P into nonempty ordinal-sum-indecomposable factors: for a labeled P the blocks are exactly C1,…,Ck, and for an abstract factorization the factors are uniquely determined up to the corresponding factor isomorphisms, including their order.

### Proof of the component-order assertion [PROVED-HERE]

Take two distinct components C and D. No element of C can be incomparable with an element of D, because such a pair would be an edge joining the components. Thus every cross pair is comparable. It remains to prove that the direction is uniform.

Suppose c0∈C and d0∈D satisfy c0<d0. If u∥v and u<d, with v and d comparable, then d<v is impossible: transitivity would give u<v. Hence v<d. Applying this along an incomparability path in C from c0 to any c shows c<d0 for every c∈C.

Now fix such a c. Along an incomparability path d0=d0,d1,…,dt=d in D, if c<dj and dj∥dj+1, then dj+1<c is impossible, since it would give dj+1<c<dj and hence dj+1<dj. Because c and dj+1 are cross-component and therefore comparable, c<dj+1. Thus c<d for every d∈D. Consequently, if one cross pair points from C to D, every cross pair does; if the first pair points from D to C, the symmetric argument applies.

Therefore define C<D when (equivalently, whenever) c<d for all c∈C and d∈D. Any two distinct components are related in exactly one direction. This relation is transitive: C<D and D<E imply c<d<e for arbitrary representatives, so C<E. Hence it is a strict total order on the components. List them as C1<⋯<Ck.

For i<j, every element of Ci is below every element of Cj, while the order inside Ci is exactly the induced order Pi. This is precisely the definition of P1⊕⋯⊕Pk, proving the asserted decomposition.

### Proof of indecomposability and uniqueness [PROVED-HERE]

For any nonempty posets A and B, every element of A is comparable with every element of B in A⊕B. Hence the incomparability graph of A⊕B has no edge between the A-side and the B-side, and is disconnected (there are vertices on both sides). Thus an ordinal-sum decomposition into two nonempty pieces implies a disconnected incomparability graph.

Conversely, if the incomparability graph of a nonempty poset S is disconnected, its components are at least two nonempty sets, and the component-order argument just proved writes S as the ordinal sum of the induced subposets on those components. Therefore

\[
 S\text{ is ordinal-sum-indecomposable}
 \quad\Longleftrightarrow\quad
 G(S)\text{ is connected}.
\]

Each Ci is a connected component, so each Pi is indecomposable.

For uniqueness, suppose a factorization into nonempty indecomposables is given, first in the labeled form
\[
P=R_1\oplus\cdots\oplus R_m
\]
with disjoint blocks D1,…,Dm covering X. There are no incomparability edges between distinct Di and Dj. Since Ri is indecomposable, G(P)|Di is connected, so Di lies in one component of G(P). Conversely, a path in G(P) cannot cross from one D-block to another, so every component of G(P) lies in one D-block. The two containments force each Di to be exactly one Cj. Thus m=k and the blocks are precisely the canonical components. Since the ordinal sum puts Di below Dj for i<j, their order is the intrinsic total order C1<⋯<Ck. An abstract factorization is transported to this labeled situation by its poset isomorphism, giving the same conclusion up to factor isomorphism. No permutation of the factors is allowed except one that preserves this ordered sequence.

### Degenerate cases [PROVED-HERE]

Nonemptiness is essential only to ensure that there is at least one component and no empty factor is introduced; the theorem explicitly excludes the empty poset. If P is a singleton, G(P) is the connected one-vertex graph, so k=1 and the singleton is its own indecomposable factor. If P is a chain with n≥2 elements, G(P) has n isolated one-vertex components, ordered in the chain order, so its canonical factorization is the ordinal sum of its n singleton factors. If P is an antichain with more than one element, G(P) is connected, so the whole antichain is one indecomposable factor; this also illustrates why incomparability components must not be confused with disjoint-union components.

## 4. δ under ordinal sums

### Theorem [PROVED-HERE]

For finite nonempty posets P1,…,Pk,

\[
\boxed{\displaystyle
\delta(P_1\oplus\cdots\oplus P_k)=\max_{1\le i\le k}\delta(P_i),
}
\]

where δ(Pi)=0 when Pi is a chain.

### Proof by a complete linear-extension bijection [PROVED-HERE]

Let S=P1⊕⋯⊕Pk and let ei=|L(Pi)|. Define

\[
\Phi:L(P_1)\times\cdots\times L(P_k)\longrightarrow L(S)
\]

by concatenating the lists: first L1, then L2, and so on. The result is a linear extension because each Li respects its internal order and every element of Pi is below every element of Pj for i<j.

Conversely, in any global linear extension all elements of Pi must occur before all elements of Pj whenever i<j. Restricting the global list to Pi therefore gives a member Li of L(Pi), and the global list is necessarily the concatenation of those restrictions. Thus Φ is a bijection, and

\[
|L(S)|=\prod_{i=1}^k e_i.
\]

Because every tuple has exactly one image, a uniformly chosen global linear extension corresponds to a uniformly chosen tuple of local extensions; in particular the local coordinates are independent and uniform. More explicitly, for x,y∈Pi that are incomparable in Pi, if Li(x<y) denotes the local extensions in which x occurs before y, then

\[
\Pr_S(x<y)
=\frac{|L_i(x<y)|\prod_{j\ne i}e_j}{\prod_j e_j}
=\frac{|L_i(x<y)|}{e_i}
=\Pr_{P_i}(x<y),
\]

and the same equality holds with x and y reversed.

There are no incomparable pairs from distinct factors: every such cross pair is ordered by the ordinal sum. The incomparable pairs of S are therefore exactly the disjoint union of the incomparable pairs internal to the Pi, and each internal pair has exactly the same two orientation probabilities in S as in Pi. If at least one factor is a nonchain, taking the maximum over this union gives

\[
\delta(S)=\max_i\delta(P_i),
\]

with the chain factors contributing 0. If every factor is a chain, then S is a chain, so δ(S)=0 by convention and the right side is also the maximum of zeros. This covers all cases.

## 5. Exact calibrations

### Singleton [PROVED-HERE]

A singleton is a chain and has one linear extension, so the stipulated chain convention gives δ=0.

### Q [PROVED-HERE]

Let Q have elements a,b,c and sole strict relation a<b; c is isolated from that relation. The permutations respecting a<b are exactly

\[
abc,\quad acb,\quad cab.
\]

Thus Q has exactly three linear extensions. Among them, a occurs before c twice (abc, acb) and c before a once (cab), so the two probabilities for {a,c} are 2/3 and 1/3. Also b occurs before c once (abc) and c before b twice (acb, cab), so the probabilities for {b,c} are 1/3 and 2/3. The pair {a,b} is comparable. Hence

\[
\boxed{\delta(Q)=1/3.}
\]

Moreover, G(Q) is the path a--c--b, so Q is itself ordinal-sum-indecomposable.

### The standard V-poset [PROVED-HERE]

Let V have relations v<a and v<b, with a∥b. Its only linear extensions are

\[
vab,\quad vba.
\]

Thus there are exactly two. The pair {a,b} is oriented each way once, giving probabilities 1/2 and 1/2, and it is the only incomparable pair. Therefore

\[
\boxed{\delta(V)=1/2.}
\]

So V is not the 1/3 block. In fact G(V) consists of the edge a--b and the isolated vertex v, and the canonical factorization is the singleton v followed by the two-element antichain {a,b}; V is not ordinal-sum-indecomposable either.

## 6. Q/singleton corollary

### Corollary [PROVED-HERE]

If
\[
S=B_1\oplus\cdots\oplus B_m
\]
where every Bj is either a singleton or a copy of Q, and at least one Bj is Q, then

\[
\boxed{\delta(S)=1/3.}
\]

Indeed, the ordinal-sum δ theorem gives the maximum of the singleton values 0 and the Q values 1/3. The maximum is 1/3 because a Q block is present.

## 7. In-session computation audit (not a logical premise)

### Calibration run [COMPUTED]

The persisted script `outputs/ordinal_sum_factorization/calibration.py` was executed in-session. Its exact output was:

```
singleton linear extensions: 1
singleton extensions: ['s']
singleton incomparable-pair probabilities/minima: []
singleton delta: 0
Q linear extensions: 3
Q extensions: ['abc', 'acb', 'cab']
Q incomparable-pair probabilities/minima: [('a', 'c', Fraction(2, 3), Fraction(1, 3), Fraction(1, 3)), ('b', 'c', Fraction(1, 3), Fraction(2, 3), Fraction(1, 3))]
Q delta: 1/3
V linear extensions: 2
V extensions: ['vab', 'vba']
V incomparable-pair probabilities/minima: [('a', 'b', Fraction(1, 2), Fraction(1, 2), Fraction(1, 2))]
V delta: 1/2
```

### Adversarial finite graph audit [COMPUTED]

The persisted script `outputs/ordinal_sum_factorization/graph_exhaustive_check.py` enumerated all labeled strict relations on n≤5 vertices, retained exactly the transitive ones, formed the incomparability components, checked uniform cross orientation, and checked reconstruction as an ordinal sum. Exact output:

```
n=1: posets_checked=1, bad_cases=0
n=2: posets_checked=3, bad_cases=0
n=3: posets_checked=19, bad_cases=0
n=4: posets_checked=219, bad_cases=0
n=5: posets_checked=4231, bad_cases=0
```

The persisted script `outputs/ordinal_sum_factorization/uniqueness_exhaustive_check.py` additionally checked all ordered set partitions on these labeled posets and found no alternative ordered factorization whose blocks were graph-connected and cross-ordered. Exact output:

```
n=1: posets_checked=1, canonical-indecomposable ordered factorizations unique=True
n=2: posets_checked=3, canonical-indecomposable ordered factorizations unique=True
n=3: posets_checked=19, canonical-indecomposable ordered factorizations unique=True
n=4: posets_checked=219, canonical-indecomposable ordered factorizations unique=True
n=5: posets_checked=4231, canonical-indecomposable ordered factorizations unique=True
```

These audits do not replace the component-path proof above; they found no counterexample in the stated finite ranges.


---
provenance: actor=work_math_manager_streaming work_id=work_a79642ace32c node_id=width_two_ordinal_sum_factorization banked=2026-08-16T22:25:57Z

## Provenance

- work_math_manager_streaming | work_a79642ace32c | width_two_ordinal_sum_factorization | imported from wiki entry canonical-ordinal-sum-factorization-theorem-for-finite-poset
- supervisor | work_d9012266fb52 | banked per finding at effort end




# Theorem 10.1 (Antichain heavy-gap coincidence)

---

## Banked record: `antichain-defect-distinct-heavy-index-exclusion`

# antichain-defect-distinct-heavy-index-exclusion

title: Antichain-defect distinct-heavy-index exclusion
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: The antichain hypothesis makes the feasible gap maps a Cartesian product. Exact tied-fiber weights show that every defect marginal is maximized precisely on the common intersection of the three legal-gap intervals. Heavy-gap uniqueness then forces that intersection to be a singleton, shared by all three defects.
[graph-node: kgn_7e50beeefbc3 — this page is a PROJECTION; truth lives in the research KG]

## Statement

Let P be a finite ordinal-sum-indecomposable poset, let C be a maximum chain with P\C={x,y,z}, and assume x,y,z are pairwise incomparable. If every incomparable-pair orientation probability avoids the closed interval [1/3,2/3], then the unique heavy gaps supplied by heavy-gap rigidity satisfy r_x=r_y=r_z. In particular, the three heavy gaps cannot be pairwise distinct in this nonempty subfamily. The conclusion includes boundary gaps 0 and |C| and the equality boundaries N/3 and 2N/3.

## Content

Let P be a finite ordinal-sum-indecomposable poset, let C be a maximum chain with P\C={x,y,z}, and assume x,y,z are pairwise incomparable. If every incomparable-pair orientation probability avoids the closed interval [1/3,2/3], then the unique heavy gaps supplied by heavy-gap rigidity satisfy r_x=r_y=r_z. In particular, the three heavy gaps cannot be pairwise distinct in this nonempty subfamily. The conclusion includes boundary gaps 0 and |C| and the equality boundaries N/3 and 2N/3.

## Provenance

- supervisor | work_5d721f333ec6 | banked per finding at effort end



---

## Banked record: `corrected-antichain-distinct-heavy-index-exclusion-derivatio`

# corrected-antichain-distinct-heavy-index-exclusion-derivatio

title: corrected-antichain-distinct-heavy-index-exclusion-derivation
type: claim | label: proved | verification: unverified
namespace: third23
[graph-node: kgn_53d7a783f9a8 — this page is a PROJECTION; truth lives in the research KG]

## Statement

PROVED (conditional on the imported exact antichain three-defect marginal formula, antichain feasible-gap product/common-intersection lemma, and heavy-gap rigidity under closed-third avoidance): Let P be finite ordinal-sum-indecomposable, C a maximum chain, P\C={x,y,z} pairwise incomparable, and assume every incomparable-pair orientation probability avoids the closed interval [N/3,2N/3] (equivalently every such numerator is strictly below N/3 or strictly above 2N/3). Then the unique heavy gaps r_x,r_y,r_z coincide. Hence pairwise-distinct heavy gaps are impossible in the antichain-defect subfamily.

## Content

Let I_u=[a_u,b_u]\cap\mathbb Z be the legal gap interval of defect u, with gaps 0,...,m relative to C=(c_1<...<c_m). The imported exact ledger gives, for a feasible gap triple g=(i,j,k), the fiber weight W(g)=1+1_{i=j}+1_{i=k}+1_{j=k}+2·1_{i=j=k}: weight 1 for three distinct gaps, 2 for exactly one tied pair, and 6 for a full tie. This is the antichain specialization of the induced tied-block product; it retains all three coordinates and is not an additive pair correction. Because the defects are pairwise incomparable, feasibility is exactly I_x×I_y×I_z. Pairwise incomparability also forces the intervals to intersect pairwise; Helly for integer intervals gives J=I_x∩I_y∩I_z nonempty. For r∈I_x, summing the exact fiber weights over (j,k) gives μ_x(r)=n_y n_z+|I_y∩I_z|+n_z·1_{r∈I_y}+n_y·1_{r∈I_z}+2·1_{r∈I_y∩I_z}, where n_u=|I_u|; cyclic formulas hold for y,z. The correct marginal-sum explanation is that the first two terms are constant in r, while the final three are nonnegative membership bonuses. Since J is nonempty, the maximum value is attained exactly when both bonuses 1_{r∈I_y} and 1_{r∈I_z} equal 1, i.e. exactly for r∈J; any r∈I_x\J misses at least one nonnegative bonus and is strictly smaller. This is a maximization statement, not a claim that a marginal is an additive sum of independent tied contributions. The marginal μ_x(r) is the total number of extensions with x in gap r, so Σ_{r∈I_x}μ_x(r)=N. By imported heavy-gap rigidity, x has a unique gap r_x with μ_x(r_x)>N/3, and every other gap has mass at most? More precisely the rigidity input gives μ_x(r_x)>N/3 and the left/right tails strictly below N/3; uniqueness of the heavy atom follows because two atoms >N/3 would contradict the rigidity conclusion. Therefore the global maximum of μ_x is >N/3 and, by the preceding maximizer characterization, every maximizer lies in J; in particular r_x∈J. The same argument gives r_y,r_z∈J. If J contained two distinct gaps, then both would be maximizers for μ_x and both would have the same value μ_x(r_x)>N/3, contradicting uniqueness of x's heavy gap. Thus J={r} is a singleton, and r_x=r_y=r_z=r. This includes boundary gaps 0 and m: the interval and Helly argument uses closed integer intervals, and the rigidity input explicitly includes endpoint jumps and singleton windows. Equality cases at N/3 and 2N/3 are excluded by the hypothesis; all strict inequalities used above are therefore legitimate. The proof does not assert or need the stronger tail-cover inequality N≤3T, and it does not promote the ledger to an automatic balanced-pair theorem. Imported inputs remain at their recorded verification status; the present derivation is complete conditional on them.

## Edges

- depends_on -> Exact antichain three-defect marginal formula (kgn_92184aa04225)
- depends_on -> Antichain feasible-gap product and common intersection (kgn_7ac00685647b)
- depends_on -> Heavy-Gap Rigidity Under Closed-Third Avoidance (kgn_61fdce45cbe7)
- depends_on -> Corrected Three-Defect Ledger Interface (kgn_2d30c290f545)

## Provenance

- agent | kg bank



---

## Banked record: `antichain-distinct-heavy-verification-debt-resolution`

# antichain-distinct-heavy-verification-debt-resolution

title: Antichain Distinct-Heavy Verification Debt Resolution
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Exact marginal formulas identify J as the common maximizing plateau, while uniqueness of each greater-than-one-third atom forces that plateau to contain exactly one gap.
[graph-node: kgn_c86f23036454 — this page is a PROJECTION; truth lives in the research KG]

## Statement

For three pairwise-incomparable defects under the exact Cartesian gap/fiber model and closed-third avoidance, their legal gap intervals have a nonempty common intersection J; every point of J maximizes each defect marginal; and the chain-cut CDF jump argument gives each marginal a unique atom of mass greater than N/3. Hence J is a singleton and all three unique heavy-gap indices coincide. This argument uses neither a tail-cover inequality nor any inference from separate marginals to a joint orientation event.

## Content

For three pairwise-incomparable defects under the exact Cartesian gap/fiber model and closed-third avoidance, their legal gap intervals have a nonempty common intersection J; every point of J maximizes each defect marginal; and the chain-cut CDF jump argument gives each marginal a unique atom of mass greater than N/3. Hence J is a singleton and all three unique heavy-gap indices coincide. This argument uses neither a tail-cover inequality nor any inference from separate marginals to a joint orientation event.

## Provenance

- supervisor | work_3b0d5b48d20f | banked per finding at effort end




# Theorem 10.2 (Centered three-interval CH inequality)

---

## Banked record: `centered-three-interval-ch-chamber-specific-global-decision`

# centered-three-interval-ch-chamber-specific-global-decision

title: Centered three-interval CH inequality
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Parametrize all weak endpoint-order chambers, use exact rational certificates expressing -Q_A as a nonnegative combination of S_L=N-3L_1, S_H=N-3H_3, and a coefficientwise nonnegative residual, then handle the sole exceptional chamber a=12|0, b=01|2 by substituting a2=a3=p, a1=p+1+u, b1=b2=q, b3=q+1+v and proving that simultaneous positive tail slacks force p=q=u=v=0, where Q_A=0.
[graph-node: kgn_a93dee9bd6fb — this page is a PROJECTION; truth lives in the research KG]

## Statement

For every nonnegative integer endpoint vector with intervals I_u=[-a_u,b_u], if 3L_1<N and 3H_3<N, then Q_A≤0; equivalently, Q_A>0 implies N≤3 max(L_1,H_3). The result is proved by exact weak-chamber polynomial certificates for 168 of 169 endpoint-pattern pairs and an explicit four-variable slack identity for the exceptional chamber.

## Content

# Centered three-interval CH chamber-specific global decision

# Centered three-interval CH chamber-specific global decision

status: as labeled in the artifact (session deliverable, banked VERBATIM by the harness)

HEADLINE: [PROVED-HERE] CH holds for every centered integer three-interval box. An exact weak-chamber polynomial certificate covers 168 of the 169 weak endpoint-pattern pairs; the sole exceptional chamber is settled by an explicit four-variable slack identity.

# Direct CH decision: centered three-interval antichain inequality — 2026-08-17

## Completion

**[PROVED-HERE]** For every nonnegative integer endpoint vector with `I_u=[-a_u,b_u]`,

`3L_1<N` and `3H_3<N` implies `Q_A<=0`.

Equivalently, `Q_A>0` implies `N<=3 max(L_1,H_3)`.

The complete referee-ready artifact is banked at `outputs/direct_CH_decision_20260817_PROVED.md` and under the wiki title `Direct CH decision: centered three-interval antichain inequality — 2026-08-17`.

## 1. Exact interface consumed

**[SOURCE-VERBATIM — consumed, not reopened]** For `I_u=[-a_u,b_u]`, put

`n_u=1+a_u+b_u`,
`d_uv=1+min(a_u,a_v)+min(b_u,b_v)`, and
`d_123=1+min(a_1,a_2,a_3)+min(b_1,b_2,b_3)`.

The banked exact formulas are

`N=n1*n2*n3+d12*n3+d13*n2+d23*n1+2*d123`,

`L1=a1*n2*n3+min(a1,a2)*n3+min(a1,a3)*n2+a1*d23+2*min(a1,a2,a3)`,

`H3=b3*n1*n2+min(b3,b1)*n2+min(b3,b2)*n1+b3*d12+2*min(b1,b2,b3)`.

The tied weak-order ledger is

`N=T123+T132+T213+T231+T312+T321`,

`Q_A=T123-T231-T312-2*T321`.

Set `S_L=N-3L1` and `S_H=N-3H3`.

The banked signed identity is `Q_A=(D-N)/2`, where

`D=n3*s(I1,I2)+n1*s(I2,I3)+n2*s(I1,I3)
 +2*s(I1 intersect I2,I3)+2*s(I1,I2 intersect I3)`,

and `s(A,B)=sum_{x in A,y in B} sgn(y-x)`.

## 2. Exact signed-sum chamber formulas

**[PROVED-HERE]** For `A=[-a,b]` and `B=[-c,d]`, direct finite summation gives:

```text
 a<=c, b<=d: (a+b+1)*(a-b-c+d)
 a<=c, b>=d: a^2-a*c+a*d+a-b*c-b*d-b-c+d^2+d
 a>=c, b<=d: a*c+a*d+a-b^2-b*c+b*d-b-c^2-c+d
 a>=c, b>=d: (c+d+1)*(a-b-c+d)
```

These formulas agree on equality faces. They are obtained by splitting the inner signed sum at the interval endpoints; no interpolation or floating-point arithmetic is needed.

## 3. Weak-chamber certificates

The 13 ordered equality patterns for three endpoint extents are:

```text
0: 012       1: 01|2       2: 02|1       3: 0|12
4: 0|1|2     5: 0|2|1     6: 12|0       7: 1|02
8: 1|0|2     9: 2|01      10: 2|0|1     11: 1|2|0
12: 2|1|0
```

For a pattern `B0|...|B(r-1)`, assign its common endpoint values as

`x, x+1+z1, x+2+z1+z2, ...`,

where `x,z_i>=0`; use independent variables for the `a` and `b` patterns. This parametrizes exactly every integer weak endpoint pattern, including zero endpoints and equality faces.

For each pair of patterns define

`Rem=-Q_A-alpha*S_L-beta*S_H`.

The exact rational `(alpha,beta)` certificate table is:

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
row11: (1/4,0) (1/2,1/2) (1/4,0) (1/2,1/2) (2/3,5/6) (1/2,1/2) (1/4,0) (1/3,1/6) (1/2,1/2) (1/4,0) (1/4,0) (1/3,1/6) (1/4,0)
row12: (1/2,0) (5/6,2/3) (1/2,0) (5/6,2/3) (1,1) (5/6,2/3) (1/2,0) (1/2,0) (5/6,2/3) (1/2,0) (1/2,0) (1/2,0) (1/2,0)
```

**[COMPUTED — exact coefficient audit executed in-session]** The exact rational expansion of `Rem` had nonnegative coefficients for 168 of the 169 pattern pairs. The only uncertified pair was row 6, column 1: `a=12|0`, `b=01|2`. The numerical LP was used only to discover small rational candidates; every listed residual was then re-expanded and checked with exact rational coefficients.

Therefore, in every nonexceptional chamber,

`-Q_A=alpha*S_L+beta*S_H+Rem`,

with `alpha,beta>=0` and `Rem>=0`. Hence `S_L>0,S_H>0` implies `Q_A<=0` in all 168 nonexceptional chambers.

## 4. Exceptional chamber

The sole exceptional pattern is

`a2=a3=p`, `a1=p+1+u`, `b1=b2=q`, `b3=q+1+v`,

with `p,q,u,v>=0`. Exact substitution gives

`Q_A=-(p+q+1)/2 * R`,

where

`R=p^2+2*p*q-p*u-p*v+3*p+q^2-q*u-q*v+3*q-2*u*v-4*u-4*v`.

The exact sum of the tail slacks is

```text
S_L+S_H = -p^3-3*p^2*q-p^2*u-4*p^2*v-8*p^2
          -3*p*q^2-5*p*q*u-5*p*q*v-16*p*q
          -4*p*u*v-7*p*u-13*p*v-12*p
          -q^3-4*q^2*u-q^2*v-8*q^2-4*q*u*v-13*q*u-7*q*v-12*q
          -4*u*v-6*u-6*v+4.
```

If `u+v>=1`, this is at most `-2`; if `u=v=0` and `p+q>=1`, the negative `p,q` terms make it strictly negative. Thus `S_L>0,S_H>0` forces `p=q=u=v=0`. At that point `Q_A=0`.

So CH holds in the exceptional chamber as well.

## 5. Boundary and stance checks

**[PROVED-HERE]** The weak-pattern parametrization includes zero endpoints, singleton intervals, repeated endpoints, containments, and every equality face.

**[SOURCE-VERBATIM — consumed]** The all-singleton box has

`T=(1,1,1,1,1,1), N=6, L1=H3=0, Q_A=-3`.

The exceptional base calibration has

`I1=[-1,0], I2={0}, I3=[0,1]`,

`T=(4,2,2,1,1,1), N=11, L1=H3=3, Q_A=0`.

Its forward pair masses are **[COMPUTED]**

`(M12,M23,M13)=(7,7,8)`,

so the tempting midpoint lemma `2M13<=N` fails even though `3L1=3H3=9<11`; the transitivity defect is 5 and gives `Q_A=0`. This kills the simplest k=3 injection, not the chamber proof.

**[FAILED-AT — non-load-bearing extremal route]** The consumed endpoint-transition record is

`(N,L1,H3,Q_A,U) old=(14,0,8,1,15)`,

`(N,L1,H3,Q_A,U) new=(20,6,12,6,26)`,

with `Delta U=11` against the loose allowance 16. This kills the old active-branch endpoint induction; it was not retried.

**[SOURCE-VERBATIM — consumed]** The raw TP2/MTP2 obstruction is the exact minor `2*2<1*6`; the transformed AD route was consumed and not retried.

## Conclusion

**[PROVED-HERE]** Every weak endpoint chamber is covered by an exact nonnegative-coefficient certificate or by the explicit exceptional calculation. Therefore

`(3L1<N and 3H3<N) => Q_A<=0`

for every centered integer interval box.

**Completion: PROVED.**

No counterexample ledger or defect-pair numerators are applicable.

## Provenance

- kg_import | imported from wiki entry centered-three-interval-ch-chamber-specific-global-decision



---

## Banked record: `deepcheck-repaired-ch-global-residuals-next`

# deepcheck-repaired-ch-global-residuals-next

title: Deepcheck of Repaired Centered-CH Global Residuals
type: note | label: mixed | verification: unverified
namespace: third23
mechanism: Fresh Fraction and SymPy QQ implementations independently parse and replay the supplied and repaired tables, verify the exact formulas and endpoint branches by exhaustive finite checks, and compare all residual coefficients and cell summaries. The entry reports both the repaired-scope pass and the unrepaired-table defect, without claiming an unscoped CH theorem.
[graph-node: kgn_136ffba5d3f9 — this page is a PROJECTION; truth lives in the research KG]

## Statement

An independent exact-rational replay verifies that the adopted repaired centered-CH certificate has nonnegative residual coefficients in all 168 nonexceptional cells, with the exceptional cell handled separately by an exact polynomial argument. The unrepaired source table fails at row (11,11), where changing (α,β) from (1/4,0) to (1/2,0) repairs the reported defect; the result applies only to centered integer intervals with a specified common integer cut.

## Content

# deepcheck-repaired-ch-global-residuals-next

# Deepcheck of the repaired centered-CH global residuals — 2026-08-17

## Verdict and exact scope

**[PROVED]** The adopted repaired centered certificate passes an independent exact-rational replay in the charged scope: centered legal triples
\[
 I_i=[-a_i,b_i],\qquad a_i,b_i\in\mathbb Z_{\ge0},
\]
with a specified common integer cut (translated to cut 0). There are 168 nonexceptional cells in the 13-by-13 weak endpoint-order pairing; every repaired residual coefficient in every one of them is nonnegative, and every coefficient comparison has zero mismatch. The one `EXC` cell is handled separately by an exact polynomial argument below.

**[CONTESTED]** The unrepaired source table is not a certificate: its row `(11,11)` entry is `(alpha,beta)=(1/4,0)`, and its residual has three coefficients `-1/2`. The adopted result uses exactly the specified repair `(alpha,beta)=(1/2,0)` at that row and nowhere else. This report does not claim an unscoped CH theorem.

The symbol `\mathbb Z_{\ge0}` above is written literally as “nonnegative integers”; no real-parameter or no-common-cut extension is made.

## Provenance of the exact inputs and fresh computation

**[COMPUTED]** The source artifact was accessed at:

- `outputs/direct_CH_decision_20260817_PROVED.md`;
- source byte SHA-256: `9eb6031fecf65abb51f16ed73adc8d166bb3582ecd94467f4415220f8d94a87e`.

Its table was parsed independently, accepting the source's `row10:`/`row11:`/`row12:` label-spacing variation. It yielded 13 rows, 169 entries, and one literal `EXC`. The parsed source table equals `outputs/independent_ch_certification_20260817/fresh_original_table.txt` and also equals the independently deposited `outputs/independent_repaired_169_centered_ch_certificate_audit_20260817/supplied_table.txt`.

**[COMPUTED]** The canonical supplied-table hash (13 normalized `row i:` lines joined by one LF, no final LF) is
`4ac6f3b63d9a92f2e0470a577a62f7400995af9cdd0f5ce9aad48c36ce5feaa1`.
The adopted repaired snapshot is `outputs/independent_ch_certification_20260817/fresh_repaired_table.txt` and equals the independently deposited `.../repaired_table.txt`; its canonical hash is
`2e6f562b5233d730cc5c531b8ce24d748e76e24062838aa6dd629190e1774d92`.
The exact parsed difference is the single tuple
```
(row 11, column 11, (1/4,0), (1/2,0)).
```
The `EXC` remains at row 6, column 1. Thus the repaired artifact was not silently substituted for the source: the source was replayed as supplied for the defect diagnosis, and the one-entry repaired artifact was replayed separately.

The fresh Fraction implementation is `outputs/independent_ch_certification_20260817/deepcheck_next_replay.py`, driven exactly by `deepcheck_next_runner.py`. The executed runner SHA-256 is `2c7cf4cedfe2cda1381e44588f3e7a9a0a3940cc0826211c79bc974047cfc255`; the loaded implementation SHA-256 is `bea5b70d24621af59608c22ba6a5c93bd61c2ecb66dee4ca49116d6ac9eb8775`. The runner adds only the missing generic `Poly.__pow__` method and corrects diagnostic manifest field names; it changes neither the input table nor a mathematical formula. The exact captured output is `deepcheck_next_stdout.txt`, SHA-256 `627ff0a2bcd790884a37c2e002c9ff213a93bffffceb5fff851b5d47f633d3b1`. The complete fresh cell summary is `deepcheck_next_cell_summary.tsv`, SHA-256 `c8e10cb7032b6aa5bab18a0f72053b236b6e45f7f5a1ee88c8cc454a45e06279`; the complete coefficient ledger is `deepcheck_next_coefficient_ledger.tsv`, SHA-256 `cbd2369a16e9674c5df14a9780c6ae182e4fe97ba0b12dcde9060d0279f93603`.

**[COMPUTED]** As an independent second implementation, a fresh SymPy `QQ` expansion is persisted at `deepcheck_next_sympy_replay.py` (SHA-256 `621951be9f2eb418e0937d5f7750501b98655c5b87690bd936a90744d0e32175`) with output `deepcheck_next_sympy_stdout.txt` (SHA-256 `99061288f21b1f215d9c31be4ad8de63a8cabc9d695358925c41d0ca273bc695`). It independently returned:
```
SYMPY_CELLS_EXC_IDENTITY_BADNEG 168 1 0 0
SYMPY_GLOBAL_MIN_MAX 1/4 59
SYMPY_ROW11_SUPPORT_MIN_MAX_NEG_IDZERO (47, 1/2, 63/2, 0, True)
SYMPY_VERDICT PASS
```
No prior residual ledger was used to compute either replay; the old deposited manifest was consulted only afterward for a metric-consistency check, which returned zero mismatches.

## Exact centered inputs reconstructed

**[COMPUTED]** For `I_i=[-a_i,b_i]`, define
```
n_i=1+a_i+b_i
d_ij=1+min(a_i,a_j)+min(b_i,b_j)
d_012=1+min(a_0,a_1,a_2)+min(b_0,b_1,b_2).
```
For a state `g=(i,j,k)`, the exact weight and signed weak-order charge are
```
W(g)=1+[i=j]+[i=k]+[j=k]+2[i=j=k],
q(g)=[i<=j<=k]-[j<=k<=i]-[k<=i<=j]-2[k<=j<=i].
```
Thus `N=sum W(g)`, `Q_A=sum q(g)`, `L_1=sum_{i<0}W(g)`, `H_3=sum_{k>0}W(g)`, and
`S_L=N-3*L_1`, `S_H=N-3*H_3`.

**[PROVED-HERE]** Expanding the five constant/equality pieces of `W` gives the exact formulas used in every cell:
```
N = n0*n1*n2 + d01*n2 + d02*n1 + d12*n0 + 2*d012
L1 = a0*n1*n2 + min(a0,a1)*n2 + min(a0,a2)*n1
     + a0*d12 + 2*min(a0,a1,a2)
H3 = b2*n0*n1 + min(b2,b0)*n1 + min(b2,b1)*n0
     + b2*d01 + 2*min(b0,b1,b2).
```

**[PROVED-HERE]** For `s([-a,b],[-c,d])=sum_{x=-a}^b sum_{y=-c}^d sgn(y-x)`, direct splitting at the endpoints gives the four exact branches:
```
a<=c, b<=d: (a+b+1)*(a-b-c+d)
a<=c, b>=d: a^2-a*c+a*d+a-b*c-b*d-b-c+d^2+d
a>=c, b<=d: a*c+a*d+a-b^2-b*c+b*d-b-c^2-c+d
 a>=c, b>=d: (c+d+1)*(a-b-c+d).
```
Writing `J_01=I_0 intersection I_1` and `J_12=I_1 intersection I_2`, the exact signed expansion is
```
D=n2*s(I0,I1)+n0*s(I1,I2)+n1*s(I0,I2)
  +2*s(J01,I2)+2*s(I0,J12)
Q_A=(D-N)/2.
```
Statewise, the signed summand satisfies `d(g)-W(g)=2q(g)`, which proves the displayed signed identity once summed.

**[COMPUTED]** The Fraction replay independently checked the four signed branches on all `5^4=625` endpoint cases: `625` cases, `0` failures. It checked the closed formulas against direct finite-state enumeration on all `5^6=15625` centered endpoint boxes with each endpoint in `{0,1,2,3,4}`: `15625` cases, `0` formula failures, and `0` failures of `2*Q_A=D-N`.

## Chamber indexing and exact adopted table

**[PROVED-HERE]** The 13 weak endpoint-order patterns, used for both rows (`a`) and columns (`b`), are exactly
```
0: 012       1: 01|2       2: 02|1       3: 0|12
4: 0|1|2     5: 0|2|1     6: 12|0       7: 1|02
8: 1|0|2     9: 2|01       10: 2|0|1     11: 1|2|0
12: 2|1|0.
```
For ordered blocks at ranks `0,1,2`, their values are `x`, `x+1+z1`, `x+2+z1+z2`, with all `x,z1,z2>=0`; use independent `A0,A1,A2` and `B0,B1,B2` on the two sides. Taking the minimum and subtracting one from each successive distinct-value gap is the inverse map, so this includes zero endpoints, singleton intervals, equality faces, and containments.

**[COMPUTED]** The complete adopted repaired coefficient matrix, with rows and columns in that order, is:
```
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
row 10: (1/4,0) (1/2,1/2) (1/4,0) (1/2,1/2) (2/3,5/6) (1/2,1/2) (1/4,0) (1/4,0) (1/2,1/2) (1/4,0) (1/4,0) (1/4,0) (1/4,0)
row 11: (1/4,0) (1/2,1/2) (1/4,0) (1/2,1/2) (2/3,5/6) (1/2,1/2) (1/4,0) (1/3,1/6) (1/2,1/2) (1/4,0) (1/4,0) (1/2,0) (1/4,0)
row 12: (1/2,0) (5/6,2/3) (1/2,0) (5/6,2/3) (1,1) (5/6,2/3) (1/2,0) (1/2,0) (5/6,2/3) (1/2,0) (1/2,0) (1/2,0) (1/2,0)
```

## Exact replay of all cells

**[COMPUTED]** In each nonexceptional cell, the fresh implementation expanded in `QQ[A0,A1,A2,B0,B1,B2]`:
```
R = -Q_A - alpha*S_L - beta*S_H,
RHS = alpha*S_L + beta*S_H + R.
```
It compared every coefficient of `-Q_A` with the corresponding coefficient of `RHS` over the union of all supports, and recorded the residual coefficient and `identity_difference` in the ledger.

The exact fresh totals are:
```
supplied/original: total 169; nonexceptional 168; passes 167; failures 1;
                   EXC 1; identity mismatches 0; negative-residual cells 1.
repaired:         total 169; nonexceptional 168; passes 168; failures 0;
                   EXC 1; identity mismatches 0; negative-residual cells 0.
```
The repaired summary has 169 data records: 168 `PASS` and one `EXC`. The repaired coefficient ledger has exactly `6792` coefficient-comparison data rows (plus its header), every recorded `identity_difference` is zero, and every repaired residual coefficient is nonnegative. Across all repaired residual supports, the exact coefficient minimum is `1/4` and maximum is `59`.

**[PROVED-HERE]** Therefore, cell by cell for all 168 nonexceptional chambers,
```
-Q_A = alpha*(N-3*L_1) + beta*(N-3*H_3) + R,
```
with the table's rational nonnegative `alpha,beta` and coefficientwise nonnegative `R`. This conclusion is a finite exact coefficient proof, not a floating-point or sampled inference.

### Explicit row (11,11) check

**[COMPUTED]** Both endpoint patterns are `1|2|0`, with
```
a=(A0+A1+A2+2, A0, A0+A1+1),
b=(B0+B1+B2+2, B0, B0+B1+1).
```
For the original entry `(1/4,0)`, the residual has support 49, minimum `-1/2`, maximum `51/2`, and its only negative coefficients are
```
A2*B1       = -1/2
A2*B0*B1    = -1/2
A0*A2*B1   = -1/2.
```
For the adopted repaired entry `(1/2,0)`, the fresh ledger has 55 compared monomials, zero identity mismatches, residual support 47, minimum `1/2`, maximum `63/2`, and zero negative coefficients. Its complete nonzero residual is:
```
1=27/2; B2=4; B1=2; B1*B2=1/2; B0=33/2; B0*B2=5; B0*B1=2; B0*B1*B2=1/2; B0^2=3; B0^2*B2=1; A2=2; A2*B0=5/2; A2*B0^2=1/2; A1=23/2; A1*B2=3/2; A1*B1=3/2; A1*B0=13; A1*B0*B2=3/2; A1*B0*B1=3/2; A1*B0^2=3/2; A1*A2=1; A1*A2*B0=1; A1^2=3/2; A1^2*B0=3/2; A0=63/2; A0*B2=5; A0*B1=5; A0*B1*B2=1/2; A0*B0=33/2; A0*B0*B2=2; A0*B0*B1=3/2; A0*B0^2=3/2; A0*A2=5/2; A0*A2*B0=1; A0*A1=16; A0*A1*B2=3/2; A0*A1*B1=3/2; A0*A1*B0=9/2; A0*A1*A2=1; A0*A1^2=3/2; A0^2=27/2; A0^2*B2=1; A0^2*B1=3/2; A0^2*B0=3; A0^2*A2=1/2; A0^2*A1=3; A0^3=3/2.
```

**[COMPUTED]** The exact old-defect witness uses `(A0,A1,A2)=(0,0,14)`, `(B0,B1,B2)=(0,7,0)`, giving
```
a=(16,0,1), b=(9,0,8),
(N,L1,H3,D,Q_A)=(308,177,224,420,56),
(S_L,S_H)=(-223,-364),
R_old=-1/4, R_new=111/2.
```
This independently exhibits the original-table failure and the repaired-cell positivity; it is not used to certify any other cell.

## The separate exceptional cell

**[COMPUTED]** Row 6, column 1 is `a=12|0`, `b=01|2`. Put
```
a=(p+1+u,p,p), b=(q,q,q+1+v), p,q,u,v>=0.
```
The exact substitution gives
```
Q_A=-(p+q+1)/2 * R,
R=p^2+2*p*q-p*u-p*v+3*p+q^2-q*u-q*v+3*q-2*u*v-4*u-4*v,
```
and
```
S_L+S_H = -p^3-3*p^2*q-p^2*u-4*p^2*v-8*p^2
          -3*p*q^2-5*p*q*u-5*p*q*v-16*p*q
          -4*p*u*v-7*p*u-13*p*v-12*p
          -q^3-4*q^2*u-q^2*v-8*q^2-4*q*u*v-13*q*u-7*q*v-12*q
          -4*u*v-6*u-6*v+4.
```

**[PROVED-HERE]** If `u+v>=1`, the displayed negative terms give
`S_L+S_H <= 4-6u-6v-4uv <= -2`. If `u=v=0` and `p+q>=1`, the `-12p-12q` terms give `S_L+S_H <= 4-12(p+q) <= -8`. Thus simultaneous `S_L>0` and `S_H>0` forces `p=q=u=v=0`. At that base point, exact direct enumeration gives
```
T_(123,132,213,231,312,321)=(4,2,2,1,1,1),
(N,L1,H3,Q_A)=(11,3,3,0),
(S_L,S_H)=(2,2).
```
The direct exceptional formula check covered `4^4=256` parameter points with zero failures. The inequalities, rather than this bounded check, prove the exceptional implication.

## Common-cut translation and boundary

**[ARGUED]** For a legal interval triple with a specified common integer cut `t`, write `a_i=t-A_i` and `b_i=B_i-t`; translating every integer state by `-t` sends the triple to `[-a_i,b_i]`. Equalities and order inequalities, hence `W`, `q`, `N`, and `Q_A`, are preserved; the strict tails are preserved because the cut is translated with the intervals. Thus the centered replay is exactly lossless for the stated common-cut scope.

**[FAILED-AT — explicitly outside this charge]** No certificate or theorem claim is made for triples with no common integer cut, or for a fixed external cut held fixed while intervals are translated. The present artifact does not supply the hypotheses needed for those cases, and they were not silently accepted.

## Final disposition

**[PROVED]** The repaired centered common-cut certificate is verified: 168/168 nonexceptional cells have exact coefficientwise nonnegative residuals, the repaired row `(11,11)` is `(1/2,0)` and passes explicitly, all coefficient identity mismatches are zero, and the one exceptional cell is handled by the exact argument above.

**[CONTESTED]** The original source table is rejected as written solely because its row `(11,11)` `(1/4,0)` residual has the three displayed negative `-1/2` coefficients and the exact witness `R_old=-1/4`. This defect is not attributed to the repaired artifact.

**[COMPUTED]** The persistence-floor attack was answered by the independent SymPy replay, which returned `168` cells, `1` exception, `0` identity failures, `0` negative cells, global coefficient range `[1/4,59]`, and a passing row-11 record. No missing load-bearing artifact remains.

## Transient implementation-attempt record

**[FAILED-AT — transient, non-mathematical, corrected]** The first Fraction-driver invocation stopped before emitting results because `Poly.__pow__` had not been implemented (`TypeError: unsupported operand type(s) for ** or pow(): 'Poly' and 'int'`). The corrected runner added that routine and reran successfully.

**[FAILED-AT — transient, non-mathematical, corrected]** The next invocation reached the post-replay diagnostic manifest check but used nonexistent keys `residual_support`, `residual_min`, `residual_max` (`KeyError: 'residual_support'`). The check was corrected to the deposited manifest's `repair_support`, `repair_min`, `repair_max`; the exact replay itself had already completed, and the corrected run returned all totals quoted above.

**[FAILED-AT — transient, non-mathematical, corrected]** The first independent SymPy invocation used `diff.is_zero()` although SymPy exposes `is_zero` as a Boolean property (`TypeError: 'bool' object is not callable`). The corrected persisted SymPy script used `diff.is_zero` and passed with the quoted totals. None of these transient API/driver errors is a mathematical cell failure or a missing artifact.


---
provenance: actor=work_math_manager_streaming work_id=work_7976cf608d39 node_id=deepcheck-repaired-ch-global-residuals-next banked=2026-08-17T23:33:25Z

## Provenance

- work_math_manager_streaming | work_7976cf608d39 | deepcheck-repaired-ch-global-residuals-next | imported from wiki entry deepcheck-repaired-ch-global-residuals-next



---

## Banked record: `exceptional-weak-chamber-ch-certificate`

# exceptional-weak-chamber-ch-certificate

title: Exceptional Weak-Chamber CH Certificate
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Exact substitution gives a slack-sum polynomial that is nonpositive whenever u+v>=1, or whenever p+q>=1 with u=v=0; the only possible strict-tail point is therefore the all-zero base case.
[graph-node: kgn_451ec098ed95 — this page is a PROJECTION; truth lives in the research KG]

## Statement

In the sole exceptional weak chamber, parameterized by a_2=a_3=p, a_1=p+1+u, b_1=b_2=q, and b_3=q+1+v with p,q,u,v>=0, simultaneous positivity of N-3L_1 and N-3H_3 forces p=q=u=v=0. At that base point Q_A=0. Hence CH also holds throughout the exceptional chamber.

## Content

In the sole exceptional weak chamber, parameterized by a_2=a_3=p, a_1=p+1+u, b_1=b_2=q, and b_3=q+1+v with p,q,u,v>=0, simultaneous positivity of N-3L_1 and N-3H_3 forces p=q=u=v=0. At that base point Q_A=0. Hence CH also holds throughout the exceptional chamber.

## Provenance

- supervisor | work_659c2ea2cb36 | banked per finding at effort end




# Theorems 11.1-11.2 (V foundation; V-CH vacuity)

---

## Banked record: `v-lambda-uniform-three-defect-foundation-audit-round-28-corr`

# v-lambda-uniform-three-defect-foundation-audit-round-28-corr

title: Corrected V/Lambda Three-Defect Foundation Audit
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Legal gap intervals are shown nonempty, and singleton intervals would make C∪{u} an (m+1)-element chain, contradicting maximality. Feasible gap maps are partitioned into canonical fibers with weight W(g)=∏_r e(P[B_r]); in the V case the exact weight is 1+1_{j=k}, yielding sibling marginal monotonicity and forcing both sibling defects to have the same heavy gap, contradicting pairwise distinctness. Order duality and gap reflection transfer the exclusion to the Lambda case.
[graph-node: kgn_af072f7e8e57 — this page is a PROJECTION; truth lives in the research KG]

## Statement

For finite posets with a maximum chain of size m, exactly three off-chain defects, CLOSED-THIRD avoidance, and V- or Lambda-shaped defect order, the corrected foundation is proved: every defect has a non-singleton legal gap interval, the canonical fiber model and exact V-weight formula hold, and pairwise-distinct unique heavy gaps are impossible in both V and Lambda cases. The correction is that a one-defect chain extension has size |C∪{u}|=m+1, not m+2; all downstream conclusions remain valid.

## Content

# V/Lambda Uniform Three-Defect Foundation Audit — Round 28 (Corrected)

status: proved
scope: Finite posets P with a maximum chain C of cardinality m, exactly three off-chain defects, CLOSED-THIRD avoidance, and V- or Lambda-shaped induced defect order; excludes pairwise-distinct unique heavy gaps.
depends on: uniform-arbitrary-k-gap-map-realization-and-canonical-fiber; corrected-three-defect-ledger-interface-statement; exact-three-defect-chain-cut-ledger; exact-three-defect-defect-pair-ledger; fully-tied-three-defect-fiber-calibration; heavy-gap-rigidity-under-closed-third-avoidance

# Corrected outcome

**PROVED.** The false cardinality `|C∪{u}|=m+2` is replaced everywhere by the correct identity `|C∪{u}|=m+1`. Every charged V/Lambda conclusion survives unchanged.

## Uniform legal-gap foundation and correction
For an off-chain defect u define its legal chain-gap interval `I_u=[a_u,b_u]⊆{0,…,m}` in the usual way: a gap r is legal iff every chain predecessor c_t<u has t≤r and every chain successor u<c_t has r<t. Initial/final-segment transitivity gives a_u≤b_u, so I_u is nonempty. If `I_u={r}`, then u is comparable with every element of C and inserts at its unique position (before c_1, between c_r and c_{r+1}, or after c_m). Hence `C∪{u}` is a chain and, because u∉C,
`|C∪{u}|=m+1`.
This contradicts that C is a maximum-cardinality m-chain. Therefore every off-chain defect has `|I_u|≥2`. The former `m+2` literal was used only in this singleton-window contradiction; replacing it by m+1 proves the same contradiction.

## Exact uniform fiber model
For a defect gap map g, feasibility means `g(u)∈I_u` and `u<v` among defects implies `g(u)≤g(v)`. With `B_r=g^{-1}(r)`, the canonical block bijection gives
`W(g)=∏_r e(P[B_r])`, and `e(P)=Σ_g W(g)`.
Unrestricted Cartesian feasibility in the presence of defect relations is false and is not used.

## V branch
Write the V order as `p<q`, `p<r`, `q∥r`, with gaps `(i,j,k)`. Feasible states are exactly
`i∈I_p, j∈I_q, k∈I_r, i≤j, i≤k`,
and the tied-block calculation gives
`W(i,j,k)=1+1_{j=k}`.
After interchanging q,r if needed, write `I_q=[a,b]`, `I_r=[c,d]` with b≤d. Incomparability q∥r forces c≤b, and p<q forces the right endpoint of I_p to be ≤b. The exact sibling marginals are
`M_q(j)=Σ_{i∈I_p,i≤j}|I_r∩[i,m]| + 1_{j∈I_r}|I_p∩(-∞,j]|`,
`M_r(k)=Σ_{i∈I_p,i≤k}|I_q∩[i,m]| + 1_{k∈I_q}|I_p∩(-∞,k]|`.
Thus M_q is nondecreasing on I_q, so its unique heavy gap is b. The function M_r is nondecreasing through b; for k>b its first term is constant and its diagonal term vanishes, whereas at b the diagonal contributes `|I_p|>0`. Hence `M_r(b)>M_r(k)` for every k>b. Heavy-gap uniqueness forces the heavy gap of r also to be b. Therefore the sibling heavy gaps coincide, contradicting pairwise distinctness. This proves the V exclusion.

## Lambda branch
Order duality sends Lambda to V. Reversing C reflects gaps by `s=m-r`, sends `[a_u,b_u]` to `[m-b_u,m-a_u]`, bijects feasible maps and tied-block linear extensions, preserves N and maximum-chain status, and gives `M_u^*(s)=M_u(m-s)`. CLOSED-THIRD avoidance is preserved because orientation probabilities change by p↦1-p, and pairwise distinctness of heavy gaps is preserved by reflection. The proved V exclusion therefore yields the Lambda exclusion.

## Dependency and downstream audit
The noncircular chain is: legal gaps → feasible maps/canonical fibers → exact V weight → sibling marginal monotonicity → V exclusion; heavy-gap rigidity supplies only existence/uniqueness of heavy gaps. Lambda uses only the explicit duality bijection. Neither exclusion is used to prove any dependency.

The corrected m+1 argument preserves unchanged: non-singleton legal intervals; genuine endpoint cuts; the V feasible-state set; `W=1+1_{j=k}`; the sibling endpoint contradiction; Lambda reflection; and exclusion of pairwise-distinct heavy gaps in both shapes. A separate three-chain count m+2 in the recovered artifact is legitimate because it uses three defects while omitting one chain element; it is unrelated to the corrected one-defect count.

Final label: **PROVED**. No downstream conclusion becomes unsupported.

---
provenance: actor=work_math_manager_streaming work_id=work_39ddcfed4a36 node_id=v_lambda_uniform_foundation_correction banked=2026-08-17T23:50:09Z

## Edges

- depends_on -> Uniform arbitrary-k gap-map realization and canonical fiber theorem (kgn_db3be885c74b)
- depends_on -> Corrected Three-Defect Ledger Interface (kgn_2d30c290f545)
- depends_on -> Exact Three-Defect Chain-Cut Ledger (kgn_88e7aca374de)
- depends_on -> Exact Three-Defect Defect-Pair Ledger (kgn_d0c557800cab)
- depends_on -> Fully Tied Three-Defect Fiber Calibration (kgn_34a50bcd46c7)
- depends_on -> Heavy-Gap Rigidity Under Closed-Third Avoidance (kgn_61fdce45cbe7)

## Provenance

- work_math_manager_streaming | work_39ddcfed4a36 | v_lambda_uniform_foundation_correction | imported from wiki entry v-lambda-uniform-three-defect-foundation-audit-round-28-corr



---

## Banked record: `every-realizable-gated-common-heavy-v-configuration-fails-cl`

# every-realizable-gated-common-heavy-v-configuration-fails-cl

title: Universal V Common-Heavy Closed-Third Exclusion Theorem
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Uses exact weighted marginal formulas for the lower defect and one sibling, together with their monotonicity. The strict lower- and upper-tail inequalities in CH_V force any common-heavy gap to be simultaneously h=A and h=D; the normalized endpoint constraints then force I_q to be the singleton {h}, which yields the remaining contradiction. The argument works directly from the guarded executable model and does not rely on the excluded round-17, strong-order, pinned-inequality, finite-scan, or Lambda claims.
[graph-node: kgn_2755dbce013c — this page is a PROJECTION; truth lives in the research KG]

## Statement

For every realizable normalized V-configuration in the authoritative executable model, with defect order p<q, p<r, and q∥r, there is no gap h satisfying the common-heavy predicate CH_V(h). Consequently, no realizable V-instance can satisfy the V common-heavy candidate conjunction, and in particular every realizable common-heavy V-configuration fails closed-third avoidance.

## Content

# Every realizable gated common-heavy V configuration fails closed-third avoidance

# Universal V Common-Heavy Closed-Third Exclusion Theorem (Corrected Guarded Model)

**OUTCOME: PROVED.**

## 1. Exact statement and scope

**[PROVED-HERE — theorem]** For every integer `m >= 0`, every normalized endpoint tuple admitted by the authoritative executable model, and every exact `REALIZABLE_V` instance with defect order

\[
p<q,\qquad p<r,\qquad q\parallel r,
\]

there is no raw gap `h` for which `CH_V(h)` holds. Consequently

\[
\mathsf{REALIZABLE}_V\ \wedge\ \exists h\,\mathsf{CH}_V(h)
\quad\Longrightarrow\quad
\neg\mathsf{AVOID\_CLOSED\_THIRD}_V,
\]

and, more strongly, the executable conjunction

\[
\mathsf{V\_CH\_CANDIDATE}
 =\mathsf{REALIZABLE}_V\wedge(N>0)\wedge
  \mathsf{AVOID\_CLOSED\_THIRD}_V\wedge
  \exists h\,\mathsf{CH}_V(h)
\]

has no realizable tuple. The proof below is stronger than the requested implication: it rules out `REALIZABLE_V` together with `CH_V` before the avoidance predicate is tested.

No contested round-17 all-coincident lemma, strong-order theorem, pinned inequality, finite scan, or Lambda claim is used as a premise.

## 2. Authoritative executable interface (restated literally)

**[ARGUED — exact banked predicate interface, not a reinterpretation]** Normalize the siblings by swapping `q,r` if necessary so that `D <= F`. Put

\[
I_p=[A,B],\qquad I_q=[C_0,D],\qquad I_r=[E,F]
\]

as closed integer intervals in `{0,...,m}`. The authoritative normalized endpoint domain is

\[
0\le A\le B\le m,\quad
0\le C_0\le D\le m,\quad
0\le E\le F\le m,
\]
\[
A\le C_0,\quad A\le E,\quad B\le D,\quad E\le D,\quad D\le F.
\tag{D}
\]

The exact feasible gap set and weight are

\[
\Gamma=\{(i,j,k):i\in I_p,\ j\in I_q,\ k\in I_r,\ i\le j,\ i\le k\},
\]
\[
W(i,j,k)=1+\mathbf 1_{j=k},\qquad
N=\sum_{(i,j,k)\in\Gamma}W(i,j,k).
\tag{F}
\]

For `g_p=i,g_q=j,g_r=k`, the authoritative marginal masses are

\[
L_u(h)=\sum_\Gamma W\mathbf1_{g_u<h},\qquad
M_u(h)=\sum_\Gamma W\mathbf1_{g_u=h},\qquad
U_u(h)=\sum_\Gamma W\mathbf1_{g_u>h}.
\tag{M}
\]

The exact common-heavy predicate is

\[
\mathsf{CH}_V(h)\iff
\forall u\in\{p,q,r\}:
\quad 3L_u(h)<N,\quad 3M_u(h)>N,\quad 3U_u(h)<N.
\tag{CH}
\]

For an orientation numerator `S`, the exact closed-third avoidance test is

\[
\mathsf{OUTSIDE\_CLOSED\_THIRD}(S,N)
\iff (3S<N)\ \text{or}\ (3S>2N).
\]

`AVOID_CLOSED_THIRD_V` applies this test to `O(q<r)` and to every `O(u<c_t)` with the genuine incomparability condition `a_u<t<=b_u`; forced pairs are omitted exactly as in the authoritative entry. Equality at either boundary is forbidden. None of this avoidance predicate is assumed in the V proof until the final logical consequence.

Finally, `REALIZABLE_V` is not the cheap numerical domain (D) alone. It constructs the transitive closure from the endpoint relations and `p<q,p<r`, and requires acyclicity, `q||r`, `height(P)=m`, and connectedness of the incomparability graph. This distinction is used below.

## 3. Exact marginal formulas

**[PROVED-HERE — formula for the lower defect]** For `i in I_p`, define

\[
Q_i=|I_q\cap[i,m]|,\qquad R_i=|I_r\cap[i,m]|,
\qquad T_i=|I_q\cap I_r\cap[i,m]|.
\]

For fixed `i`, the feasible `(j,k)` choices are exactly the two suffixes `j in I_q, j>=i` and `k in I_r, k>=i`. Every choice contributes one, and the diagonal `j=k` contributes one additional extension. Hence

\[
M_p(i)=Q_iR_i+T_i.
\tag{1}
\]

This is an exact integer identity, including endpoint and singleton intervals and the fully tied state (which has weight two, not six).

**[PROVED-HERE — formula for the selected sibling]** For `j in I_q`, fixing `j` and summing over `i,k` gives

\[
M_q(j)=
\sum_{\substack{i\in I_p\\ i\le j}}|I_r\cap[i,m]|
+\mathbf1_{j\in I_r}\,|I_p\cap(-\infty,j]|.
\tag{2}
\]

The first term counts the base contribution for each feasible `i` and `k`; the second is exactly the extra diagonal contribution `k=j`, which exists precisely when `j in I_r` and `i<=j`. Formula (2) retains the `+1` diagonal correction at every `j=k`, including `i=j=k`.

## 4. Monotonicity and endpoint forcing

**[PROVED-HERE — monotonicity]** The three quantities `Q_i,R_i,T_i` in (1) are nonincreasing as `i` increases. They are nonnegative, so their product `Q_iR_i` is nonincreasing, and therefore

\[
M_p(i)\ \text{is nonincreasing on }I_p.
\tag{3}
\]

In (2), the first summand is nondecreasing in `j`, because its set of permitted `i` only expands. The function

\[
K(j)=|I_p\cap(-\infty,j]|
\]

is nondecreasing. On the interval `I_q=[C_0,D]`, the indicator `1_{j in I_r}` is also nondecreasing: by (D), `E<=D<=F`, so within `I_q` membership in `I_r=[E,F]` is zero up to the possible threshold `E` and one thereafter (or one throughout). The product `1_{j in I_r}K(j)` is consequently nondecreasing. Thus

\[
M_q(j)\ \text{is nondecreasing on }I_q.
\tag{4}
\]

No monotonicity claim about an unneeded unrestricted marginal is being smuggled in; (3) and (4) are the only two used.

**[PROVED-HERE — a common heavy gap must be both endpoints]** Assume `N>0` and `CH_V(h)`. Since `M_u(h)>N/3>0` for each `u`, the gap `h` belongs to every legal interval, in particular `h in I_p cap I_q`.

If `h>A`, then (3) gives

\[
M_p(A)\ge M_p(h)>N/3.
\]

Because `A<h`, the strict lower tail contains the entire atom at `A`, so

\[
L_p(h)=\sum_{s<h}M_p(s)\ge M_p(A)>N/3,
\]

contradicting the literal strict CH inequality `3L_p(h)<N`. Therefore

\[
h=A.\tag{5}
\]

If `h<D`, then (4) gives

\[
M_q(D)\ge M_q(h)>N/3.
\]

Because `D>h`, the strict upper tail contains the atom at `D`, so

\[
U_q(h)=\sum_{s>h}M_q(s)\ge M_q(D)>N/3,
\]

contradicting the literal strict CH inequality `3U_q(h)<N`. Therefore

\[
h=D.\tag{6}
\]

Equations (5) and (6) yield `A=D=h`. The normalized endpoint inequalities give

\[
A\le C_0\le D,
\]

so `C_0=A=D=h`; hence

\[
I_q=[C_0,D]=\{h\}.
\tag{7}
\]

The proof used the strict CH tails exactly as written. It did not replace them by an atom-only condition, and it did not treat equality at `N/3` as if it satisfied CH.

## 5. The singleton contradiction is the realizability gate

**[PROVED-HERE — exact height obstruction]** If `I_q={h}`, the endpoint definition gives, for every `t` in `{1,...,m}`,

\[
c_t<q\iff t\le h,
\qquad
q<c_t\iff t>h.
\]

There is no `t` with `h<t<=h`, so q is comparable with every chain element. Thus, with empty portions omitted at `h=0` or `h=m`,

\[
c_1<\cdots<c_h<q<c_{h+1}<\cdots<c_m
\]

is a chain of `m+1` elements. This contradicts the exact `REALIZABLE_V` guard `height(P)=m`. The same argument covers `m=0`: adjoining q to the empty displayed chain already gives a chain longer than zero.

Therefore `REALIZABLE_V` and `CH_V(h)` are incompatible for every `h`.

**[PROVED-HERE — universal V conclusion]** We have proved the stronger quantified statement

\[
\boxed{
\forall m,\forall\text{ normalized endpoint tuples},\quad
\mathsf{REALIZABLE}_V\Longrightarrow
\neg\exists h\in\{0,\ldots,m\}\,\mathsf{CH}_V(h).
}
\tag{8}
\]

Since the executable candidate predicate includes both `REALIZABLE_V` and `exists h CH_V(h)`, it is empty. In particular every realizable gated common-heavy V configuration fails the requested closed-third-avoidance conjunction; in fact no realizable gated common-heavy V configuration reaches that conjunction at all.

## 6. Explicit Lambda consequence by order duality only

**[PROVED-HERE — Lambda duality]** Let `P` instead have the Lambda defect order

\[
q<p,\qquad r<p,\qquad q\parallel r,
\]

with the same type of displayed maximum chain `C=(c_1<...<c_m)`. Do not import a Lambda closure claim. Form the order dual `P^vee`, and write its displayed chain as

\[
d_s=c_{m+1-s}\qquad(1\le s\le m).
\]

Then `P^vee` has the V order `p<q,p<r,q||r`.

For a linear extension `L` of P, reverse its word to obtain `L^vee`, a linear extension of `P^vee`. If a defect has original gap `x`, it has dual gap `m-x`. Hence the exact interval transformation is

\[
[a_x,b_x]\longmapsto[m-b_x,m-a_x].
\tag{9}
\]

The Lambda feasible inequalities `j<=i,k<=i` transform under

\[
(i,j,k)\longmapsto(m-i,m-j,m-k)
\]

to the V inequalities `i^vee<=j^vee,i^vee<=k^vee`. Equality `j=k` is preserved, so the exact tied-sibling weight `1+1_{j=k}` is preserved state by state. Reversing each local tied-block word gives the same conclusion directly from the canonical fiber bijection. Thus the map is a weight-preserving bijection and

\[
N(P^vee)=N(P).
\tag{10}
\]

For every defect `x`, if `M_x,L_x,U_x` are the original Lambda masses and starred quantities are the dual V masses, then at `s=m-h`

\[
M_x^*(s)=M_x(h),\qquad
L_x^*(s)=U_x(h),\qquad
U_x^*(s)=L_x(h).
\tag{11}
\]

Therefore a common-heavy gap `h` in Lambda becomes the common-heavy gap `m-h` in V: the two strict tails simply exchange and the strict heavy-atom inequality is unchanged.

The event numerators transform explicitly as follows. Reversal of a word gives, for any incomparable defect pair,

\[
O_{P^vee}(x<y)=O_P(y<x)=N-O_P(x<y).
\tag{12}
\]

For an eligible defect-chain pair, put `t=m+1-s`, so that `d_s=c_t`. Then

\[
O_{P^vee}(x<d_s)
 =O_P(c_t<x)
 =N-O_P(x<c_t).
\tag{13}
\]

Eligibility is preserved exactly: `a_x<t<=b_x` is equivalent, under `s=m+1-t`, to

\[
m-b_x<s\le m-a_x,
\]

which is the dual interval condition. Thus all and only genuine defect-chain events are paired; forced pairs remain outside the avoidance predicate.

The closed-third test is invariant under these complements. Indeed,

\[
S<N/3\Longleftrightarrow N-S>2N/3,
\qquad
S>2N/3\Longleftrightarrow N-S<N/3,
\]

and `S=N/3` maps to `N-S=2N/3`, while `S=2N/3` maps to `N-S=N/3`. Hence the closed interval, including both equality boundaries, is preserved. The sibling event `q<r` is covered by (12), and every eligible chain event by (13).

Finally, order duality preserves acyclicity, incomparability of q and r, maximum-chain height, and the incomparability graph. It also preserves `N>0`. If the reflected V endpoint tuple is not in the canonical `D<=F` sibling labeling, swap q and r; this only complements the sibling orientation and leaves both CH and the outside-closed-third predicate invariant.

Consequently, a realizable Lambda instance satisfying common CH and closed-third avoidance would dualize to a realizable V instance satisfying common CH and closed-third avoidance, contradicting (8). Therefore the Lambda/common-heavy consequence is

\[
\boxed{
\mathsf{REALIZABLE}_\Lambda\wedge
\exists h\,\mathsf{CH}_\Lambda(h)
\Longrightarrow
\neg\mathsf{AVOID\_CLOSED\_THIRD}_\Lambda,
}
\]

and this consequence has been obtained only through the explicit duality (9)--(13), with its hypotheses and event numerators checked.

## 7. Adversarial checks and honesty boundary

**[ARGUED — circularity check]** The proof consumes only the authoritative V endpoint domain, exact feasible set, exact weight, exact marginal definitions, and the `height(P)=m` component of `REALIZABLE_V`. It does not consume `AVOID_CLOSED_THIRD_V`, heavy-gap rigidity, a strong-order theorem, the contested all-coincident lemma, a pinned inequality, or any finite scan. The conclusion is therefore not circular.

**[PROVED-HERE — singleton and endpoint check]** CH positivity first forces `h` into every interval. The monotonicity argument remains valid for singleton intervals and for `h=0` or `h=m`; no division, limiting argument, or fictitious gap `-1` or `m+1` occurs. The singleton outcome is rejected by the exact height guard, not by an informal nondegeneracy assumption. In particular, the necessary strict window consequence `C_0<D` is derived from maximum-chain status rather than substituted for it.

**[ARGUED — gate-versus-realizability check]** The numerical inequalities (D) are used only as necessary consequences of the authoritative normalized realization interface. They are not claimed sufficient. Acyclicity, q/r incomparability, height, and incomparability-graph connectedness remain the exact realizability scope; height is the guard that closes (7).

**[PROVED-HERE — strict-versus-closed-third check]** The contradiction uses the strict CH inequalities `3L<N` and `3U<N` and the strict atom inequality `3M>N`. The avoidance predicate is separately the closed interval `[N/3,2N/3]`; its equality cases are retained, and duality maps the two equality faces into one another.

**[ARGUED — no scan substitution]** The bounded scans mentioned in the route context are not used to discharge (8). They are, at most, COMPUTED corroboration. The universal step is the two marginal monotonicity derivation plus the exact height contradiction.

## 8. In-session computation ledger (corroboration only)

**[COMPUTED — not a proof of (8)]** The exact-integer script
`outputs/code/v_common_heavy_duality_audit_20260818.py` was executed in this session, and its output was persisted verbatim at
`outputs/v-common-heavy-duality-audit-20260818.txt`. It checked the formulas, the two monotonicities, degenerate normalized tuples, and the order-duality transformation. The exact output was:

```text
FORMULA_MONOTONICITY_AUDIT {'through_m': 6, 'normalized_checked': 5214, 'formula_bad_on_legal': 0, 'p_q_monotonicity_bad': 0, 'CH_hits': 28, 'CH_hits_q_nonsingleton': 0, 'CH_hits_all_nonsingleton': 0}
FIRST_CH_HITS [(0, (0, 0, 0, 0, 0, 0), 0, 2, [(0, 2, 0), (0, 2, 0), (0, 2, 0)]), (1, (0, 0, 0, 0, 0, 0), 0, 2, [(0, 2, 0), (0, 2, 0), (0, 2, 0)]), (1, (1, 1, 1, 1, 1, 1), 1, 2, [(0, 2, 0), (0, 2, 0), (0, 2, 0)])]
SINGLETON_WITNESS {'m': 1, 'tuple': (0, 0, 0, 0, 0, 0), 'h': 0, 'N': 2, 'structural_checks': {'acyclic': True, 'qr_incomp': True, 'height': 3, 'connected': False}}
DUALITY_AUDIT {'V_tuple': (0, 1, 0, 2, 1, 2), 'V_N': 14, 'V_qr': 8, 'Lambda_reflected_intervals': (1, 2, 0, 2, 0, 1), 'Lambda_N': 14, 'Lambda_qr': 6, 'state_reflection_weight_bijection': True, 'marginal_reflection': [True, True, True], 'qr_complement': True, 'all_chain_complement_checks': [True, True, True, True, True, True], 'original_structural': {'acyclic': True, 'qr_incomp': True, 'height': 2, 'connected': True}}
```

The scan's 28 normalized CH hits are boundary/singleton records; none has `C_0<D`, exactly as the proof predicts. This computation is an audit, not the universal argument.

## 9. Final disposition

**[PROVED-HERE]** The requested V target is proved, with all quantifiers, endpoint boundaries, strict CH inequalities, closed-third equality boundaries, exact realizability scope, singleton cases, gate scope, and Lambda order-duality/event-numerator transformations checked. There is no unresolved lemma in the charged V or dual Lambda/common-heavy consequence.

**[FAILED — none]** No proof step stalled; no finite computation was promoted to a universal proof.


---
provenance: actor=work_math_manager_streaming work_id=work_f0c0995ee809 node_id=prove_v_common_heavy_vacuity banked=2026-08-18T07:42:37Z

## Provenance

- work_math_manager_streaming | work_f0c0995ee809 | prove_v_common_heavy_vacuity | imported from wiki entry every-realizable-gated-common-heavy-v-configuration-fails-cl



---

## Banked record: `lambda-common-heavy-vacuity-by-duality`

# lambda-common-heavy-vacuity-by-duality

title: Lambda Common-Heavy Vacuity by Duality
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Exact order duality transfers the V common-heavy impossibility to Lambda.
[graph-node: kgn_2124828500d2 — this page is a PROJECTION; truth lives in the research KG]

## Statement

No realizable authoritative guarded-Lambda configuration has a common heavy gap. Reflection of chain gaps by x↦m−x gives a weight-preserving bijection between the V and Lambda feasible-state systems, preserves the realizability guards, exchanges lower and upper tails, and sends each incomparable orientation numerator S to N−S. Therefore the proved emptiness of V-CH transfers exactly to L-CH, including all closed-third equality boundaries.

## Content

No realizable authoritative guarded-Lambda configuration has a common heavy gap. Reflection of chain gaps by x↦m−x gives a weight-preserving bijection between the V and Lambda feasible-state systems, preserves the realizability guards, exchanges lower and upper tails, and sends each incomparable orientation numerator S to N−S. Therefore the proved emptiness of V-CH transfers exactly to L-CH, including all closed-third equality boundaries.

## Provenance

- supervisor | work_f0c0995ee809 | banked per finding at effort end




# Theorem 11.3 (Two-equal partition)

---

## Banked record: `round-29-two-equal-cell-partition`

# round-29-two-equal-cell-partition

title: Round 29 Two-Equal Cell Partition
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Exhaustive case partition by defect shape, coincident heavy-index pair, and strict position of the separated third heavy index; the closed cases are discharged by the banked distinct-heavy exclusions and order-duality transfer.
[graph-node: kgn_11b04727840e — this page is a PROJECTION; truth lives in the research KG]

## Statement

In the exactly-two-equal heavy-index dispatch for the three-defect maximum-chain models, the configurations partition exhaustively into 5 V cells, 5 Lambda cells, and 4 Q cells, for 14 cells total. Eight cells are closed by previously banked exclusions or transfers, leaving exactly six genuinely open candidates: one V cell, one Lambda cell, and four Q cells. The sole V candidate is the tied-siblings configuration p<q, p<r, q parallel to r with rho_q=rho_r>rho_p; the sole Lambda candidate is its order-dual with rho_q=rho_r<rho_p; and the four Q candidates are tied x,y with z below or above, tied x,z with y above, and tied y,z with x below.

## Content

In the exactly-two-equal heavy-index dispatch for the three-defect maximum-chain models, the configurations partition exhaustively into 5 V cells, 5 Lambda cells, and 4 Q cells, for 14 cells total. Eight cells are closed by previously banked exclusions or transfers, leaving exactly six genuinely open candidates: one V cell, one Lambda cell, and four Q cells. The sole V candidate is the tied-siblings configuration p<q, p<r, q parallel to r with rho_q=rho_r>rho_p; the sole Lambda candidate is its order-dual with rho_q=rho_r<rho_p; and the four Q candidates are tied x,y with z below or above, tied x,z with y above, and tied y,z with x below.

## Provenance

- supervisor | work_d06eac75f5cd | banked per finding at effort end




# Theorem 11.4 (Full-Cone TE(2=1))

---

## Banked record: `full-cone-te-2-1-theorem-closing-v-2e-tied-siblings`

# full-cone-te-2-1-theorem-closing-v-2e-tied-siblings

title: Full-Cone TE(2=1) Theorem Closing V-2E Tied Siblings
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Canonical sibling normalization followed by an exhaustive disjoint two-case split and application of the independently replayed strict- and boundary-facet certificate atlases.
[graph-node: kgn_d9e87643b122 — this page is a PROJECTION; truth lives in the research KG]

## Statement

For every canonical realizable V-shaped three-defect instance in the tied-siblings TE(2=1) cell, canonical exchange of the two siblings gives D≤F. Hence exactly one of the mutually exclusive cases D<F and D=F holds. In the case D<F, the certified 31-chamber/62-certificate atlas `gated-te21-chamber-atlas-and-exact-certificates` gives N≤3 max(H,L). In the case D=F, the certified 31-chamber boundary atlases `exact-d-f-facet-certificate-atlas-for-guarded-te-2-1`, `normalized-d-f-0-te-2-1-facet-certificate-atlas`, and `independent-exact-replay-of-the-d-f-facet-atlas` give 3L-N=R_L with R_L coefficientwise nonnegative, and therefore N≤3L≤3 max(H,L). Thus every canonical realizable TE(2=1) point satisfies N≤3 max(H,L), and the V-2E tied-siblings cell is closed. This theorem is banked under `full-cone-te-2-1-theorem-closing-the-v-2e-tied-siblings-cell`.

## Content

For every canonical realizable V-shaped three-defect instance in the tied-siblings TE(2=1) cell, canonical exchange of the two siblings gives D≤F. Hence exactly one of the mutually exclusive cases D<F and D=F holds. In the case D<F, the certified 31-chamber/62-certificate atlas `gated-te21-chamber-atlas-and-exact-certificates` gives N≤3 max(H,L). In the case D=F, the certified 31-chamber boundary atlases `exact-d-f-facet-certificate-atlas-for-guarded-te-2-1`, `normalized-d-f-0-te-2-1-facet-certificate-atlas`, and `independent-exact-replay-of-the-d-f-facet-atlas` give 3L-N=R_L with R_L coefficientwise nonnegative, and therefore N≤3L≤3 max(H,L). Thus every canonical realizable TE(2=1) point satisfies N≤3 max(H,L), and the V-2E tied-siblings cell is closed. This theorem is banked under `full-cone-te-2-1-theorem-closing-the-v-2e-tied-siblings-cell`.

## Provenance

- supervisor | work_26117b285c41 | banked per finding at effort end



---

## Banked record: `gated-te21-chamber-atlas-and-exact-certificates`

# gated-te21-chamber-atlas-and-exact-certificates

title: Gated TE21 Chamber Atlas and Exact Certificates
type: computation | label: computed | verification: unverified
namespace: third23
mechanism: Exact chamber exhaustion with rational coefficientwise-nonnegative residual certificates, ledger-polynomial replay, boundary enumeration, and hash-checked artifact/code outputs; a separate explicit counterexample establishes the FAILED-AT interpretation of the unrestricted four-clause domain.
[graph-node: kgn_5eb432672414 — this page is a PROJECTION; truth lives in the research KG]

## Statement

An exact generator/replay for the normalized guarded-V domain enumerated 31 chamber parameterizations, 62 rational certificates, 70 Round-32 closed-boundary rows, and passed the reported identity and numerical checks. It also computed a precise failure mode for interpreting the four displayed gate clauses as the entire endpoint domain: the instance Ip=[1,2], Iq=[0,1], Ir=[0,2] violates the required order B<=D and makes the universal certificate impossible.

## Content

# Gated TE21 Chamber Atlas and Exact Certificates

# Gated TE(2=1) Chamber Atlas and Exact Certificates

**Status: COMPLETE for the actual normalized guarded-V domain; FAILED-AT if the four displayed gate clauses are read as the entire formal endpoint domain.**

The complete self-contained atlas, all 31 chamber parameterizations, all 62 exact rational certificates and expanded residual coefficient lists, exact ledger polynomials, all 70 Round-32 closed-boundary rows, and replay metadata are persisted at:

- `outputs/artifacts/gated_te21_chamber_atlas_20260817/atlas.md`
- `outputs/data/gated_te21_chamber_atlas_20260817.json`
- `outputs/code/gated_te21_chamber_atlas_20260817.py`

The executed generator/replay returned exactly:

```text
PATTERNS 31
CERTIFICATES 62
IDENTITY_REPLAY_CHECKS 49152
NUMERIC_SPOT_CHECKS 142125
BOUNDARY_70_COUNT 70
BOUNDARY_ALL_GATE True
BOUNDARY_ALL_EQUALITY_NO_INTERIOR True
BOUNDARY_ROWS_SHA256 f63ffa11ced10fec42edc3c97d979144d75148372619bce21e1ad58aa14f1a91
DATA_SHA256 59e2b841ce2cb653d900a73092165f1b78547f4bf6023c4b04adf677a878174
REPORT_SHA256 3541901a46c6e9603933d95546d3adb075df15570e6cc6134c7a67ed2c8777a7
```

## Exact model and certificate convention

The corrected guarded V model is `Gamma={(i,j,k): i<=j and i<=k}` with `W(i,j,k)=1+[j=k]`. If `X_<`, `X_>`, and `Y` are the unweighted `j<k`, `k<j`, and `j=k` slice counts, then
`N=X_<+X_>+2Y`, `O(q<r)=X_<+Y`, and `O(r<q)=X_>+Y`.
The exact r30 literals are `H=mass(i>A)=U_p(A)` and `L=mass(j<D)=L_q(D)`. The two branch identities are therefore
`3H-N = alpha*(N-3L)+beta*(N-3H)+R_H` and
`3L-N = alpha*(N-3L)+beta*(N-3H)+R_L`.
Every listed alpha,beta is rational and nonnegative, and every coefficient of every R is nonnegative in the chamber's nonnegative variables.

## Exhaustion and the gate distinction

For an actual V realization, `p<q` and `p<r` prove `B<=D` and `B<=F`. Swap q,r so `D<=F`; the sibling-overlap gate then gives `E<=D`. Translating `D=0` gives `A=-x,B=-y,C0=-c,E=-e,F=f` with `x>y>=0,c>=1,e>=0,f>=1`. The weak endpoint orders of `(x,y,c,e)` are exactly the 31 listed patterns. Each strict level gap is `1+z_i`, with `u,z_i,v>=0` and `F=1+v`; this is a bijective gate parameterization. No unrestricted-domain-only chamber is admitted.

If the four displayed clauses alone are treated as the entire formal endpoint domain, the requested universal certificate is impossible. The exact first obstruction is
`Ip=[1,2], Iq=[0,1], Ir=[0,2]`, which satisfies `A<B,C0<D,E<F` and sibling overlap but has `B>D`. Its exact ledger is `N=3,H=L=0`, so both branch left sides equal `-3`, while `N-3H=N-3L=3`; with alpha,beta>=0 and coefficientwise-nonnegative R the right side cannot be negative. This is the literal FAILED-AT boundary. It is not silently admitted to the actual normalized atlas.

## Independent Round-32 boundary replay

The exact 70 records at Pareto coordinates `(C,P)=(0,3)` were rebuilt from states and every eligible strict/weak chain orientation. All 70 satisfy the four-clause realizability gate, all have `N=3,H=L=0`, all have at least one equality face (`3S=N` or `3S=2N`), and none has an interior middle-third hit. The complete row/equality-event list and hash are in the JSON/report above. Equality-event counts are:

```text
sibling:q<r 70
chain:r<c2 8, chain:c2<r 8
chain:r<c3 18, chain:c3<r 18
chain:r<c4 24, chain:c4<r 24
chain:r<c5 20, chain:c5<r 20
```

This entry is a banked projection of the complete workspace artifact; the artifact itself contains the full derivations, residual expansions, machine-readable certificate data, exact replay code, and outputs.

---
provenance: actor=work_math_manager_streaming work_id=work_cfdbae0965ed node_id=gated_te21_chamber_atlas banked=2026-08-18T06:48:52Z

## Provenance

- work_math_manager_streaming | work_cfdbae0965ed | gated_te21_chamber_atlas | imported from wiki entry gated-te21-chamber-atlas-and-exact-certificates



---

## Banked record: `exact-d-f-facet-certificate-atlas-for-guarded-te-2-1`

# exact-d-f-facet-certificate-atlas-for-guarded-te-2-1

title: D=F Facet Bound for Guarded TE(2=1)
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Normalize by D=F and D=0, partition the parameter envelope into 31 exhaustive weak-order cells, derive exact affine endpoint and cubic N,H,L formulas, and verify that every residual 3L−N has nonnegative coefficients. An independent parser/replay reconstructs the identities and checks all cells and boundary fibers; the claimed result is also supported by the banked atlas, coefficient data, generator, and replay report.
[graph-node: kgn_169d5d6d9e5c — this page is a PROJECTION; truth lives in the research KG]

## Statement

On the omitted facet D=F (equivalently f=0), every realizable normalized instance satisfies N≤3L, and therefore N≤3 max(H,L). This is established by an exhaustive 31-cell weak-order chamber atlas over the larger envelope x>y≥0, c,e≥1, with coefficientwise-nonnegative residuals 3L−N and an independent replay certificate.

## Content

# Exact D=F Facet Certificate Atlas for Guarded TE(2=1)

# Exact D=F Facet Certificate Atlas for Guarded TE(2=1)

status: as labeled in the artifact (session deliverable, banked VERBATIM by the harness)

HEADLINE: [PROVED-HERE] The omitted facet D=F (f=0) is closed by the stronger inequality N <= 3L, hence N <= 3 max(H,L), on a 31-cell chamber envelope containing every realizable facet instance. The complete atlas, exact coefficient data, generator, independent replay, and report were banked under “TE(2=1) D=F Facet Chamber-and-Certificate Proof Object.”

[PROVED-HERE] Normalize by swapping q,r so D<=F and translating D to 0. On the omitted facet D=F, write (A,B,C0,D,E,F)=(-x,-y,-c,0,-e,0). Exact realizability and maximum-chain guards imply x>y>=0, c>=1, e>=1. Let R0 be the subset satisfying the full authoritative endpoint, acyclicity, q||r, height=m, and connected-incomparability guards. Then R0 is contained in E0={(x,y,c,e) in Z^4: x>y>=0, c>=1, e>=1}. The proof deliberately certifies the larger E0, so no sufficiency of E0 is required.

[ARGUED] The authoritative tied-siblings ledger is Gamma={(i,j,k): i in Ip, j in Iq, k in Ir, i<=j, i<=k}, with W(i,j,k)=1+[j=k]. For P=[a,b], Q=[q0,q1], R=[r0,r1], and (t)+=max(t,0), the exact slices are:
X_(j<k)=sum_{j=q0..q1} ((j-a+1)+-(j-b)+)((r1-j)+-(r0-1-j)+);
X_(k<j)=sum_{k=r0..r1} ((k-a+1)+-(k-b)+)((q1-k)+-(q0-1-k)+);
Y=sum_{h=max(q0,r0)..min(q1,r1)} ((h-a+1)+-(h-b)+);
V=X_(j<k)+X_(k<j)+2Y.
Thus N=V(Ip,Iq,Ir), H=V([A+1,B],Iq,Ir)=U_p(A), and L=V(Ip,[C0,D-1],Ir)=L_q(D). Strict tails are literal: i=A is excluded from H and j=D is excluded from L.

[PROVED-HERE] The exhaustive weak-order cells, listed in increasing level order with bars denoting strict inequality and letters in one block denoting equality, are:
0 y|xce; 1 yc|xe; 2 yce|x; 3 ye|xc; 4 c|y|xe; 5 c|ye|x; 6 ce|y|x; 7 e|y|xc; 8 e|yc|x; 9 y|c|xe; 10 y|ce|x; 11 y|e|xc; 12 y|x|ce; 13 y|xc|e; 14 y|xe|c; 15 yc|e|x; 16 yc|x|e; 17 ye|c|x; 18 ye|x|c; 19 c|e|y|x; 20 c|y|e|x; 21 c|y|x|e; 22 e|c|y|x; 23 e|y|c|x; 24 e|y|x|c; 25 y|c|e|x; 26 y|c|x|e; 27 y|e|c|x; 28 y|e|x|c; 29 y|x|c|e; 30 y|x|e|c. Each strict gap is 1+z_i with z_i>=0. The eight cells whose lowest level contains e use the shifted parameterization e=1+u: cells 3,7,8,17,18,22,23,24. Equality and lower faces, including e=1, c=1, y=0, and x=y+1, are explicit.

[COMPUTED] For every cell, the complete exact affine endpoint formulas and expanded N,H,L polynomials are stored in the JSON and human-readable atlas. Each cell has the exact expanded identity 3L-N=R_L. All 31 residuals have coefficientwise-nonnegative coefficients; there are 391 nonzero residual monomials in total, with smallest nonzero coefficient 1/2 and largest 31. Therefore every cell proves N<=3L, and hence N<=3 max(H,L).

[PROVED-HERE] The ledger expansion has total degree at most three in the nonnegative chamber variables. The generator solved the exact rational degree-3 interpolation problem and performed direct weighted-fiber checks on 0<=u,z_i<=6. The independent consumer does not use interpolation: it parses the stored rational coefficient lists, expands each identity coefficientwise, reconstructs endpoints from chamber blocks, and enumerates fibers directly.

[COMPUTED] Independent replay output:
PATTERN_COUNT 31
PATTERN_COVERAGE_BOX 2304
IDENTITY_EXPANSIONS 31
IDENTITY_RESIDUAL_TERMS 391
NEGATIVE_RESIDUAL_COEFFICIENTS 0
NEGATIVE_NHL_COEFFICIENTS 0
DIRECT_BOX_CHECKS 102459
BOUNDARY_EQUALITY_CHECKS 328
E_EQUALS_1_DOMAIN_ROWS 288
KNOWN_POINT x=2 y=1 c=2 e=2 f=0 parameters=pattern0(u=1,z0=0) N=18 H=6 L=11
KNOWN_POSET {'acyclic': True, 'q_parallel_r': True, 'height': 2, 'incomparability_connected': True, 'linear_extensions': 18, 'ledger': (18, 6, 11)}
ALL_CHECKS_PASS True

[COMPUTED] Complete banked files:
- atlas: outputs/artifacts/te21_D_eq_F_facet_atlas_20260818/atlas.md, SHA-256 e5cdb27fb431b3e0ef84c6edbc95dd2e525585ec665278cf67564aab6ab3f219;
- replay report: outputs/artifacts/te21_D_eq_F_facet_atlas_20260818/replay_report.txt, SHA-256 50303d6d5fc9d684d63723803d9bffbde719db2fb15f173ee3a5359256a0a791;
- coefficient data: outputs/data/te21_D_eq_F_facet_atlas_20260818.json, SHA-256 7aad8e7378dfe5475ba1dc3b8283e8250adf64dafe3359a0a0460b23c6288a5a;
- generator: outputs/code/generate_te21_D_eq_F_facet_atlas_20260818.py, SHA-256 8679af787466d8e8927d839abd048fde31d7c869491f2b0cf0b873910e70bcf4;
- independent replay: outputs/code/replay_te21_D_eq_F_facet_atlas_20260818.py, SHA-256 fce41ac04f3d13a50cb7ad099d7ee49d9067c7acdd0c529ce3daae66fa31a81d.

[COMPUTED] The known realizable point m=2, Ip=[0,1], Iq=Ir=[0,2] has normalized (x,y,c,e,f)=(2,1,2,2,0), endpoints (-2,-1,-2,0,-2,0), and (N,H,L)=(18,6,11). Its residual is 3L-N=15.

[ARGUED] Merger interface: use the existing certified f>=1 atlas unchanged for f>=1, and dispatch to this 31-cell atlas for f=0. The shared interface is W=1+[j=k], H=U_p(A), L=L_q(D), and D<=F. Existing atlas hashes recomputed in-session: markdown 3541901a46c6e9603933d95546d3adb075df15570e6cc6134c7a67ed2c8777a7; JSON 59e2b841ce2cb653d900a73092165f1b78547f4bf6023c4b04adf677a878174d; code 415b3d1260a3a767ad89f0bf17113312ac4b224f1913860124a8d22df53d59ca.

## Provenance

- kg_import | imported from wiki entry exact-d-f-facet-certificate-atlas-for-guarded-te-2-1



---

## Banked record: `normalized-d-f-0-te-2-1-facet-certificate-atlas`

# normalized-d-f-0-te-2-1-facet-certificate-atlas

title: D=F=0 Facet Bound for Normalized Guarded-V TE(2=1)
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Uses exact guarded state-enumeration formulas for N, H, and L, containment of realizable points in the normalized envelope E₀, and exhaustive exact-arithmetic certification across the 31 filtered cells, including replay and equality-face audits.
[graph-node: kgn_ce31e6197ff4 — this page is a PROJECTION; truth lives in the research KG]

## Statement

Every realizable normalized guarded-V TE(2=1) instance on the canonical boundary facet D=F=0 satisfies N ≤ 3L, and therefore N ≤ 3 max(H,L). The facet certificate atlas reports that all 31 envelope cells are resolved, with no remaining open or FAILED-AT cases; it does not establish any Lambda/Q transfer or global assembly result.

## Content

# Normalized D=F=0 TE(2=1) Facet Certificate Atlas

# Normalized D=F=0 TE(2=1) Facet Certificate Atlas

## Disposition

**[PROVED-HERE]** Every realizable normalized guarded-V TE(2=1) instance on the canonical boundary facet D=F=0 satisfies the stronger inequality N <= 3L, and hence the charged implication N <= 3 max(H,L). No chamber remains open and no FAILED-AT frontier remains on this facet. This artifact is deliberately restricted to the boundary job: it makes no Lambda/Q transfer and does not perform the global assembly walk.

The complete 31-cell human-readable table is `outputs/artifacts/te21_D_eq_F_facet_atlas_20260818/atlas.md`; the complete exact coefficient record is the JSON named below. The table is not abbreviated in that file: it contains all endpoint affine expressions, all expanded N,H,L polynomials, and every expanded residual. The replay and equality-face audit are independent exact-arithmetic consumers.

## 1. Exact hypotheses and definitions

**[ARGUED]** Use the corrected guarded-V model from the attached ledger entries. There is a displayed chain C=(c_1<...<c_m), defect order p<q and p<r, and q parallel r. Their closed integer gap intervals are

    I_p=[A,B], I_q=[C_0,D], I_r=[E,F].

A gap is the number of chain elements below the defect. After the canonical q/r swap, D<=F. The exact feasible gap states and fiber weight are

    Gamma={(i,j,k) in I_p x I_q x I_r : i<=j and i<=k},
    W(i,j,k)=1+1_{j=k}.

Thus a tied q/r fiber has exactly two extensions, one per sibling orientation, including i=j=k; it never has weight six. Empty restricted intervals have zero mass, and nonempty but infeasible inputs (A>D or A>F) also have zero mass. Singleton intervals and all endpoint cuts use the same literal closed-interval convention. In particular g(u)<tau means u<c_tau, while g(u)>=tau means c_tau<=u in the raw gap event dictionary (equivalently c_tau<u under the attached threshold notation).

For closed restrictions P=[a,b], Q=[q_0,q_1], R=[r_0,r_1], define (t)_+=max(t,0) and

    X_< = sum_{j=q_0}^{q_1} ((j-a+1)_+-(j-b)_+)
                         ((r_1-j)_+-(r_0-1-j)_+),
    X_> = sum_{k=r_0}^{r_1} ((k-a+1)_+-(k-b)_+)
                         ((q_1-k)_+-(q_0-1-k)_+),
    Y   = sum_{h=max(q_0,r_0)}^{min(q_1,r_1)}
                         ((h-a+1)_+-(h-b)_+),
    V(P,Q,R)=X_<+X_>+2Y.

**[PROVED-HERE]** These formulas count respectively j<k, k<j, and j=k states with i<=j,i<=k; the tied slice has weight two. Therefore, with the strict tails taken literally,

    N=V(I_p,I_q,I_r),
    H=V([A+1,B],I_q,I_r),
    L=V(I_p,[C_0,D-1],I_r).

The interval-level zero guard is essential: the historical unguarded raw formula can return a negative value on an empty interval, so this proof uses direct guarded state enumeration and never interprets such a raw expression as a mass.

## 2. Realizability containment and normalization

**[ARGUED]** The authoritative realizability predicate additionally constructs the transitive closure from the endpoint relations and p<q,p<r and requires acyclicity, q parallel r, height(P)=m, and connected incomparability graph. Its endpoint consequences after D<=F include

    0<=A<=B<=m, 0<=C_0<=D<=m, 0<=E<=F<=m,
    A<=C_0, A<=E, B<=D, E<=D, D<=F,

before translation. Maximum-chain nonsingletonness gives A<B, C_0<D, E<F.

**[PROVED-HERE]** Translate all gaps by -D and set

    x=D-A, y=D-B, c=D-C_0, e=D-E, f=F-D.

On the requested facet f=0, so D=F=0 after translation and

    (A,B,C_0,D,E,F)=(-x,-y,-c,0,-e,0).

The displayed necessary inequalities imply exactly the larger envelope

    E_0={ (x,y,c,e) in Z^4 : x>y>=0, c>=1, e>=1 }.

Every realizable facet point belongs to E_0. The proof certifies E_0 itself; it does not claim that every E_0 point passes the acyclicity, height, connectedness, or q-parallel structural tests. Thus there is no realizability mismatch hidden in the enlargement. The exact facet is R_0 subset E_0.

All degeneracies are allowed where the envelope allows them: y=0, c=1, e=1, and x=y+1. The strict tail [A+1,B] can be empty when x=y+1 and is then zero by the interval guard. The q tail [C_0,D-1]=[-c,-1] is handled literally. D=F is an explicit equality, not a limiting value of f>=1.

## 3. Pre-enumeration resource contract (run before generation)

**[COMPUTED]** The preflight command was run before the generator:

    python outputs/code/preflight_te21_D_eq_F_facet_20260818.py

The exact output was:

    PLANNED_TIMEOUT_SECONDS 300
    MEMORY_BUDGET_MIB 256
    ALL_ORDERED_WEAK_PARTITIONS 75
    FILTERED_BY_x_gt_y 31
    PATTERN_DIMENSION_COUNTS {2: 4, 3: 15, 4: 12}
    INTERPOLATION_SAMPLE_COUNTS_BY_DIMENSION {2: 10, 3: 20, 4: 35}
    GENERATOR_INTERPOLATION_DIRECT_CALLS 2280
    GENERATOR_VALIDATION_DIRECT_CALLS 34153
    GENERATOR_VALIDATION_COMPONENT_CHECKS 102459
    REPLAY_VALIDATION_DIRECT_CALLS 34153
    REPLAY_BOUNDARY_DIRECT_CALLS 328
    TOTAL_DIRECT_LEDGER_CALLS 70914
    MAX_SINGLE_CALL_TRIPLES 6468
    GENERATOR_INTERPOLATION_CANDIDATE_TRIPLES 46279
    GENERATOR_VALIDATION_CANDIDATE_TRIPLES 28209692
    REPLAY_VALIDATION_CANDIDATE_TRIPLES 28209692
    REPLAY_BOUNDARY_CANDIDATE_TRIPLES 16392
    WEIGHTED_INNER_LOOP_ESTIMATE 197672249

The benchmark in the same preflight was a literal direct ledger on equal intervals [-n,0]:

    BENCHMARK n=2 repeats=2000 candidate_triples=54000 elapsed=0.009202800 loops_per_second=5867779.376 extrapolated_n64=0.046802203 checksum=40000
    BENCHMARK n=4 repeats=1000 candidate_triples=125000 elapsed=0.016233800 loops_per_second=7699983.966 extrapolated_n64=0.035665659 checksum=70000
    BENCHMARK n=8 repeats=300  candidate_triples=218700 elapsed=0.026643800 loops_per_second=8208288.600 extrapolated_n64=0.033457035 checksum=99000
    BENCHMARK n=12 repeats=100 candidate_triples=219700 elapsed=0.026896800 loops_per_second=8168257.942 extrapolated_n64=0.033621000 checksum=91000
    BENCHMARK_MEDIAN_LOOPS_PER_SECOND 8168257.942305904
    PREFLIGHT_PASS True

The extrapolation is a performance estimate only, not a proof step. The explicit execution contract was a 300-second timeout and 256 MiB working-memory budget. The generator replay under tracemalloc measured 108.374037 seconds and 41.027 MiB peak traced allocation; the independent replay measured 82.292844 seconds and 2.440 MiB peak traced allocation. Both passed the contract. The generator is streaming in its chamber/point loops and stores only the 31 records and small exact interpolation matrices; no state cube is retained.

## 4. Exhaustive weak-order chambers

**[PROVED-HERE]** The weak-order search is complete. There are 75 ordered set partitions of four labeled quantities (the fourth ordered Bell/Fubini number); the x>y half is (75-13)/2=31 because x=y has the 13 ordered partitions of three labels. The executable preflight independently generated all 75, filtered x>y, and checked equality with the following exact list:

    0 y|xce; 1 yc|xe; 2 yce|x; 3 ye|xc;
    4 c|y|xe; 5 c|ye|x; 6 ce|y|x; 7 e|y|xc; 8 e|yc|x;
    9 y|c|xe; 10 y|ce|x; 11 y|e|xc; 12 y|x|ce; 13 y|xc|e;
    14 y|xe|c; 15 yc|e|x; 16 yc|x|e; 17 ye|c|x; 18 ye|x|c;
    19 c|e|y|x; 20 c|y|e|x; 21 c|y|x|e;
    22 e|c|y|x; 23 e|y|c|x; 24 e|y|x|c;
    25 y|c|e|x; 26 y|c|x|e; 27 y|e|c|x; 28 y|e|x|c;
    29 y|x|c|e; 30 y|x|e|c.

A bar is strict inequality; one block is equality. For a row with blocks B_0|...|B_s, put the lowest level at offset+shift+u, and each later level one plus a nonnegative gap z_i higher. The offset is 1 if c is in the lowest block and 0 otherwise; shift is 1 exactly when e is in the lowest block but c is not. Thus all parameters u,z_i are independent nonnegative integers, strict gaps are 1+z_i, and e>=1. Shifted rows are exactly 3,7,8,17,18,22,23,24. Sorting any E_0 point and taking its consecutive gaps recovers one and only one row, so equality blocks, x=y+1, zero parameters, c=1, and e=1 are covered without overlap or omission.

## 5. Certificates and exact symbolic table

**[PROVED-HERE]** On every one of the 31 cells, the rational certificate is the L branch with

    3L-N = R_L,       alpha=0, beta=0,

where alpha and beta are nonnegative rationals and every coefficient of R_L in the independent nonnegative chamber variables is nonnegative. Therefore N<=3L on that cell, and N<=3 max(H,L). No forced-base-point argument is needed because every chamber closes symbolically.

For an explicit sample, cell 0 y|xce has levels y=u and x=c=e=u+z0+1 and

    N=8 +(26/3)z0+3z0^2+(1/3)z0^3+8u+6uz0+uz0^2+2u^2+u^2z0,
    H=2 +(11/3)z0+2z0^2+(1/3)z0^3+3u+4uz0+uz0^2+u^2+u^2z0,
    L=3 +(31/6)z0+(5/2)z0^2+(1/3)z0^3+6u+5uz0+uz0^2+2u^2+u^2z0,
    R_L=1 +(41/6)z0+(9/2)z0^2+(2/3)z0^3+10u+9uz0+2uz0^2+4u^2+2u^2z0.

**[COMPUTED]** The complete exact N/H/L/R expansions for cells 0 through 30, including endpoint affine formulas and coefficient lists (not just this sample), are in `atlas.md` and the JSON. The generator fits only degree <=3 exact rational polynomials from the literal ledger, then validates them on the larger 0..6 box; the consumer does not use interpolation. Across the 31 residuals there are 391 nonzero residual terms, with smallest nonzero coefficient 1/2 and largest coefficient 31; no residual coefficient is negative.

## 6. Four required independent checks

**[COMPUTED]** The exact commands were run from the workspace root with the resource contract above:

    python outputs/code/generate_te21_D_eq_F_facet_atlas_20260818.py
    python outputs/code/replay_te21_D_eq_F_facet_atlas_20260818.py
    python outputs/code/equality_face_audit_te21_D_eq_F_20260818.py

Generator output:

    PATTERN_COUNT 31
    ALL_GENERATOR_BOX_CHECKS 102459
    ALL_RESIDUAL_NEGATIVE_COUNTS 0
    KNOWN_POINT [18, 6, 11]

Independent replay output (four checks separated explicitly):

    FACET-CHAMBER-EXHAUSTIVENESS: PATTERN_COUNT 31; PATTERN_COVERAGE_BOX 2304;
      pattern hit counts 0:36 1:28 2:28 3:28 4:56 5:56 6:56 7:56 8:56
      9:84 10:84 11:84 12:84 13:84 14:84 15:56 16:56 17:56 18:56
      19:70 20:70 21:70 22:70 23:70 24:70 25:126 26:126 27:126
      28:126 29:126 30:126.
    EXACT-SYMBOLIC-IDENTITIES: IDENTITY_EXPANSIONS 31; IDENTITY_RESIDUAL_TERMS 391;
      DIRECT_BOX_CHECKS 102459.
    COEFFICIENTWISE-NONNEGATIVE-RESIDUALS: NEGATIVE_RESIDUAL_COEFFICIENTS 0;
      NEGATIVE_NHL_COEFFICIENTS 0; ALL_CHECKS_PASS True.
    EQUALITY-FACE-NEAR-MISSES: BOUNDARY_EQUALITY_CHECKS 328;
      E_EQUALS_1_DOMAIN_ROWS 288.

The separate equality-face audit, which parses rational coefficients and does not interpolate, returned:

    COEFFICIENT_SLOTS_DEGREE_LE_3_TOTAL 760
    COEFFICIENT_ZERO_SLOTS_RESIDUAL_TOTAL 369
    RESIDUAL_NONZERO_TERMS_TOTAL 391
    NEGATIVE_COEFFICIENTS_ALL_FOUR_POLYNOMIALS 0
    BOUNDARY_0_1_ASSIGNMENTS_TOTAL 328
    BOUNDARY_ZERO_COORDINATE_INCIDENTS_TOTAL 580
    BOUNDARY_TARGET_EQUALITIES_3L_EQ_N 0
    BOUNDARY_MIN_RESIDUAL_3L_MINUS_N 1
    FINITE_COVERAGE_BOX_ROWS 2304
    E_EQUALS_1_ROWS 288
    COVERAGE_TARGET_EQUALITIES_3L_EQ_N 0
    COVERAGE_MIN_RESIDUAL_3L_MINUS_N 1
    COVERAGE_MAX_RESIDUAL_3L_MINUS_N 500
    EQUALITY_FACE_AUDIT_PASS True

The row ledger has, for every cell, the exact tuple (id, pattern, degree<=3 slots, residual terms, residual zero slots, boundary assignments, boundary equalities, boundary minimum):

    0 y|xce 10 9 1 4 0 1
    1 yc|xe 10 8 2 4 0 7
    2 yce|x 10 6 4 4 0 6
    3 ye|xc 10 8 2 4 0 10
    4 c|y|xe 20 12 8 8 0 9
    5 c|ye|x 20 10 10 8 0 8
    6 ce|y|x 20 6 14 8 0 6
    7 e|y|xc 20 12 8 8 0 18
    8 e|yc|x 20 10 10 8 0 14
    9 y|c|xe 20 18 2 8 0 5
    10 y|ce|x 20 15 5 8 0 4
    11 y|e|xc 20 18 2 8 0 8
    12 y|x|ce 20 9 11 8 0 1
    13 y|xc|e 20 9 11 8 0 1
    14 y|xe|c 20 9 11 8 0 1
    15 yc|e|x 20 13 7 8 0 11
    16 yc|x|e 20 8 12 8 0 7
    17 ye|c|x 20 13 7 8 0 17
    18 ye|x|c 20 8 12 8 0 10
    19 c|e|y|x 35 10 25 16 0 8
    20 c|y|e|x 35 19 16 16 0 14
    21 c|y|x|e 35 12 23 16 0 9
    22 e|c|y|x 35 10 25 16 0 14
    23 e|y|c|x 35 19 16 16 0 29
    24 e|y|x|c 35 12 23 16 0 18
    25 y|c|e|x 35 27 8 16 0 9
    26 y|c|x|e 35 18 17 16 0 5
    27 y|e|c|x 35 27 8 16 0 15
    28 y|e|x|c 35 18 17 16 0 8
    29 y|x|c|e 35 9 26 16 0 1
    30 y|x|e|c 35 9 26 16 0 1

## 7. Realizable witness and self-checks

**[COMPUTED]** The concrete omitted witness is m=2, I_p=[0,1], I_q=I_r=[0,2]. It translates to

    (x,y,c,e,f)=(2,1,2,2,0),
    (A,B,C_0,D,E,F)=(-2,-1,-2,0,-2,0).

The exact fiber ledger gives N=18, p-gap marginals (12,6,0), q- and r-gap marginals (4,7,7), H=6, L=11, and sibling orientation masses 9 and 9. The exact five-node closure replay gives acyclic=True, q_parallel_r=True, height=2, incomparability_connected=True, linear_extensions=18, ledger=(18,6,11). It lies in cell 0 with (u,z0)=(1,0), and 3L-N=15.

**[PROVED-HERE]** Since the proof is on the entire larger E_0, the witness is covered even though the old strict-facet atlas had normalized F=1+v and omitted it. The old failure frontier was exactly f=0; it is now closed by the present 31-cell boundary atlas. No claim is made about Lambda/Q/global assembly.

## 8. Replay files, exact commands, and hashes

All paths are relative to the workspace root. The hashes below were recomputed in this session.

    outputs/code/preflight_te21_D_eq_F_facet_20260818.py
      SHA-256 209d0ae41153af351cf800e4d67dafdde2e14edd540e5eae05cb77f1649a45f5
    outputs/code/generate_te21_D_eq_F_facet_atlas_20260818.py
      SHA-256 8679af787466d8e8927d839abd048fde31d7c869491f2b0cf0b873910e70bcf4
    outputs/code/replay_te21_D_eq_F_facet_atlas_20260818.py
      SHA-256 fce41ac04f3d13a50cb7ad099d7ee49d9067c7acdd0c529ce3daae66fa31a81d
    outputs/code/equality_face_audit_te21_D_eq_F_20260818.py
      SHA-256 211452b6de29382632f17736e32952c9341e4be99540f66a26f7af19e12c96b5
    outputs/data/te21_D_eq_F_facet_atlas_20260818.json
      SHA-256 7aad8e7378dfe5475ba1dc3b8283e8250adf64dafe3359a0a0460b23c6288a5a
    outputs/data/te21_D_eq_F_facet_equality_faces_20260818.json
      SHA-256 c65cdb94f7bfb2c76a5e076151883f6c4f31b2b9371a1965ff006a441d13b002
    outputs/artifacts/te21_D_eq_F_facet_atlas_20260818/atlas.md
      SHA-256 e5cdb27fb431b3e0ef84c6edbc95dd2e525585ec665278cf67564aab6ab3f219
    outputs/artifacts/te21_D_eq_F_facet_atlas_20260818/replay_report.txt
      SHA-256 50303d6d5fc9d684d63723803d9bffbde719db2fb15f173ee3a5359256a0a791
    outputs/artifacts/te21_D_eq_F_facet_atlas_20260818/equality_face_report.txt
      SHA-256 2b4a8f19c2231620ffe881b9f796bf129e492941e8fc64f4a42bb4bc618aaf4c

**[COMPUTED]** Independent replay of the listed commands ended with `ALL_CHECKS_PASS True` and `EQUALITY_FACE_AUDIT_PASS True`. The exact machine-readable table, not a floating-point reconstruction, is the certificate object.

## Final theorem label

**[PROVED-HERE]** The normalized D=F=0 TE(2=1) realizable boundary facet is closed by 31 exhaustive weak-order chambers, each carrying the nonnegative rational certificate 3L-N=R_L. The charged implication N<=3 max(H,L) follows on the whole facet. The strict D<F atlas is a separate sibling artifact; the present result closes precisely the boundary omission.


---
provenance: actor=work_math_manager_streaming work_id=work_0799b5e85585 node_id=d_eq_f_facet_certificate_atlas banked=2026-08-18T08:47:27Z

## Provenance

- work_math_manager_streaming | work_0799b5e85585 | d_eq_f_facet_certificate_atlas | imported from wiki entry normalized-d-f-0-te-2-1-facet-certificate-atlas



---

## Banked record: `independent-full-cone-te-2-1-certificate-replay`

# independent-full-cone-te-2-1-certificate-replay

title: Independent Full-Cone TE(2=1) Certificate Replay
type: computation | label: computed | verification: unverified
namespace: third23
mechanism: Fresh exact execution of the repaired certificate checker, supplemented by an independent audit of coefficient parsing, sourced-witness events, and canonical-cone coverage.
[graph-node: kgn_ed5c52361408 — this page is a PROJECTION; truth lives in the research KG]

## Statement

A fresh execution of the repaired independent checker verified the complete canonical realizable V tied-siblings TE(2=1) certificate system. On the strict facet D<F, it verified all 31 chambers and all 62 certificates, including 49,152 exact identity-component checks, 32,768 strict-certificate numerical points, 47,375 exact ledger points, and 7,776 coverage rows. On the boundary facet D=F, it reconstructed all 31 identities 3L-N=R_L and found all 391 nonzero residual coefficients nonnegative. The exact minimum nonzero residual coefficient is 1/2, while the minimum evaluated on the tested {0,1}-faces is 1. Equality-face persistence passed 31 rows, 328 assignments, and 2,304 finite-envelope rows. The canonical full-cone check partitioned 6,048 rows exhaustively and disjointly into 5,292 rows with D<F and 756 rows with D=F, with no gap or overlap. The corrected sourced-witness audit counted 280 equality events, not the obsolete count 210, and found zero forbidden interior hits. The command returned VERDICT PASS without importing or preserving a prior success label.

## Content

A fresh execution of the repaired independent checker verified the complete canonical realizable V tied-siblings TE(2=1) certificate system. On the strict facet D<F, it verified all 31 chambers and all 62 certificates, including 49,152 exact identity-component checks, 32,768 strict-certificate numerical points, 47,375 exact ledger points, and 7,776 coverage rows. On the boundary facet D=F, it reconstructed all 31 identities 3L-N=R_L and found all 391 nonzero residual coefficients nonnegative. The exact minimum nonzero residual coefficient is 1/2, while the minimum evaluated on the tested {0,1}-faces is 1. Equality-face persistence passed 31 rows, 328 assignments, and 2,304 finite-envelope rows. The canonical full-cone check partitioned 6,048 rows exhaustively and disjointly into 5,292 rows with D<F and 756 rows with D=F, with no gap or overlap. The corrected sourced-witness audit counted 280 equality events, not the obsolete count 210, and found zero forbidden interior hits. The command returned VERDICT PASS without importing or preserving a prior success label.

## Provenance

- supervisor | work_26117b285c41 | banked per finding at effort end




# Theorem 11.5 (Reflection transfer; Lambda)

---

## Banked record: `lambda-l-2e-exact-reflection-transfer`

# lambda-l-2e-exact-reflection-transfer

title: Lambda L-2E Exact Reflection Transfer
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Exact weight-preserving order duality transfers the entire Lambda cell to the previously certified Full-Cone V theorem.
[graph-node: kgn_c392e695c792 — this page is a PROJECTION; truth lives in the research KG]

## Statement

For the Lambda tied-siblings configuration q<p, r<p, q∥r, reflection of chain gaps by R_m(x)=m−x bijects the feasible states Γ_L={(i,j,k):j≤i and k≤i} with the corresponding canonical V feasible states. It preserves the fiber weight W(i,j,k)=1+1[j=k] and hence the total extension count N; maps every interval [a,b] to [m−b,m−a]; exchanges strict lower and upper tails; and sends each same-label orientation numerator S to N−S while preserving diagonal fibers, genuine defect–chain cuts, endpoints, and threshold equalities. Under this transfer, the Lambda two-equal-heavy pattern ρ_q=ρ_r<ρ_p, on both D<F and D=F facets, becomes the canonical V TE(2=1) pattern. The replay-certified Full-Cone TE(2=1) inequality then contradicts the two strict Lambda small-side guards. Therefore no Lambda tied-siblings L-2E configuration survives closed-third avoidance, and L-2E is closed.

## Content

For the Lambda tied-siblings configuration q<p, r<p, q∥r, reflection of chain gaps by R_m(x)=m−x bijects the feasible states Γ_L={(i,j,k):j≤i and k≤i} with the corresponding canonical V feasible states. It preserves the fiber weight W(i,j,k)=1+1[j=k] and hence the total extension count N; maps every interval [a,b] to [m−b,m−a]; exchanges strict lower and upper tails; and sends each same-label orientation numerator S to N−S while preserving diagonal fibers, genuine defect–chain cuts, endpoints, and threshold equalities. Under this transfer, the Lambda two-equal-heavy pattern ρ_q=ρ_r<ρ_p, on both D<F and D=F facets, becomes the canonical V TE(2=1) pattern. The replay-certified Full-Cone TE(2=1) inequality then contradicts the two strict Lambda small-side guards. Therefore no Lambda tied-siblings L-2E configuration survives closed-third avoidance, and L-2E is closed.

## Provenance

- supervisor | work_8d7166a8feca | banked per finding at effort end



---

## Banked record: `lambda-l-2e-exact-reflection-transfer-from-full-cone-te-2-1`

# lambda-l-2e-exact-reflection-transfer-from-full-cone-te-2-1

title: Lambda L-2E Exact Reflection Transfer
type: claim | label: mixed | verification: unverified
namespace: third23
mechanism: The proof reflects chain gaps by R_m(x)=m−x, maps Lambda states and linear extensions to their order duals, preserves the weight and realizability data, canonically separates the D<F and D=F branches, and transfers the upstream Full-Cone bound. The computational component independently replays the reflection and upstream certificate checks but does not reprove the upstream theorem.
[graph-node: kgn_7e866b8c21af — this page is a PROJECTION; truth lives in the research KG]

## Statement

By order-dual reflection, every realizable Lambda configuration in the specified current-shelf, common-heavy V-shaped three-defect setting bijects to a canonical realizable Full-Cone TE(2=1) configuration, preserving feasibility, weights, realizability, and the quantities N, H, and L. Consuming the authorized Full-Cone theorem therefore proves N_L ≤ 3 max(H_L,L_L); the accompanying exact replay passed the stated reflection, branch, and certificate checks. No sharpness or converse result is claimed.

## Content

# lambda-l-2e-exact-reflection-transfer-from-full-cone-te-2-1

# Independent replay certificate: Lambda L-2E exact reflection transfer

**Requested title:** `lambda-l-2e-exact-reflection-transfer-from-full-cone-te-2-1`

## Verdict

**CONFIRMED. L-2E CLOSED.**

The universal reflection transfer is proved below from the order-dual involution. The upstream Full-Cone TE(2=1) V theorem is consumed as an authorized dependency, not reproved. Its two branches, `D<F` and `D=F`, were separately rerun from the deposited exact certificate code and both passed.

## 1. Required readings and dependency record

**[COMPUTED — READ-HERE]** The following artifacts were read verbatim from the KG/wiki before this replay:

1. `lambda-l-2e-exact-reflection-transfer-from-full-cone-te-2-1` (the claim under audit).
2. `full-cone-te-2-1-theorem-closing-v-2e-tied-siblings` (KG node `kgn_d9e87643b122`, snapshot `cb2399fb98e28e2364846e9099afb50f4cb95fc33ec703538ee3549b4681a3e6`). Exact statement: “For every canonical realizable V-shaped three-defect instance in the tied-siblings TE(2=1) cell, canonical exchange of the two siblings gives D≤F. Hence exactly one of the mutually exclusive cases D<F and D=F holds. In the case D<F, the certified 31-chamber/62-certificate atlas `gated-te21-chamber-atlas-and-exact-certificates` gives N≤3 max(H,L). In the case D=F, the certified 31-chamber boundary atlases `exact-d-f-facet-certificate-atlas-for-guarded-te-2-1`, `normalized-d-f-0-te-2-1-facet-certificate-atlas`, and `independent-exact-replay-of-the-d-f-facet-atlas` give 3L-N=R_L with R_L coefficientwise nonnegative, and therefore N≤3L≤3 max(H,L). Thus every canonical realizable TE(2=1) point satisfies N≤3 max(H,L), and the V-2E tied-siblings cell is closed.”
3. `independent-full-cone-te-2-1-certificate-replay` (KG node `kgn_ed5c52361408`, snapshot `8e4ebaaf4c24ff2b9ddaeaf9d06e7bcf16f6a1f4b2e8d3ccbee45edefbb059a8`). Exact statement: the fresh exact checker passed all 31 strict chambers/62 certificates, 49,152 identity-component checks, 32,768 strict numerical points, 47,375 exact ledger points, 7,776 coverage rows; all 31 boundary identities and 391 nonzero residual coefficients were nonnegative; minimum nonzero residual coefficient 1/2; equality-face persistence passed 31 rows/328 assignments/2,304 finite-envelope rows; and the exhaustive full-cone split was 5,292 rows with `D<F` and 756 with `D=F`, with no gap/overlap and `VERDICT PASS`.
4. The requested r35 L-CH template was located and read as `every-realizable-gated-common-heavy-v-configuration-fails-cl`, Section 6, “Explicit Lambda consequence by order duality only”; its projection is `lambda-common-heavy-vacuity-by-duality`. No separate current-shelf slug literally containing `r35` was found.

The exact model ledger entries were also read: `v-lambda-uniform-three-defect-foundation-audit-round-28-corr`, `corrected-v-tied-siblings-exact-ledger`, `corrected-guarded-v-ledger-identities`, `complete-corrected-guarded-v-tied-siblings-identities`, and the strict/boundary atlas entries.

**[ARGUED — CERTIFIED UPSTREAM CONSUMPTION]** The Full-Cone theorem is the sole nonlocal theorem consumed. This certificate checks its interface and both branches; it does not replace the theorem by a finite scan.

## 2. Exact Lambda/V state model

Let `C=(c_1<...<c_m)` and `G_m={0,1,...,m}`. Lambda has `q<p, r<p, q||r`. A legal interval is `I_u^L=[a_u^L,b_u^L]`, where gap `x` means exactly `x` chain elements precede `u`; legality is literally `c_t<u => t<=x` and `u<c_t => x<t`.

The exact state set and weight are

`Gamma_L={(i,j,k) in I_p^L x I_q^L x I_r^L : j<=i and k<=i}`,

`W_L(i,j,k)=1+1[j=k]`.

Let `P_V=P_L^vee` and display `d_s=c_{m+1-s}`. Then V has `p<q,p<r,q||r`,

`Gamma_V={(I,J,K) in I_p^V x I_q^V x I_r^V : I<=J and I<=K}`,

and the same weight formula.

## 3. Interval and state bijection

**[PROVED-HERE]** Put `R_m(x)=m-x`. It is an involution of `G_m`; `0` and `m` exchange and the sole gap is fixed when `m=0`. For every closed `[a,b]` in `G_m`,

`R_m([a,b])=[m-b,m-a]`.

Indeed, with `s=m+1-t`, `d_s<_V u` iff `u<_L c_t`, so `x<t` becomes `x<m+1-s`, equivalently `s<=m-x`; and `u<_V d_s` iff `c_t<_L u`, so `t<=x` becomes `m-x<s`. Thus no fictitious gap `-1` or `m+1` appears.

The state involution is

`R_Gamma(i,j,k)=(m-i,m-j,m-k)`.

`j<=i,k<=i` becomes `m-i<=m-j,m-i<=m-k`, exactly the V feasibility conditions, and involutivity gives equality of the two feasible sets. Also

`W_V(R_Gamma(i,j,k))=1+1[m-j=m-k]=1+1[j=k]=W_L(i,j,k)`.

Therefore `N_V=N_L=:N`, state by state.

**[PROVED-HERE]** A Lambda fiber word `lambda_0 c_1 lambda_1 ... c_m lambda_m`, reversed and relabeled by `d_s=c_{m+1-s}`, becomes

`rev(lambda_m) d_1 rev(lambda_{m-1}) ... d_m rev(lambda_0)`.

This is an involutive bijection of actual linear extensions. It reverses the two orders in each tied sibling block but keeps two extensions, including at `i=j=k`. Duality preserves acyclicity, height/maximality, off-chain status, sibling incomparability, and incomparability-graph connectedness, so the transfer is on realizable objects, not only endpoint tuples.

## 4. Endpoint normalization, tails, and facets

Write

`I_p^V=[A,B]=[m-b_p^L,m-a_p^L]`,
`I_q^V=[C,D]=[m-b_q^L,m-a_q^L]`,
`I_r^V=[E,F]=[m-b_r^L,m-a_r^L]`.

The canonical V endpoint consequences are `A<=C, A<=E, B<=D, E<=D, D<=F`; they are consequences of actual V order/legal-window semantics. Inverse reflection gives `b_p^L>=b_q^L`, `b_p^L>=b_r^L`, `a_p^L>=a_q^L`, `b_r^L>=a_q^L`, `a_q^L>=a_r^L`. If raw reflection has `D>F`, swap q,r. This preserves feasibility, weight, N, equal-heavy status and CLOSED-THIRD, and only exchanges sibling labels. Since both Lambda siblings are heavy at `s`, both strict upper-tail guards are available, so canonical relabeling does not lose the selected guard.

The charged relation is `rho_q^L=rho_r^L=s<t=rho_p^L`. Reflection gives `rho_p^V=A=m-t` and `rho_q^V=rho_r^V=m-s=D`, with `A<D`. The two facets are exhaustive/disjoint:

`D<F iff a_q^L>a_r^L`, and `D=F iff a_q^L=a_r^L`.

For `M_u^X(x)=sum_{g(u)=x}W_X(g)`, `Low_u^X(h)=sum_{x<h}M_u^X(x)`, and `Up_u^X(h)=sum_{x>h}M_u^X(x)`, state reflection proves, for every integer h,

`M_u^V(m-h)=M_u^L(h)`,
`Low_u^V(m-h)=Up_u^L(h)`,
`Up_u^V(m-h)=Low_u^L(h)`.

Thus with `A=m-t,D=m-s`,

`H_V=Up_p^V(A)=Low_p^L(t)`,
`L_V=Low_q^V(D)=Up_q^L(s)`.

The charged Lambda strict guards `Low_p^L(t)<N/3` and `Up_q^L(s)<N/3` become exactly `H_V<N/3` and `L_V<N/3`; after a canonical sibling swap use the other sibling, which has the same strict heavy-tail hypothesis.

Actual singleton intervals are impossible under height `m`: a singleton legal window inserts its defect into C and gives a chain of size `m+1`. Restricted singleton/empty intervals remain literal; empty masses are zero.

## 5. Event-by-event numerator table

Let `S_X(x<y)` count extensions with x before y. Let `X_{j<k}^L,X_{k<j}^L` be unweighted strict-slice counts and `Y^L` the tied-state count. Then

`S_L(q<r)=X_{j<k}^L+Y^L`, `S_L(r<q)=X_{k<j}^L+Y^L`, and `N=X_{j<k}^L+X_{k<j}^L+2Y^L`.

| class | Lambda event | carried V event | same-label V event | exact identity |
|---|---|---|---|---|
| sibling | `q<r` | `r<q` | `q<r` | `S_V(q<r)=S_L(r<q)=N-S_L(q<r)` |
| sibling | `r<q` | `q<r` | `r<q` | `S_V(r<q)=S_L(q<r)=N-S_L(r<q)` |
| genuine chain | `u<c_t`, `a_u<t<=b_u` | `d_sigma<u`, `sigma=m+1-t` | `u<d_sigma` | `S_V(d_sigma<u)=S_L(u<c_t)` and `S_V(u<d_sigma)=N-S_L(u<c_t)` |
| same chain cut | `c_t<u` | `u<d_sigma` | `d_sigma<u` | `S_V(u<d_sigma)=S_L(c_t<u)` and `S_V(d_sigma<u)=N-S_L(c_t<u)` |
| forced pair | `p<q` (Lambda false) | `q<p` | `p<q` | `S_V(p<q)=S_L(q<p)=N-S_L(p<q)` |
| forced pair | `p<r` (Lambda false) | `r<p` | `p<r` | `S_V(p<r)=S_L(r<p)=N-S_L(p<r)` |

On each `j=k` fiber the two extensions split one to each sibling orientation, including the fully tied `i=j=k` fiber. For genuine chain events, eligibility is preserved exactly:

`a_u<t<=b_u iff m-b_u<sigma<=m-a_u`.

`g<t iff u<c_t` and `g>=t iff c_t<u`; `t=1` maps to `sigma=m`, `t=m` maps to `sigma=1`, and `m=0` has no chain cuts. Forced pairs are not included in CLOSED-THIRD. Hence every genuine same-label orientation numerator is exactly sent to `N-S`.

## 6. CLOSED-THIRD and upstream closure

**[PROVED-HERE]** For `OUT(S,N):=(3S<N) or (3S>2N)`,

`S<N/3 iff N-S>2N/3`, `S>2N/3 iff N-S<N/3`, and the two equality faces map as `S=N/3 <-> N-S=2N/3` and `S=2N/3 <-> N-S=N/3`. Thus the closed middle interval and equality conventions are invariant.

**[ARGUED — CERTIFIED UPSTREAM PROVED]** The consumed Full-Cone theorem gives `N_V<=3 max(H_V,L_V)` on every canonical realizable V TE(2=1) point, with exactly the disjoint branches `D<F` and `D=F`. Substitution gives

`N_L<=3 max(Low_p^L(t),Up_q^L(s))`.

Both entries are `<N_L/3`, while `N_L>0`, so the right side is strictly below `N_L`, contradiction. Therefore no realizable Lambda L-2E point survives CLOSED-THIRD: **L-2E CLOSED**.

## 7. Exact computations executed here

**[COMPUTED]** The banked source `outputs/code/lambda_v_reflection_transfer_audit_20260818.py` was executed and returned:

```text
reflection_audit_max_m = 6
reflection_state_fiber_checks = 35832
all_state_weight_and_N_checks = PASS
tail_exchange_checks = PASS
orientation_complement_checks = PASS
chain_endpoint_cuts_checked = all t=1..m for every m<=6
cited_boundary_sample_V_intervals = ((0, 1), (0, 2), (0, 2))
cited_boundary_sample_L_intervals = ((1, 2), (0, 2), (0, 2))
cited_boundary_sample_N = 18
cited_boundary_sample_V_marginals = [[12, 6, 0], [4, 7, 7], [4, 7, 7]]
cited_boundary_sample_L_marginals = [[0, 6, 12], [7, 7, 4], [7, 7, 4]]
cited_boundary_sample_V_H_L = (6, 11)
cited_boundary_sample_L_mapped_H_L = (6, 11)
canonical_V_facet_counts_m0_to_6 = {'D<F': 14388, 'D=F': 7056}
status = ALL REFLECTION REGRESSION ASSERTIONS PASSED
```

**[COMPUTED]** Rerun of `outputs/code/gated_te21_chamber_atlas_20260817.py` (strict facet) returned `PATTERNS 31`, `CERTIFICATES 62`, `IDENTITY_REPLAY_CHECKS 49152`, `NUMERIC_SPOT_CHECKS 142125`, `BOUNDARY_70_COUNT 70`, `BOUNDARY_ALL_GATE True`, `BOUNDARY_ALL_EQUALITY_NO_INTERIOR True`, and the explicit gate-only obstruction `[1,2],[0,1],[0,2]` with `B_le_D=False`. The obstruction is the documented `FAILED_AT_LITERAL_GATE_ONLY` scope diagnostic, not an actual-domain failure.

**[COMPUTED]** Rerun of `outputs/code/replay_te21_D_eq_F_facet_atlas_20260818.py` returned:

```text
PATTERN_COUNT 31
PATTERN_COVERAGE_BOX 2304
IDENTITY_EXPANSIONS 31
IDENTITY_RESIDUAL_TERMS 391
NEGATIVE_RESIDUAL_COEFFICIENTS 0
NEGATIVE_NHL_COEFFICIENTS 0
DIRECT_BOX_CHECKS 102459
BOUNDARY_EQUALITY_CHECKS 328
E_EQUALS_1_DOMAIN_ROWS 288
KNOWN_POINT x=2 y=1 c=2 e=2 f=0 parameters=pattern0(u=1,z0=0) N=18 H=6 L=11
KNOWN_POSET {'acyclic': True, 'q_parallel_r': True, 'height': 2, 'incomparability_connected': True, 'linear_extensions': 18, 'ledger': (18, 6, 11)}
ALL_CHECKS_PASS True
```

The equality-face parser also returned `391` residual terms, zero negative coefficients, `BOUNDARY_0_1_ASSIGNMENTS_TOTAL 328`, `FINITE_COVERAGE_BOX_ROWS 2304`, `BOUNDARY_MIN_RESIDUAL_3L_MINUS_N 1`, `COVERAGE_MIN_RESIDUAL 1`, and `EQUALITY_FACE_AUDIT_PASS True`.

**[COMPUTED]** Independent source `outputs/code/lambda_l2e_independent_replay_20260818.py` and verbatim output `outputs/lambda-l2e-independent-replay-20260818.txt` were persisted. The modular exact run returned:

```text
LEGAL_INTERVAL_REFLECTION 165
STATE_INTERVAL_REPLAY (173613, 6355899, 173613, 3751704, 173613, 5193861, 9, Counter({'D<F': 73194, 'D=F': 27225}), 330)
ACTUAL_LINEAR_EXTENSION_DUAL_REPLAY (101, 0)
REALIZABILITY_ENDPOINT_DOMAIN_AUDIT (101, 18)
HEAVY_CANONICAL_RELABEL_AUDIT (0, 0, 0, [])
CLOSED_THIRD_COMPLEMENT_AUDIT (1326, 33)
STATUS ALL_INDEPENDENT_L2E_REFLECTION_ASSERTIONS_PASSED
```

The state replay covers all nonempty interval triples through `m=8`, every integer threshold including outside endpoints, all orientations, diagonals, and chain cuts. Actual linear-extension duality was checked on 101 realizable cases through `m=3`, with zero singleton cases; 18 required canonical sibling swapping.

**[FAILED — NON-LOAD-BEARING IMPLEMENTATION ATTEMPTS, RESOLVED]** One preliminary custom legality test reversed the two dual relation branches and stopped at `(m,a,b)=(1,0,0)`; it was corrected. A subsequent all-in-one permutation run timed out at 300 seconds during `m=5` exhaustive permutations, with no assertion failure; its completed state audit was rerun modularly through `m=3` for the permutation component and passed. These are implementation/resource stalls only, not mathematical mismatches.

## 8. Boundary/hypothesis checklist and dependency tree

**[PROVED-HERE]** `0<->m`, no `-1/m+1`; `m=0` makes `s<t` impossible; empty restrictions have zero mass; actual singleton windows contradict height; `j=k` and `i=j=k` have weight 2; strict/weak and genuine-cut conditions are literal; chain-cut endpoints are `1->m` and `m->1`; atom and CLOSED-THIRD equality faces persist; `D<F` and `D=F` are exhaustive/disjoint after the only allowed sibling swap; and all realizability guards are preserved by duality.

```text
this L-2E replay
├── legal-gap/fiber ledgers
│   ├── v-lambda-uniform-three-defect-foundation-audit-round-28-corr
│   ├── corrected-v-tied-siblings-exact-ledger
│   ├── corrected-guarded-v-ledger-identities
│   └── complete-corrected-guarded-v-tied-siblings-identities
├── r35 template actually located/read
│   └── every-realizable-gated-common-heavy-v-configuration-fails-cl §6
│       └── lambda-common-heavy-vacuity-by-duality
└── certified upstream Full-Cone V theorem
    ├── full-cone-te-2-1-theorem-closing-v-2e-tied-siblings
    │   ├── gated-te21-chamber-atlas-and-exact-certificates [D<F]
    │   └── exact-d-f-facet-certificate-atlas-for-guarded-te-2-1 [D=F]
    │       ├── normalized-d-f-0-te-2-1-facet-certificate-atlas
    │       └── independent-exact-replay-of-the-d-f-facet-atlas
    └── independent-full-cone-te-2-1-certificate-replay [full-cone split]
```

**[PROVED-HERE]** The reflection/interface identities and all boundary mappings are exact. **[COMPUTED]** Every load-bearing in-session replay passed. **[ARGUED — CERTIFIED UPSTREAM PROVED]** The consumed theorem closes both V facets. Final disposition: **CONFIRMED — L-2E CLOSED**.

---
provenance: actor=work_math_manager_streaming work_id=work_8d7166a8feca node_id=lambda_2e_reflection_transfer_independent_replay banked=2026-08-18T12:12:05Z

## Provenance

- work_math_manager_streaming | work_8d7166a8feca | lambda_2e_reflection_transfer_independent_replay | imported from wiki entry lambda-l-2e-exact-reflection-transfer-from-full-cone-te-2-1



---

## Banked record: `independent-lambda-reflection-replay`

# independent-lambda-reflection-replay

title: Independent Lambda Reflection Replay
type: computation | label: computed | verification: unverified
namespace: third23
mechanism: Independent exhaustive finite symbolic and exact-enumeration regression of every interface used by the reflection transfer.
[graph-node: kgn_9b9157f33e6c — this page is a PROJECTION; truth lives in the research KG]

## Statement

An independent exact replay confirmed the Lambda reflection transfer. It checked 173,613 interval triples through m=8, 6,355,899 tail identities, 3,751,704 chain-cut identities, actual linear-extension duality through m=3, the 31 strict chambers and 62 strict certificates, all 49,152 Full-Cone identities, and the 31 boundary identities with 391 residual terms. Every check passed, including state bijection, fiber-weight preservation, tail exchange, numerator complementation, endpoint handling, and the D<F/D=F partition.

## Content

An independent exact replay confirmed the Lambda reflection transfer. It checked 173,613 interval triples through m=8, 6,355,899 tail identities, 3,751,704 chain-cut identities, actual linear-extension duality through m=3, the 31 strict chambers and 62 strict certificates, all 49,152 Full-Cone identities, and the 31 boundary identities with 391 residual terms. Every check passed, including state bijection, fiber-weight preservation, tail exchange, numerator complementation, endpoint handling, and the D<F/D=F partition.

## Provenance

- supervisor | work_8d7166a8feca | banked per finding at effort end




# Theorem 12.1 (Q-D exclusion)

---

## Banked record: `pairwise-distinct-heavy-q-exclusion`

# pairwise-distinct-heavy-q-exclusion

title: Pairwise-Distinct-Heavy Q Exclusion
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: An exhaustive symbolic chamber analysis proves heavy-index coincidence or supplies an eligible middle-third chain cut; the complementary heavy atom supplies the upper bound.
[graph-node: kgn_cd5f714cdd73 — this page is a PROJECTION; truth lives in the research KG]

## Statement

For the charged displayed maximum-chain Q presentation with defects x<y and z incomparable with both, legal closed intervals X=[a,b], Y=[c,d], Z, endpoint constraints a≤c and b≤d, non-singleton windows, feasible states (i,j,k) satisfying i∈X, j∈Y, k∈Z and i≤j, and intrinsic weight w(i,j,k)=1+1_{i=k}+1_{j=k}, closed-third avoidance cannot coexist with pairwise-distinct unique heavy-gap indices. The disjoint chamber b<c, endpoint-equality chamber b=c, and proper-overlap chamber c<b, including their endpoint subchambers, exhaust the legal interval systems. Every chamber either forces coincidence or degeneracy of heavy indices, or yields a genuine incomparable defect–chain cut whose exact orientation numerator lies strictly between N/3 and 2N/3. The conclusion is limited to this charged displayed Q presentation.

## Content

For the charged displayed maximum-chain Q presentation with defects x<y and z incomparable with both, legal closed intervals X=[a,b], Y=[c,d], Z, endpoint constraints a≤c and b≤d, non-singleton windows, feasible states (i,j,k) satisfying i∈X, j∈Y, k∈Z and i≤j, and intrinsic weight w(i,j,k)=1+1_{i=k}+1_{j=k}, closed-third avoidance cannot coexist with pairwise-distinct unique heavy-gap indices. The disjoint chamber b<c, endpoint-equality chamber b=c, and proper-overlap chamber c<b, including their endpoint subchambers, exhaust the legal interval systems. Every chamber either forces coincidence or degeneracy of heavy indices, or yields a genuine incomparable defect–chain cut whose exact orientation numerator lies strictly between N/3 and 2N/3. The conclusion is limited to this charged displayed Q presentation.

## Provenance

- supervisor | work_8fe8697950c8 | banked per finding at effort end



---

## Banked record: `q-distinct-heavy-chamber-certificate-independent-decision-ro`

# q-distinct-heavy-chamber-certificate-independent-decision-ro

title: Distinct-Heavy Q Branch Audit
type: note | label: report | verification: unverified
namespace: third23
mechanism: Independent replay of the exact isotone state space, tied-block fiber weights, interval-chamber endpoint cases, closed-middle witnesses, and heavy-order inequalities; the artifact is banked as a session deliverable under q-distinct-heavy-branch-repair-deepcheck.
[graph-node: kgn_e7d60772c2b1 — this page is a PROJECTION; truth lives in the research KG]

## Statement

The audit confirms that the pairwise-distinct-heavy Q branch is impossible for the specified charged maximum-chain presentation, under the stated hypotheses and imported lemmas. The result is scoped to this charged Q presentation class and is not an exclusion theorem for all possible Q presentations.

## Content

# Q distinct-heavy chamber certificate independent decision round 23

# Q distinct-heavy chamber certificate independent decision round 23

status: as labeled in the artifact (session deliverable, banked VERBATIM by the harness)

HEADLINE: CONFIRMED. The pairwise-distinct-heavy Q branch is impossible for the charged maximum-chain presentation. The exact isotone state space, tied-block weights, all interval chambers, endpoint cases, and closed-middle witnesses were independently replayed; the complete referee artifact is banked under q-distinct-heavy-branch-repair-deepcheck.

# Theorem-audit outcome: CONFIRMED

## Scope and imported premises

[PROVED-HERE] The charged setting is a finite poset P with displayed maximum chain C=(c_1<...<c_m), defect relation x<_P y, z incomparable with both, closed-third avoidance for every incomparable pair, and pairwise-distinct unique heavy gap indices. The conclusion is for this charged Q presentation and for any presentation satisfying exactly these hypotheses; it is not an exclusion claim for every possible Q presentation.

[ARGUED — IMPORTED] The proof uses the supplied canonical gap-fiber bijection, exact chain-cut and tied-defect event dictionary, closed-third strong-order lemma, maximum-chain heavy-gap lemma, and heavy-gap alignment lemma. In particular, for a defect u there is a unique rho_u with mu_u(rho_u)>N/3 and strict lower and upper tails each less than N/3.

## 1. Interval systems and realizability

Write X=I_x=[a,b], Y=I_y=[c,d], Z=I_z=[e,f] in G_m={0,...,m}, with n_x=b-a+1, n_y=d-c+1, n_z=f-e+1.

[PROVED-HERE] Since x<_P y, every chain predecessor of x is a predecessor of y and every chain successor of y is a successor of x. Hence

  a<=c and b<=d.                                             (1)

Since z is incomparable with x and y, the actual windows satisfy

  X intersect Z is nonempty and Y intersect Z is nonempty.       (2)

For example, b_z<a_x would imply z<c_{b_z+1}<=c_{a_x}<x. The other disjoint-order cases are identical.

[PROVED-HERE] A defect window cannot be a singleton in the maximum-chain setting. If I_u={r}, then c_t<u for t<=r and u<c_t for t>r, including r=0 and r=m. Therefore C union {u} is a chain longer than C. For m=0, any nonempty defect is already a chain longer than the empty chain. Thus

  n_x,n_y,n_z>=2.                                           (3)

Conversely, (1) and (2) are sufficient for the Q interval construction. Impose the chain threshold relations determined by X,Y,Z, impose x<y, and take transitive closure. For every i in X, j in Y, k in Z with i<=j, a block word inserting x,y,z in gaps i,j,k and respecting x<y is a total order extending all generators. Hence the relation is acyclic. A hidden relation between z and x or between z and y would require one of the four forbidden disjoint-window inequalities, so the closure has exactly Q on the defects and exactly the supplied windows.

Therefore the exact feasible state space is

  F={(i,j,k): i in X, j in Y, k in Z, i<=j}.                  (4)

This is not X times Y times Z. The inequality i<=j is forced because i>j would place y<c_{j+1}<x. There is no inequality involving k.

Ordinal-sum-indecomposability is an additional filter, not an omitted chamber. In the constructed Q poset the defect incomparability graph is x--z--y, and c_t is incomparable with u exactly when a_u<t<=b_u. Thus connectedness can only remove interval rows from the already-exhausted superset above.

## 2. Exact state weights and orientation formulas

[PROVED-HERE] For (i,j,k) in F, the exact fiber weight is

  w(i,j,k)=1+1_{i=k}+1_{j=k}.                                (5)

The local cases are: all gaps distinct, weight 1; i=j not equal to k, the forced xy block, weight 1; i=k<j, the two words xz,zx, weight 2; i<j=k, the two words yz,zy, weight 2; and i=j=k, the three words xyz,xzy,zxy, weight 3. The fully tied block has three words, not six. Its exact splits are (xz,zx)=(2,1) and (yz,zy)=(1,2).

Thus N=sum_F w. The exact defect-pair numerators are

  M_xz=sum_{i<k} w + #{i=k<j} + 2#{i=j=k},
  M_zx=sum_{k<i} w + #{i=k<j} + #{i=j=k},
  M_yz=sum_{j<k} w + #{i<j=k} + #{i=j=k},
  M_zy=sum_{k<j} w + #{i<j=k} + 2#{i=j=k}.                 (6)

Each incomparable pair's two numerators add to N. No equality of the two orientations is assumed.

For an interval A, let A_{>=r}=A intersect [r,m], A_{<=r}=A intersect [0,r], with strict variants A_{>r}, A_{<r}. Direct summation over the isotone set F gives, for every literal endpoint 0<=r<=m,

  mu_x(r)=1_{r in X} ( n_z |Y_{>=r}| + 1_{r in Z}|Y_{>=r}|
                       + |Y intersect Z intersect [r,m]| ),

  mu_y(r)=1_{r in Y} ( n_z |X_{<=r}| + |X intersect Z intersect [0,r]|
                       + 1_{r in Z}|X_{<=r}| ),

  mu_z(r)=1_{r in Z} ( |F_2| + 1_{r in X}|Y_{>=r}|
                       + 1_{r in Y}|X_{<=r}| ),                 (7)

where F_2={(i,j) in X times Y:i<=j}.

The tie-separated forms, including the full diagonal, are

  mu_x(r)=1_X(r)(n_z|Y_{>r}|+1_Z(r)|Y_{>r}|
             +|Y intersect Z intersect (r,m]|+2 1_{r in Y intersect Z}),

  mu_y(r)=1_Y(r)(n_z|X_{<=r}|+|X intersect Z intersect [0,r)|
             +1_Z(r)|X_{<r}|+2 1_{r in X intersect Z}),

  mu_z(r)=1_Z(r)(|F_2|+1_X(r)|Y_{>r}|+1_Y(r)|X_{<r}|
             +2 1_{r in X intersect Y}).                       (8)

The total identity is

  N=n_z|F_2|+sum_{r in X intersect Z}|Y_{>=r}|
      +sum_{r in Y intersect Z}|X_{<=r}|
    =sum_r mu_x(r)=sum_r mu_y(r)=sum_r mu_z(r).                (9)

The exact chain-cut numerators are

  M_{u<c_t}=sum_{r<t}mu_u(r),
  M_{c_t<u}=sum_{r>=t}mu_u(r).                                (10)

Thus a_u<t<=b_u is exactly the genuine-incomparability range. At t=1 the left sum contains only gap 0; at t=m the right sum contains only gap m when present. No fictitious gap -1 or m+1 occurs.

## 3. Heavy order

[PROVED-HERE] The imported heavy inequalities imply that rho_u is the unique global maximizer of mu_u: every other atom is in one strict tail and is less than N/3, while mu_u(rho_u)>N/3.

If rho_y<rho_x, heavy-gap alignment applied to y and x says x is not below y, contradicting x<_P y. Hence pairwise distinctness leaves only

  rho_z<rho_x<rho_y,
  rho_x<rho_z<rho_y,
  rho_x<rho_y<rho_z.                                       (11)

The corresponding strong defect orientations are respectively z before both, x before z before y, and both x,y before z. No independent-marginal assertion is used.

## 4. Exhaustive chambers

From a<=c and b<=d there are exactly three x/y cases: D, b<c; E, c=b; and genuine overlap O, c<b. The latter splits into endpoint chambers.

### D: b<c

Here i<=j is automatic. Under unique modes, every point of X intersect Z has the same positive correction and is strictly above points of X outside Z, so X intersect Z={p}. Likewise Y intersect Z={q}, with p<q. The exact atoms are

  mu_x(r)=n_z n_y+n_y 1_{r=p}+1,       r in X,
  mu_y(r)=n_z n_x+n_x 1_{r=q}+1,       r in Y,
  mu_z(r)=n_x n_y+n_y 1_{r=p}+n_x 1_{r=q},  r in Z.           (12)

Thus rho_x=p and rho_y=q. If n_y>n_x then rho_z=p; if n_x>n_y then rho_z=q; if n_x=n_y then mu_z has two maxima. Hence pairwise-distinct unique modes are impossible in D.

Here

  N=n_z n_x n_y+n_x+n_y,

and, because n_z>=2 and X intersect Z={p}, p is an endpoint of X. The strict tail of x away from p has weight

  A=(n_x-1)(n_z n_y+1),

with exact slack

  3A-N=n_z n_y(2n_x-3)+2n_x-n_y-3.                         (13)

For n_x=2 this equals (n_z-1)n_y+1>0. For n_x>=3 and n_z>=2 it is at least (4n_x-7)n_y+2n_x-3>0.

If p=a, choose t=p+1; then M_{c_t<x}=A. If p=b, choose t=p; then M_{x<c_t}=A. These are valid cuts even at endpoint gaps because n_x>=2.

### E: c=b

Here X intersect Y={c}, and overlap with both X and Y forces c in Z. Since n_z>=2, Z has a point below c or above c. If it has a point below c, X intersect Z contains at least two points; formula (7) makes their mu_x values equal and maximal. If it has a point above c, Y intersect Z contains at least two points; formula (7) makes their mu_y values equal and maximal. Hence E has no all-unique modes. The exceptional singleton Z={c} is excluded by (3). This covers the equality boundary.

### O: c<b

Let J=[c,b]. For r in Z, write mu_z(r)=|F_2|+delta(r). Then

  delta(r)=n_y on X\Y,
           d-a+2 on J,
           n_x on Y\X,
           0 outside X union Y.                              (14)

The central value is strictly larger than both side values because

  (d-a+2)-n_y=c-a+1>0,
  (d-a+2)-n_x=d-b+1>0.                                    (15)

The overlap assumptions force K=Z intersect J to be nonempty: if Z meets X left of c and Y right of b, its interval contains all of J. Therefore a unique z mode forces K to be a singleton. Since n_z>=2 and J has at least two integer points, only two cases remain:

  L: K={c}, Z=[e,c] with e<c;
  R: K={b}, Z=[b,f] with f>b.                             (16)

No interior singleton is possible for a non-singleton integer interval Z.

#### L

Here Y intersect Z={c}; formula (7) is constant and maximal on X intersect Z. Unique x mode forces a=c, so X=[c,b]. Let n=b-c+1 and s=n_z. Then

  mu_y(c)=s+2,
  mu_y(r)=s(r-c+1)+1 for c<r<=b,
  mu_y(r)=sn+1 for b<=r<=d.                                (17)

Since sn+1-(s+2)=s(n-1)-1>0, unique y mode forces d=b. The modes are

  (rho_x,rho_y,rho_z)=(c,b,c),

so they are not pairwise distinct.

#### R

The reverse calculation first forces d=b, since otherwise Y intersect Z contains at least two equal maximal mu_y values. With Y=[c,b], formula (7) gives a constant maximal mu_x value on [a,c]. If a<c there are at least two such values, so unique x mode forces a=c and X=Y=[a,b]. The modes are

  (rho_x,rho_y,rho_z)=(a,b,b),

again not pairwise distinct. The endpoint comparison is s(n-1)-1>0, so no equality case is lost.

Therefore every legal interval system is in D, E, L, R, or a non-unique interior-overlap remainder, and no system has three pairwise-distinct unique modes.

## 5. Closed-middle witnesses

The chamber classification already proves exclusion. Under the imported heavy hypotheses it also gives the asserted exact forbidden witness.

In L, with X=Y=[c,b], n=b-c+1, s=n_z, and P_0=n(n+1)/2,

  N=sP_0+n+1,
  A=s(P_0-n)+n,                                             (18)

where A is the strict lower tail of the heavy y mode b. The exact slack is

  3A-N=s n(n-2)+2n-1>0.                                    (19)

For n=2 the slack is 3; for n>=3 it is positive. The selected pair is y and c_b, with exact numerator M_{y<c_b}=A. It is incomparable because c<b, and t=b is valid even when b=m.

In R, with X=Y=[a,b], the right tail of the heavy x mode a has the same A and the same strict slack. The selected pair is c_{a+1} and x, with exact numerator M_{c_{a+1}<x}=A. It is incomparable because a<a+1<=b, and t=a+1 is valid even when a=0.

In D, A is given by (13), and the selected pair is as stated in the D chamber. In every case A omits the heavy atom, so

  N-A>=mu_u(rho_u)>N/3,

and hence A<2N/3. Combining with (13) or (19) gives

  N/3<A<2N/3.                                             (20)

Thus the exact numerator lies in the required closed interval [N/3,2N/3], with strict inequality at both ends. The selected pair is a genuine incomparable defect-chain pair by (10). E and the interior-overlap remainder have no unique heavy modes, so their mode degeneracy closes them before a witness is needed.

## 6. Computations executed in-session

[COMPUTED] Replayed outputs/code/q_distinct_heavy_branch_repair_deepcheck.py. Exact output:

m 1 1 0 0
m 2 18 2 0
m 3 108 8 0
m 4 410 22 0
m 5 1198 48 0
m 6 2947 92 0
m 7 6412 160 0
m 8 12720 260 0
m 9 23475 400 0
m 10 40876 590 0
m 11 67848 840 0
m 12 108186 1162 0
TOTAL systems 264199 unique 3584 distinct 0 formula_failures 0
tail_bad_count 0 tail_min_slack 3
mode_class_fail_count 0 first []
formula_examples []

The script's chamber_counts [] line was an unused output-label omission, not evidence.

[COMPUTED] Replayed outputs/code/q_distinct_heavy_branch_pair_and_chamber_audit.py. It returned pair_formula_failures 0, mode_class_failures 0, tail_tests 992, tail_min 3, tail_max 159, bad 0; algebra_disjoint_bad_2<=100 0; algebra_common_bad_2<=100 0; and

full_tie_states [(0, 0, 0, 3)] pair_split {'xz': 2, 'zx': 1, 'yz': 1, 'zy': 2}

[COMPUTED] Replayed outputs/code/q_distinct_heavy_branch_topological_audit.py:

topological_interval_checks_m1_to_4 537 extension_total 17130 weight_vs_topological_failures 0

[COMPUTED] Independent exact replay through m=8, persisted as outputs/code/_runs/run_1786988280564/script.py, directly closed every generator system, checked the exact supplied windows, and compared direct weighted sums with the marginal and pair formulas. Exact output:

INDEPENDENT_RAW_Q_INTERVALS_m1_to_8 23814 closure_rows 23814 formula_failures 0 pair_failures 0
UNIQUE 592 DISTINCT 0 CHAMBERS {'D': 172, 'E': 0, 'L': 210, 'R': 210, 'I': 0} class_failures 0 witness_failures 0
SYMBOLIC_BAD_D_2_to_150 0 SYMBOLIC_BAD_COMMON_2_to_150 0

The same audit found 23750 rows of height m and 6293 rows of height m with connected incomparability graph. These are the maximum-chain and ordinal-sum-indecomposable filters and only shrink the already-exhausted superset.

[COMPUTED] Direct topological witness calibrations returned:

CALIBRATION x<c1 N 17 numerator 7 A 7 3A 21 2N 34 incomparable True
CALIBRATION y<c2 N 9 numerator 4 A 4 3A 12 2N 18 incomparable True
CALIBRATION c2<x N 9 numerator 4 A 4 3A 12 2N 18 incomparable True

## 7. Adversarial boundary and degeneracy checks

[COMPUTED] The equality probe m=2, X=[0,1], Y=[1,2], Z=[0,2] has N=20, weights

[(0,1,0,2),(0,1,1,2),(0,1,2,1),(0,2,0,2),(0,2,1,1),(0,2,2,2),(1,1,0,1),(1,1,1,3),(1,1,2,1),(1,2,0,1),(1,2,1,2),(1,2,2,2)]

and mu_x=(10,10,0), mu_y=(0,10,10), mu_z=(6,8,6). It has mode ties exactly as the E argument predicts. The fully tied state has three words and the asymmetric (2,1)/(1,2) splits. Singleton probes are outside the charged range and are rejected by maximum-chain maximality.

[COMPUTED] Broad-superset adversarial check: if one ignores the imported heavy-tail inequalities and scans merely unique-mode rows, 122 rows through m=8 have the selected tail at least 2N/3. The explicit row m=5, X=Y=[0,4], Z=[4,5] has

N=36,
mu_x=(11,9,7,5,4,0),
mu_y=(2,4,6,8,16,0),
mu_z=(0,0,0,0,21,15),
A=25>2N/3=24.

But 3*mu_x(rho_x)=33<36, so this row is not a legal charged heavy-gap row. Imposing the heavy inequalities gives upper_bad_heavy 0. This check prevents the invalid inference that a unique mode alone is a heavy mode.

Persistence-floor attack check: interval realization, direct closure and window recovery, exact topological sorting, independent marginal and pair enumeration, symbolic inequality scans, endpoint/equality probes, singleton degeneracy, and the broad heavy-filter stress test were all performed. No additional untried attack remains that is not already covered by the interval parametrization or the direct topological audit.

There is no mathematical [FAILED] step and no [CONJECTURED] step in the charged proof.

## Final conclusion

[PROVED-HERE] CONFIRMED: the pairwise-distinct-heavy Q branch is excluded. The proof uses the correct Cartesian-feasible isotone state space with i<=j, never independent marginals, verifies every disjoint, equality, proper-overlap, endpoint, and tied-block case, and produces the required exact closed-middle numerator whenever the unique-mode chamber survives.

## Provenance

- kg_import | imported from wiki entry q-distinct-heavy-chamber-certificate-independent-decision-ro




# Theorem 12.2 (Q-CH exclusion)

---

## Banked record: `common-heavy-q-exclusion`

# common-heavy-q-exclusion

title: Common-Heavy Q Exclusion
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: The repaired proof exhausts the legal interval cases, identifies a side atom at least as large as the central heavy atom, verifies that the selected tail corresponds to an existing eligible chain element, and uses the complementary heavy atom to prove the strict upper bound. This supersedes the original incomplete Q-common artifact.
[graph-node: kgn_9af048f80f5e — this page is a PROJECTION; truth lives in the research KG]

## Statement

Let P be a finite poset with maximum chain C and P\C={x,y,z}, where x<y and z is incomparable with both x and y. In the exact realizable weighted-gap model, assume x,y,z have the same unique heavy gap r. Then either an incomparable defect pair is balanced, or one of the strict tails L_x(r) or H_y(r) is the orientation numerator of a genuine incomparable defect–chain pair and satisfies N/3<T<2N/3, where N=e(P). Consequently, the common-heavy Q configuration is impossible under closed-third avoidance. Maximum-chain status supplies the needed non-singleton windows and endpoint eligibility; the complementary side contains a heavy atom greater than N/3, giving the upper bound T<2N/3.

## Content

Let P be a finite poset with maximum chain C and P\C={x,y,z}, where x<y and z is incomparable with both x and y. In the exact realizable weighted-gap model, assume x,y,z have the same unique heavy gap r. Then either an incomparable defect pair is balanced, or one of the strict tails L_x(r) or H_y(r) is the orientation numerator of a genuine incomparable defect–chain pair and satisfies N/3<T<2N/3, where N=e(P). Consequently, the common-heavy Q configuration is impossible under closed-third avoidance. Maximum-chain status supplies the needed non-singleton windows and endpoint eligibility; the complementary side contains a heavy atom greater than N/3, giving the upper bound T<2N/3.

## Provenance

- supervisor | work_8fe8697950c8 | banked per finding at effort end



---

## Banked record: `q-common-heavy-closure-decision-round-23-repaired`

# q-common-heavy-closure-decision-round-23-repaired

title: Q Common-Heavy Closure Decision — Round 23 Repaired
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Uses the exact non-Cartesian feasible state set i≤j, the fiber weight W(i,j,k), imported marginal and chain-cut ledgers, maximum-chain exclusion of singleton gap intervals, and an explicit legal threshold whose strict-side tail is an exact chain-cut numerator. The repair separately verifies that the selected tail is a lower bound of at least N/3 and that its threshold satisfies genuine incomparability eligibility.
[graph-node: kgn_915bfabda5b1 — this page is a PROJECTION; truth lives in the research KG]

## Statement

Under the exact realizable three-defect Q-branch hypotheses with a common unique heavy gap and closed-middle-third avoidance, either an incomparable defect pair has orientation numerator in [N/3, 2N/3], or a genuinely incomparable defect–chain pair does. In fact, the repaired argument constructs a defect–chain witness with strict numerator bounds N/3 < T < 2N/3, so the common-heavy Q branch is impossible under closed-third avoidance.

## Content

# q-common-heavy-closure-decision-round-23-repaired

# Q Common-Heavy Closure Decision — Round 23 Repaired

**STATUS: [PROVED].**

**SCOPE.** This is the exact realizable three-defect Q branch: a maximum chain
\(C=(c_1<\cdots<c_m)\), defects \(x<y\) and \(z\parallel x,z\parallel y\),
legal integer gap intervals \(X=I_x=[a,b]\), \(Y=I_y=[c,d]\),
\(Z=I_z=[e,f]\), and exact feasible states
\[
(i,j,k)\in X\times Y\times Z,\qquad i\le j.
\]
The fiber weight is
\[
W(i,j,k)=1+\mathbf1_{i=k}+\mathbf1_{j=k}.
\]
Every incomparable pair avoids the **closed** middle third
\([N/3,2N/3]\), where \(N=e(P)\), and all three defects have the same
unique heavy gap \(r\), supplied by the imported heavy-gap framework.

**DEPENDS-ON (consumed, not reproved).** Canonical gap-fiber bijection;
exact arbitrary-k event dictionary; exact three-defect chain-cut ledger and
defect-pair ledger; closed-third strong-order rigidity; maximum-chain unique
heavy-gap rigidity; and the heavy-gap alignment corollary. Maximum-chain
realizability and ordinal-sum indecomposability remain hypotheses of the
realizable interface. No Cartesian relaxation and no pairwise factorization is
used.

**SUPERSESSION INSTRUCTION.** This entry supersedes
`q-common-heavy-closure-decision-round-23`. The old artifact must be relabeled
**SUPERSEDED — REPAIRED HERE** and must not be cited for the strict-tail to
chain-cut conversion without the local eligibility argument in this entry.

## 1. The exact theorem-level outcome

**[PROVED-HERE]** Under the scope above, either an incomparable defect pair
already has an orientation numerator in the closed interval
\[
N\le 3N_{u<v}\le 2N,
\]
or there is a genuinely incomparable defect-chain pair \((u,c_t)\) with
\[
N\le 3N_{u<c_t}\le 2N
\quad\text{or}\quad
N\le 3N_{c_t<u}\le 2N.
\]
In fact, in the common-heavy Q branch the proof below constructs a defect-chain
witness with the stronger strict inequalities
\[
\frac N3<T<\frac{2N}3.
\]
Thus, under closed-third avoidance, the common-heavy branch is impossible.
The proof keeps endpoint equality as balanced; the strict conclusion here is a
consequence of the imported strict heavy atom, not a redefinition of balance.

## 2. Imported event facts and the precise repair target

**[ARGUED — IMPORTED]** For a feasible gap map \(g\), the canonical fiber has
weight \(W(g)\), and \(N=\sum_gW(g)\). For a defect \(u\), put
\[
\mu_u(q)=\sum_{g:g(u)=q}W(g),\qquad 0\le q\le m.
\]
The exact chain-cut ledger, with strict-left/weak-right convention, is
\[
N_{u<c_t}=\sum_{q<t}\mu_u(q),\qquad
N_{c_t<u}=\sum_{q\ge t}\mu_u(q).\tag{2.1}
\]
The pair \(\{u,c_t\}\) is genuinely incomparable exactly when
\[
a_u<t\le b_u.\tag{2.2}
\]
This includes \(t=1\), \(t=m\), endpoint gaps 0 and \(m\), and all equality-at-the-threshold cases: a state with \(g(u)=t\) contributes to \(c_t<u\), not to \(u<c_t\).

**[ARGUED — IMPORTED]** For distinct defects \(u,v\), the exact defect-pair
ledger is
\[
N_{u<v}=\sum_{g(u)<g(v)}W(g)
 +\sum_{q=0}^m\sum_{g(u)=g(v)=q}
 e(Q_q(g);u<v)\prod_{s\ne q}e(Q_s(g)),\tag{2.3}
\]
with the analogous reverse numerator. The tied-block factor is intrinsic; it
is not a product of pairwise probabilities. In the Q block, the fully tied
local counts are
\[
(e(Q;x<z),e(Q;z<x))=(2,1),
\qquad
(e(Q;y<z),e(Q;z<y))=(1,2),
\]
while a two-element antichain tie splits 1--1. Since \(x<y\) is comparable,
only \(x,z\) and \(y,z\) can be defect-pair alternatives here.

**[ARGUED — IMPORTED]** Common heavy gap means, for every \(u\in\{x,y,z\}\),
\[
\mu_u(r)>\frac N3,
\qquad
L_u(r):=\sum_{q<r}\mu_u(q)<\frac N3,
\qquad
H_u(r):=\sum_{q>r}\mu_u(q)<\frac N3.\tag{2.4}
\]
The inequalities in (2.4) are strict because avoidance is of the closed
third. The proof below uses the common index and these exact integer masses;
it does not infer a witness merely from the words “heavy tail.”

**[FAILED — OLD INFERENCE, REPAIRED HERE]** The unsafe generic move is to
write down a strict tail and call it a genuine cut before checking two separate
facts: (i) the tail is a *lower* bound of at least \(N/3\), not one of the
upper bounds in (2.4), and (ii) the corresponding threshold satisfies
(2.2). The data \(L_u,H_u<N/3\) alone produce neither fact. The repair is to
exhibit, from the Q marginal formulas, a legal gap on the strict side whose
atom is at least the central heavy atom. Then the selected tail is an exact
ledger numerator and its threshold is explicitly eligible. No claim below
uses the unsafe generic implication.

## 3. Realizable Q geometry and singleton exclusion

Write
\[
X=[a,b],\qquad Y=[c,d],\qquad Z=[e,f],
\]
all as integer intervals in \(\{0,\ldots,m\}\). Since \(x<y\), transitivity
along the displayed chain gives
\[
a\le c,\qquad b\le d.\tag{3.1}
\]
Indeed, every chain predecessor of \(x\) is a predecessor of \(y\), and
every chain successor of \(y\) is a successor of \(x\). Since the common
heavy gap belongs to both \(X\) and \(Y\),
\[
J:=X\cap Y=[c,b]\ne\varnothing.\tag{3.2}
\]

**[PROVED-HERE]** Every legal interval has at least two gaps. If
\(I_u=\{q\}\), then every \(c_t\) with \(t\le q\) is below \(u\), and
every \(c_t\) with \(t>q\) is above \(u\), including the endpoint cases
\(q=0,m\). Thus \(C\cup\{u\}\) is a chain of length \(m+1\), contrary to
maximum-chain status. Hence
\[
n_x=b-a+1\ge2,\qquad n_y=d-c+1\ge2,\qquad n_z=f-e+1\ge2.\tag{3.3}
\]
This is where maximum-chain realizability is load-bearing; a formal state
array with singleton windows is not an admissible counterexample.

The exact Q feasible set is
\[
\mathcal F=\{(i,j,k):i\in X,\ j\in Y,\ k\in Z,\ i\le j\}.\tag{3.4}
\]
The tied-block words give the exact integral weight
\[
W(i,j,k)=
\begin{cases}
1,&i,j,k\text{ all distinct, or }i=j\ne k,\\
2,&i=k\ne j\text{ or }j=k\ne i,\\
3,&i=j=k.
\end{cases}\tag{3.5}
\]
There is no Cartesian assertion beyond (3.4): the \(i\le j\) constraint is
retained in every sum.

## 4. Exact integer marginal ledger

Put
\[
F_0=\{(i,j)\in X\times Y:i\le j\},\qquad S=|F_0|.
\]
Summing (3.5) first over the indicated coordinates gives
\[
N=n_zS
 +\sum_{q\in X\cap Z}|Y\cap[q,m]|
 +\sum_{q\in Y\cap Z}|X\cap[0,q]|.\tag{4.1}
\]
For every gap \(q\), with an omitted indicator understood as zero, the exact
atoms are
\[
\begin{aligned}
\mu_x(q)&=\mathbf1_{q\in X}\Bigl(
 n_z|Y\cap[q,m]|
 +\mathbf1_{q\in Z}|Y\cap[q,m]|
 +|Y\cap Z\cap[q,m]|\Bigr),\\
\mu_y(q)&=\mathbf1_{q\in Y}\Bigl(
 n_z|X\cap[0,q]|
 +|X\cap Z\cap[0,q]|
 +\mathbf1_{q\in Z}|X\cap[0,q]|\Bigr),\\
\mu_z(q)&=\mathbf1_{q\in Z}\Bigl(
 S+\mathbf1_{q\in X}|Y\cap[q,m]|
 +\mathbf1_{q\in Y}|X\cap[0,q]|\Bigr).
\end{aligned}\tag{4.2}
\]
For example, in \(\mu_x(q)\), the base term has \(n_z\) choices of \(k\);
the \(i=k\) correction is present only when \(q\in Z\), and the
\(j=k\) correction sums over \(Y\cap Z\cap[q,m]\). The other two lines
are the same exact summation, not a product relaxation. In particular,
\[
\sum_q\mu_x(q)=\sum_q\mu_y(q)=\sum_q\mu_z(q)=N.\tag{4.3}
\]

## 5. The repaired Q* lemma

**[PROVED-HERE]** Under (3.1)--(3.5) and the common-heavy assumptions (2.4),
one of the following exact strict-side tails is at least its corresponding
central atom, and the side atom is a legal gap of the same defect:
\[
L_x(r),\quad H_y(r).
\]
More explicitly, the exhaustive cases are as follows.

### Case 1: \(c=b\)

Then \(r=c=b\). Since \(Z\) is non-singleton and contains \(c\), either
\(e<c\) or \(f>c\) (or both).

* If \(e<c\), then \(c-1,c\in X\cap Z\). With
  \(h=|Y\cap Z|\), (4.2) gives the exact equality
  \[
  \mu_x(c-1)=\mu_x(c)=n_zn_y+n_y+h.\tag{5.1}
  \]
  The central atom is heavy, so
  \[
  L_x(c)\ge\mu_x(c-1)=\mu_x(c)>N/3.\tag{5.2}
  \]

* If \(f>c\), then \(c,c+1\in Y\cap Z\). With
  \(h'=|X\cap Z|\), (4.2) gives
  \[
  \mu_y(c+1)=\mu_y(c)=n_zn_x+n_x+h'.\tag{5.3}
  \]
  Therefore
  \[
  H_y(c)\ge\mu_y(c+1)=\mu_y(c)>N/3.\tag{5.4}
  \]

The first alternative has \(c\ge1\) because \(X\) is non-singleton and ends
at \(c\); the second has \(c+1\le m\) because \(Y\) is non-singleton and
starts at \(c\). Thus neither uses a fictitious chain element.

### Case 2: \(c<b\)

For \(q\in Z\), (4.2) specializes to the following exact integer table:
\[
\mu_z(q)=
\begin{cases}
S+n_y,&q\in X\setminus Y,\\
S+(d-a+2),&q\in J=[c,b],\\
S+n_x,&q\in Y\setminus X,\\
S,&q\notin X\cup Y.
\end{cases}\tag{5.5}
\]
The central correction is strictly larger than both side corrections, with
integer differences
\[
(d-a+2)-n_y=c-a+1\ge1,\qquad
(d-a+2)-n_x=d-b+1\ge1.\tag{5.6}
\]
If \(Z\cap J\) contained some \(q\ne r\), then (5.5) would give
\(\mu_z(q)=\mu_z(r)>N/3\). Whichever side of \(r\) contains \(q\) would then
have strict tail at least \(\mu_z(q)>N/3\), contradicting (2.4) for \(z\).
Consequently
\[
Z\cap J=\{r\}.\tag{5.7}
\]

Both \(Z\) and \(J\) are non-singleton intervals. Therefore (5.7) forces
exactly one of the two endpoint shapes
\[
\text{(L)}\quad r=c,\quad Z=[e,c],\ e<c;
\qquad
\text{(R)}\quad r=b,\quad Z=[b,f],\ f>b.\tag{5.8}
\]
An interior \(r\) would have a neighboring point of \(Z\) in \(J\), and an
endpoint cannot extend through \(J\) without creating a second intersection.

#### Shape (L): \(r=c\), \(Z=[e,c]\)

If \(a<c\), then \(c-1,c\in X\cap Z\), and now \(Y\cap Z=\{c\}\), so
\[
\mu_x(c-1)=\mu_x(c)=n_zn_y+n_y+1>N/3.\tag{5.9}
\]
Thus \(L_x(c)>N/3\).

If \(a=c\), then \(n_x=b-c+1\ge2\), and (4.2) gives the exact values
\[
\mu_y(c)=n_z+2,\qquad
\mu_y(b)=n_zn_x+1,
\]
so
\[
\mu_y(b)-\mu_y(c)=n_z(n_x-1)-1\ge2\cdot1-1=1.\tag{5.10}
\]
The central atom \(\mu_y(c)\) is greater than \(N/3\), hence
\(\mu_y(b)>N/3\), and \(b>c\) lies in the strict right tail:
\[
H_y(c)\ge\mu_y(b)>N/3.\tag{5.11}
\]

#### Shape (R): \(r=b\), \(Z=[b,f]\)

If \(d>b\), then \(b,b+1\in Y\cap Z\), and (4.2) gives
\[
\mu_y(b+1)=\mu_y(b)=n_zn_x+n_x+1>N/3.\tag{5.12}
\]
Thus \(H_y(b)>N/3\).

If \(d=b\), then \(n_y=b-c+1\ge2\), and (4.2) gives
\[
\mu_x(c)=n_zn_y+1,\qquad
\mu_x(b)=n_z+2,
\]
so
\[
\mu_x(c)-\mu_x(b)=n_z(n_y-1)-1\ge1.\tag{5.13}
\]
Since \(\mu_x(b)>N/3\), also \(\mu_x(c)>N/3\), and \(c<b\) lies in the
strict left tail:
\[
L_x(b)\ge\mu_x(c)>N/3.\tag{5.14}
\]

Equations (5.1)--(5.14) are all integer equalities or integer inequalities;
no limiting or real-valued approximation is used.

## 6. Genuine cut conversion, with endpoints and equality retained

The preceding cases do more than produce a large number: they produce the
required eligible threshold.

* Whenever \(T=L_x(r)\) is selected, the proof exhibits a gap \(s<r\) in
  \(X\) (either \(s=r-1\) or \(s=c<r=b\)) as well as \(r\in X\).
  Hence \(a\le s<r\le b\), in particular \(a<r\le b\). Therefore
  \(\{x,c_r\}\) is genuinely incomparable and, by (2.1),
  \[
  T=L_x(r)=N_{x<c_r}.\tag{6.1}
  \]
  The existence of \(s\ge0\) forces \(r\ge1\), so \(c_r\) exists.

* Whenever \(T=H_y(r)\) is selected, the proof exhibits a gap \(s>r\) in
  \(Y\) (either \(s=r+1\) or \(s=b>r=c\)) as well as \(r\in Y\).
  Hence \(c<r+1\le s\le d\), in particular \(c<r+1\le d\). Therefore
  \(\{y,c_{r+1}\}\) is genuinely incomparable and, by (2.1),
  \[
  T=H_y(r)=N_{c_{r+1}<y}.\tag{6.2}
  \]
  The existence of \(s\le m\) forces \(r<m\), so \(c_{r+1}\) exists.

This is the exact strict-tail-to-cut repair. It explicitly rules out a
forced pair and never invokes \(c_0\) or \(c_{m+1}\). It also covers the
fallback endpoint cases \(a=c\) and \(d=b\), which are precisely where a
naive adjacent-atom sentence would be insufficient.

Now let \(M=\mu_u(r)\) be the central atom for the selected defect. The
selected \(T\) is a strict tail, so \(N-T\ge M>N/3\). Equations (5.2),
(5.4), (5.9), (5.11), (5.12), and (5.14) give \(T\ge M\) (strictly \(T>M\) in the endpoint-spike cases and
equality in the flat cases); in every case \(T\ge M>N/3\). Consequently, in exact integer form,
\[
3T>N,
\qquad
3(N-T)>N,
\qquad
3T<2N.\tag{6.3}
\]
Thus
\[
\boxed{\frac N3<T<\frac{2N}3}.\tag{6.4}
\]
In particular \(T\) lies in the requested closed interval.

If a defect-pair numerator instead satisfies \(N\le3N_{u<v}\le2N\), it is
already a balanced incomparable pair by the exact ledger (2.3), including the
cases of equality. Under the charged closed-third avoidance, that alternative
is forbidden; the genuine chain witness (6.1) or (6.2) is also forbidden.
Therefore the common-heavy Q branch cannot occur.

## 7. Boundary, realizability, and rejected diagnostic audits

**[PROVED-HERE] Endpoint audit.** A left-tail witness always has a real index
\(r\in\{1,\ldots,m\}\); a right-tail witness always has
\(r+1\in\{1,\ldots,m\}\). The singleton proof (3.3) is the only use of
maximum-chain maximality in the local case split, and it is what supplies
\(n_x,n_y,n_z\ge2\) in (5.10) and (5.13). All other endpoint claims follow
from the displayed interval inclusions. The formal gap endpoints 0 and \(m\)
remain allowed; they simply cannot be selected as a missing-side chain cut.

**[PROVED-HERE] Equality audit.** Balance is the closed condition
\(N\le3T\le2N\), not a strict condition. If any exact numerator equals
\(N/3\) or \(2N/3\), it is a valid witness and is not discarded. The present
common-heavy construction is actually strict because the imported central
atom is strictly greater than \(N/3\); this does not weaken or alter the
closed-third statement.

**[COMPUTED — FALSIFICATION SUPPORT ONLY]** The old state-only diagnostic was
recomputed exactly for
\[
m=2,\quad X=[1,2],\quad Y=[0,1],\quad Z=[0,1],\quad r=1.
\]
Its states and weights are \((1,1,0;1)\), \((1,1,1;3)\), hence
\[
N=4,\quad
(\mu_x(0),\mu_x(1),\mu_x(2))=(0,4,0),
\]
\[
(\mu_y(0),\mu_y(1),\mu_y(2))=(0,4,0),\quad
(\mu_z(0),\mu_z(1),\mu_z(2))=(1,3,0).
\]
The defect-pair numerators are
\[
N_{x<z}=2,\\quad N_{z<x}=2,\\quad
N_{y<z}=1,\\quad N_{z<y}=3,
\]
so \(x,z\) is already balanced at \(N/2\). The eligible cut numerator pairs
are \((4,0)\) for \((x,c_2)\), \((0,4)\) for \((y,c_1)\), and \((1,3)\)
for \((z,c_1)\); none is in the middle third. This is not a counterexample:
\(a\le c,b\le d\) fails (\(1\le0\) is false and \(2\le1\) is false), and
transitive closure adds
\[
c_1<x<y<c_2,
\]
which has height 4 although the displayed chain has \(m=2\). The exact
incomparability graph has components
\(\{c_1,x,y,z\}\) and \(\{c_2\}\), so the closure is ordinal-sum
decomposable. The diagnostic therefore violates both maximum-chain
realizability and the indecomposable scope, as well as closed-third avoidance
through the balanced pair.

## 8. Executed computation record (support only)

The exact audit was executed in-session from
`outputs/code/q_common_heavy_closure_round23_repaired_audit.py`; its captured
output is
`outputs/code/q_common_heavy_closure_round23_repaired_audit-output.txt`.
The load-bearing lines were:

```text
formula_cases_m1_to_8 35178
formula_and_marginal_assertions ALL_PASS
repaired_selection_cases_m1_to_8 7182
repaired_selection_case_breakdown {'c=b/Zbelow': 2772, 'c=b/Zabove': 714, 'r=c/a<c': 1386, 'r=c/a=c': 462, 'r=b/d>b': 1386, 'r=b/d=b': 462}
repaired_eligibility_and_flat/more-atom_assertions ALL_PASS
common-heavy_search_m1_to_8_(m,instances,no_balanced_chain_cut) [(1, 0, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0), (7, 0, 0), (8, 0, 0)]
diagnostic_N 4 diagnostic_marginals [[0, 4, 0], [0, 4, 0], [1, 3, 0]]
diagnostic_defect_pair_numerators {'x<z': 2, 'z<x': 2, 'y<z': 1, 'z<y': 3}
diagnostic_closed_middle_pair_xz True
diagnostic_incomparability_components [['c1', 'x', 'y', 'z'], ['c2']]
diagnostic_height_chain ['c1', 'x', 'y', 'c2'] height 4 displayed_m 2
```

A separate direct labeled-poset attack was executed from
`outputs/code/q_common_heavy_closure_round23_poset_attack.py` and returned:

```text
poset_attack_m 2 free_pairs 6 raw_posets 196 max_chain 12 indecomposable 12 common_heavy 0 common_heavy_no_chain_middle 0 common_heavy_and_full_avoidance 0
poset_attack_m 3 free_pairs 9 raw_posets 2128 max_chain 208 indecomposable 144 common_heavy 0 common_heavy_no_chain_middle 0 common_heavy_and_full_avoidance 0
```

These finite scans are falsification support only; the proof is the unbounded
integer case split in Sections 3--6.

**[FAILED — DISCARDED COMPUTATION]** One preliminary scratch audit stopped
before producing a result with `ValueError: too many values to unpack
(expected 2)` after treating an interval list as a two-entry endpoint pair.
No value from that run is used. The corrected persisted audit above reran the
same checks and returned the quoted `ALL_PASS` lines.

## Final disposition

**[PROVED-HERE] PROVED.** The common-heavy Q branch supplies a genuine
incomparable defect-chain numerator in the closed middle third (indeed in its
open middle), unless a defect pair is already balanced; equality is retained
as balanced, and all singleton, endpoint, transitive-closure,
maximum-chain, and indecomposability issues are explicitly accounted for.
The old artifact is superseded by this repaired record.


---
provenance: actor=work_math_manager_streaming work_id=work_8fe8697950c8 node_id=q_common_heavy_closure_record_repair banked=2026-08-17T18:33:04Z

## Provenance

- work_math_manager_streaming | work_8fe8697950c8 | q_common_heavy_closure_record_repair | imported from wiki entry q-common-heavy-closure-decision-round-23-repaired



---

## Banked record: `q-common-heavy-exclusion-is-presentation-general`

# q-common-heavy-exclusion-is-presentation-general

title: Q Common-Heavy Exclusion Is Presentation-General
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: The round audited the repaired common-heavy Q certificate and its exact gap-fiber dependencies, including genuine cut eligibility and noncircularity.
[graph-node: kgn_f1be1ae41c94 — this page is a PROJECTION; truth lives in the research KG]

## Statement

Let P be a finite poset with any displayed maximum chain C and P\C={x,y,z}, where x<y and z is incomparable with both x and y. Under CLOSED-THIRD avoidance, the three defects cannot have one common heavy gap. This conclusion holds for every valid Q-labeling and every displayed maximum chain; it requires no canonical presentation, centering, endpoint normalization, Cartesian relaxation, finite bound on |C|, or invariance between different chain presentations.

## Content

Let P be a finite poset with any displayed maximum chain C and P\C={x,y,z}, where x<y and z is incomparable with both x and y. Under CLOSED-THIRD avoidance, the three defects cannot have one common heavy gap. This conclusion holds for every valid Q-labeling and every displayed maximum chain; it requires no canonical presentation, centering, endpoint normalization, Cartesian relaxation, finite bound on |C|, or invariance between different chain presentations.

## Provenance

- supervisor | work_39ddcfed4a36 | banked per finding at effort end




# Theorem 12.3 (Q1, Q2 structural exclusion)

---

## Banked record: `q1-q2-two-equal-structural-exclusion`

# q1-q2-two-equal-structural-exclusion

title: Q1–Q2 Two-Equal Structural Exclusion
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: The coordinate-mode structure separates the heavy indices, while direct region accounting exhibits states missing from the attempted V cover.
[graph-node: kgn_be26b72cd9cd — this page is a PROJECTION; truth lives in the research KG]

## Statement

In the exact Q model F_Q={(i,j,k):i∈X,j∈Y,k∈Z,i≤j} with W_Q=1+1_{i=k}+1_{j=k}, the Q1 and Q2 two-equal patterns, in which the equal heavy indices belong to the comparable coordinates x and y, are excluded by unique-mode separation: ρ_x≠ρ_y. They therefore require a structural pin rather than a transfer of the V residual identity. A V-style H,L,Z,Ω cover is invalid because Q has no constraint i≤k and consequently omits mixed regions such as i<σ,j=σ and i=σ,j>σ.

## Content

In the exact Q model F_Q={(i,j,k):i∈X,j∈Y,k∈Z,i≤j} with W_Q=1+1_{i=k}+1_{j=k}, the Q1 and Q2 two-equal patterns, in which the equal heavy indices belong to the comparable coordinates x and y, are excluded by unique-mode separation: ρ_x≠ρ_y. They therefore require a structural pin rather than a transfer of the V residual identity. A V-style H,L,Z,Ω cover is invalid because Q has no constraint i≤k and consequently omits mixed regions such as i<σ,j=σ and i=σ,j>σ.

## Provenance

- supervisor | work_060eb331f93e | banked per finding at effort end




# Lemma 12.4 (Disjoint-branch closure)

---

## Banked record: `r29-q-tied-xz-separated-y-above-closed`

# r29-q-tied-xz-separated-y-above-closed

title: Exclusion of the R29 Q Cell with Tied xz and y Above
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Banked enumeration and exact marginal formulas reduce the possibilities to two mode chambers. In each chamber, explicit state-sum formulas show that a genuine chain pair has a strict-tail numerator in the forbidden closed middle third, while the complementary heavy atom exceeds \(N/3\); independent certificate and topological-sort replays verify the classification and inequalities.
[graph-node: kgn_ea6d55d0ff74 — this page is a PROJECTION; truth lives in the research KG]

## Statement

The exact Q marginal cell \(\rho_x=\rho_z=s<\rho_y=t\) is impossible under CLOSED-THIRD. Exhaustive mode classification leaves only the separated D chamber and the left-overlap chamber; in each, a genuine chain-pair strict-tail numerator \(A\) satisfies \(N/3<A<2N/3\), contradicting the closed middle-third condition.

## Content

# r29-q-tied-xz-separated-y-above-closed

# R29 Q cell: tied incomparable pair xz, separated y above

STATUS: PROVED (CLOSED)

[ARGUED — BANKED ENUMERATION, classification only] The full shelf entry `round29-exhaustive-two-equal-cell-partition` identifies the cell exactly as `rho_x=rho_z=s<rho_y=t`. The reverse order is infeasible because `x<y` and heavy-gap alignment forbid `rho_y<rho_x`.

[ARGUED — BANKED PROVED DEPENDENCIES] Consume `uniform-arbitrary-k-gap-map-realization-and-canonical-fiber`, `complete-k-2-event-dictionary`, `maximum-chain-heavy-gap-rigidity`, and `heavy-gap-alignment-corollary-under-closed-third-avoidance`. At a separated xz tie the k=2 doubled diagonal supplies the two internal orders and weight 2; at the full diagonal use the intrinsic Q weight 3 and split `(xz,zx)=(2,1)`. The third coordinate remains constrained by `i<=j`, never by an independent Cartesian relaxation.

[PROVED-HERE] Let `X=[a,b]`, `Y=[c,d]`, `Z=[e,f]`, with lengths `n_x,n_y,n_z>=2`. The exact Q marginal formulas give the following exhaustive unique-mode alternatives. If `b<c`, uniqueness forces `Z=[b,c]`, `rho_x=b`, `rho_y=c`, and `rho_z=b` exactly when `n_y>n_x`; this is the D realization of the charged cell. If `c=b`, a non-singleton Z creates a two-point maximal plateau, so no heavy row exists. If `c<b`, unique xz coincidence forces the left endpoint chamber `Z=[e,c]`, then uniqueness forces `X=Y=[c,b]`; the modes are `(c,b,c)`.

In D put `N=n_z n_x n_y+n_x+n_y` and select the genuine chain pair `{x,c_b}`. Its exact numerator is the strict left tail of x at its heavy mode:
`A=(n_x-1)(n_z n_y+1)`. Since `n_y>n_x>=2`,
`3A-N=n_z n_y(2n_x-3)+2n_x-n_y-3>0`:
for `n_x=2` it is `(n_z-1)n_y+1>0`, and for `n_x>=3` it is at least `n_y(4n_x-7)+2n_x-3>0`. The cut is genuine because `a<b`; the heavy atom gives `N-A>N/3`, so `A<2N/3`. Thus `N/3<A<2N/3`, forbidden by CLOSED-THIRD.

In the left-overlap chamber put `n=b-c+1>=2`, `s=n_z>=2`, `P=n(n+1)/2`. The exact state sum and the strict lower tail of y at its mode b are
`N=sP+n+1`, `A=s(P-n)+n`, and
`3A-N=s*n*(n-2)+2*n-1>0`.
Here `A=N_{y<c_b}` and `c<b`, so the pair is genuine; again `N-A>=mu_y(b)>N/3`, giving `A<2N/3`. This closes the second possible xz mode chamber.

[COMPUTED — independent replay] The exact certificate script, SHA-256 `d6b709825c316702b33bd8dd7b8e3d4a8ceca51928866597a8833bced26a436f`, returned `xz-y-above 1792`, `TAIL_CERTIFICATE_FAILURES 0`, `SYMBOLIC_INEQUALITY_SAMPLE_FAILURES 0`, `MARGINAL_FORMULA_FAILURES 0`, and `MODE_CLASSIFICATION_FAILURES 0` on `264199` legal triples through `m=12`. Saved stdout hash: `940e592f6ebe7eef06ff0d2bda6c9d99b2950770eb5f1c730dfa7ba5be3a8eaa`. A separate recursive topological-sort replay, `outputs/code/q_r29_topological_replay.py` (SHA-256 `32efb2cf63ffd2a784db9e28f007e884ba3874897a296b9426d771956b4a606b`), returned for D-xz `(topological_extensions,weighted_states,modes)=(30,24,((1,),(3,),(1,)))` and for L-xz `(22,18,((2,),(4,),(2,)))`, with `TOPOLOGICAL_REPLAY_VERDICT PASS`; stdout hash `1156319c833daac8aaa2def94cce970adcc189da1c964f13f06b8f53b7207196`.

[PROVED-HERE] The exact cell `rho_x=rho_z=s<rho_y=t` is therefore excluded by a referee-ready genuine chain-pair numerator in the closed middle third.

---
provenance: actor=work_math_manager_streaming work_id=work_d06eac75f5cd node_id=close-q-two-equal-cells banked=2026-08-18T01:09:34Z

## Provenance

- work_math_manager_streaming | work_d06eac75f5cd | close-q-two-equal-cells | imported from wiki entry r29-q-tied-xz-separated-y-above-closed



---

## Banked record: `r29-q-tied-yz-separated-x-below-closed`

# r29-q-tied-yz-separated-x-below-closed

title: Exclusion of the Q Cell with Tied y,z Modes and x Below
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Banked mode classification reduces the cell to two chambers. In the disjoint chamber, the pair \(\{c_{c+1},y\}\) has \(A=(n_y-1)(n_zn_x+1)\) and \(3A-N>0\), while the heavy atom gives \(A<2N/3\). In the genuine-overlap chamber, the pair \(\{c_{c+1},x\}\) has \(A=s(P-n)+n\) and \(3A-N=s n(n-2)+2n-1>0\), with the complementary mass again exceeding \(N/3\). Thus each chamber violates CLOSED-THIRD; exhaustive replay found no exceptions among 264,199 legal triples through \(m=12\).
[graph-node: kgn_8ddd1ca17ec0 — this page is a PROJECTION; truth lives in the research KG]

## Statement

The exact cell \(\rho_x=t<\rho_y=\rho_z=s\) is impossible under CLOSED-THIRD. In the disjoint and genuine-overlap marginal chambers, an explicitly constructed genuine chain pair has numerator \(A\) satisfying \(N/3<A<2N/3\), contradicting the CLOSED-THIRD condition; the result is independently certified by exhaustive computation and topological replay.

## Content

# r29-q-tied-yz-separated-x-below-closed

# R29 Q cell: tied incomparable pair yz, separated x below

STATUS: PROVED (CLOSED)

[ARGUED — BANKED ENUMERATION, classification only] The full shelf entry `round29-exhaustive-two-equal-cell-partition` identifies this cell exactly as `rho_x=t<rho_y=rho_z=s`. The opposite order is infeasible from `x<y` and heavy-gap alignment.

[ARGUED — BANKED PROVED DEPENDENCIES] Consume `uniform-arbitrary-k-gap-map-realization-and-canonical-fiber`, `complete-k-2-event-dictionary`, `maximum-chain-heavy-gap-rigidity`, and `heavy-gap-alignment-corollary-under-closed-third-avoidance`. The yz tied slice uses the exact doubled-diagonal weight 2; the full Q diagonal is retained at weight 3 with `(yz,zy)=(1,2)`. The separated x coordinate is not independent: all states satisfy `i<=j`.

[PROVED-HERE] With `X=[a,b]`, `Y=[c,d]`, `Z=[e,f]` and all lengths at least 2, the exact marginal chamber analysis is the dual of the xz case. In the disjoint chamber `b<c`, uniqueness forces `Z=[b,c]`, modes `rho_x=b`, `rho_y=c`, and `rho_z=c` exactly when `n_x>n_y`; this is the D realization of the cell. In the one-point overlap chamber `c=b`, non-singleton Z produces a two-point maximal plateau. In genuine overlap `c<b`, the yz coincidence forces the right endpoint chamber `Z=[b,f]`, then uniqueness forces `X=Y=[c,b]`, with modes `(c,b,b)`.

In D select `{c_{c+1},y}`. Its exact numerator is the strict right tail of y at mode c:
`A=(n_y-1)(n_z n_x+1)`, while `N=n_z n_x n_y+n_x+n_y`. Since `n_x>n_y>=2`,
`3A-N=n_z n_x(2n_y-3)+2n_y-n_x-3>0`:
for `n_y=2` it is `(n_z-1)n_x+1>0`, and for `n_y>=3` it is at least `n_x(4n_y-7)+2n_y-3>0`. The cut is genuine because `c<d`; the heavy atom gives `N-A>N/3`, so `A<2N/3`. Hence `N/3<A<2N/3`, violating CLOSED-THIRD.

In the right-overlap chamber put `n=b-c+1>=2`, `s=n_z>=2`, `P=n(n+1)/2`. The exact total and strict right tail of x at mode c are
`N=sP+n+1`, `A=s(P-n)+n`, and
`3A-N=s*n*(n-2)+2*n-1>0`.
Here `A=N_{c_{c+1}<x}` and `c<c+1<=b`, so the pair is genuine; `N-A>=mu_x(c)>N/3` gives `A<2N/3`. This closes the second yz mode chamber.

[COMPUTED — independent replay] The exact certificate script, SHA-256 `d6b709825c316702b33bd8dd7b8e3d4a8ceca51928866597a8833bced26a436f`, returned `yz-x-below 1792`, `TAIL_CERTIFICATE_FAILURES 0`, `SYMBOLIC_INEQUALITY_SAMPLE_FAILURES 0`, `MARGINAL_FORMULA_FAILURES 0`, and `MODE_CLASSIFICATION_FAILURES 0` over `264199` legal triples through `m=12`. Saved stdout hash: `940e592f6ebe7eef06ff0d2bda6c9d99b2950770eb5f1c730dfa7ba5be3a8eaa`. The independent topological replay returned D-yz `(30,24,((3,),(5,),(5,)))` and R-yz `(22,18,((1,),(3,),(3,)))`, and `TOPOLOGICAL_REPLAY_VERDICT PASS`; saved stdout hash `1156319c833daac8aaa2def94cce970adcc1891c964f13f06b8f53b7207196`.

[PROVED-HERE] The exact cell `rho_x=t<rho_y=rho_z=s` is excluded by the displayed genuine chain-pair numerator.

---
provenance: actor=work_math_manager_streaming work_id=work_d06eac75f5cd node_id=close-q-two-equal-cells banked=2026-08-18T01:09:35Z

## Provenance

- work_math_manager_streaming | work_d06eac75f5cd | close-q-two-equal-cells | imported from wiki entry r29-q-tied-yz-separated-x-below-closed




# Theorems 12.5-12.6 (Corrected Q3/Q4 transfer and closure)

---

## Banked record: `q3-l-and-q4-r-diagonal-correction`

# q3-l-and-q4-r-diagonal-correction

title: Q3-L and Q4-R diagonal correction
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: The six-permutation Q fiber was compared term by term with the guarded-V fiber, locating the single additional diagonal contribution.
[graph-node: kgn_31e76743caf2 — this page is a PROJECTION; truth lives in the research KG]

## Statement

In both corrected transformed Q branches, the exact transfer from the guarded-V ledger is N_Q=N_V+1, H_Q=H_V+1, and L_Q=L_V. In Q3-L the added diagonal unit lies on the original orientation x<z, transformed as r'<q'; in Q4-R it lies on the original orientation z<y, transformed as r<q.

## Content

In both corrected transformed Q branches, the exact transfer from the guarded-V ledger is N_Q=N_V+1, H_Q=H_V+1, and L_Q=L_V. In Q3-L the added diagonal unit lies on the original orientation x<z, transformed as r'<q'; in Q4-R it lies on the original orientation z<y, transformed as r<q.

## Provenance

- supervisor | work_c5d4bc1726bd | banked per finding at effort end



---

## Banked record: `corrected-q3-l-q4-r-full-diagonal-transfer`

# corrected-q3-l-q4-r-full-diagonal-transfer

title: Corrected Q3-L/Q4-R Full-Diagonal Transfer
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: The +1 diagonal transfer is combined with a strict-facet signed certificate and a separate D=F boundary atlas; this supplies the integer floor absent from the bare Full-Cone inequality.
[graph-node: kgn_994ec2d67e2b — this page is a PROJECTION; truth lives in the research KG]

## Statement

For every realizable corrected Q3-L or Q4-R overlap instance transferred to the canonical guarded-V TE(2=1) cone, the exact count relations are N_Q=N_V+1, H_Q=H_V+1, and L_Q=L_V. Hence simultaneous failure of both corrected Q bounds is equivalent, by integrality, to N_V−3H_V≥3 and N_V−3L_V≥0. On the strict facet D<F, the exhaustive 31-chamber signed H-certificate contradicts these simultaneous inequalities, including all unaligned endpoint chambers. On D=F, the separate boundary atlas supplies the strict floor 3L_V−N_V≥1, closing the correction-sensitive L-active residual and the equality case L_V=H_V+1. The aligned sign is −P_b=3H_Q−N_Q=0·(N_Q−3L_Q)−1·(N_Q−3H_Q). Thus every corrected Q3-L and Q4-R chamber and boundary is certified, and Q-2E-34 is closed.

## Content

For every realizable corrected Q3-L or Q4-R overlap instance transferred to the canonical guarded-V TE(2=1) cone, the exact count relations are N_Q=N_V+1, H_Q=H_V+1, and L_Q=L_V. Hence simultaneous failure of both corrected Q bounds is equivalent, by integrality, to N_V−3H_V≥3 and N_V−3L_V≥0. On the strict facet D<F, the exhaustive 31-chamber signed H-certificate contradicts these simultaneous inequalities, including all unaligned endpoint chambers. On D=F, the separate boundary atlas supplies the strict floor 3L_V−N_V≥1, closing the correction-sensitive L-active residual and the equality case L_V=H_V+1. The aligned sign is −P_b=3H_Q−N_Q=0·(N_Q−3L_Q)−1·(N_Q−3H_Q). Thus every corrected Q3-L and Q4-R chamber and boundary is certified, and Q-2E-34 is closed.

## Provenance

- supervisor | work_8d7166a8feca | banked per finding at effort end



---

## Banked record: `aligned-corrected-q3-l-q4-r-formulas`

# aligned-corrected-q3-l-q4-r-formulas

title: Aligned Corrected Q3-L/Q4-R Formulas
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: Closed-form enumeration and direct algebraic factorization of the corrected residual.
[graph-node: kgn_159289b76750 — this page is a PROJECTION; truth lives in the research KG]

## Statement

For every aligned corrected Q3-L or Q4-R instance with n=D−A+1≥2 and m=F−D+1≥2, the exact counts are N_Q=mn(n+1)/2+n+1, H_Q=mn(n−1)/2+n, and L_Q=mn(n−1)/2. Consequently H_Q−L_Q=n and 3H_Q−N_Q=mn(n−2)+2n−1≥3, so every aligned instance satisfies the required corrected Q bound.

## Content

For every aligned corrected Q3-L or Q4-R instance with n=D−A+1≥2 and m=F−D+1≥2, the exact counts are N_Q=mn(n+1)/2+n+1, H_Q=mn(n−1)/2+n, and L_Q=mn(n−1)/2. Consequently H_Q−L_Q=n and 3H_Q−N_Q=mn(n−2)+2n−1≥3, so every aligned instance satisfies the required corrected Q bound.

## Provenance

- supervisor | work_8d7166a8feca | banked per finding at effort end



---

## Banked record: `corrected-ordered-partition-audit-and-final-verdict-for-q-2e`

# corrected-ordered-partition-audit-and-final-verdict-for-q-2e

title: Corrected Q-2E-34 Ordered-Partition Audit
type: note | label: mixed | verification: unverified
namespace: third23
mechanism: Combines proved combinatorial counting and chamber arguments with an independently computed replay and an argued audit of recorded dependencies; the 44 count is reinterpreted as the x≤y count rather than equality alone.
[graph-node: kgn_ce996c518d3b — this page is a PROJECTION; truth lives in the research KG]

## Statement

The audit reports CONFIRMED/PASS for the corrected Q-2E-34 replay: the ordered-partition count is 75, decomposed as 13 cases with x=y, 31 with x>y, and 31 with x<y; the earlier “44 with x=y” label should read x≤y. The replay also reports validation of the strict and boundary chamber atlases, signed certificate identities, Q3-L/Q4-R transfers, and the strict-floor mechanism, with no uncovered chamber or invalid certificate found.

## Content

# Corrected ordered-partition audit and final verdict for Q-2E-34 independent replay

# Corrected ordered-partition audit and final verdict for Q-2E-34 independent replay

status: as labeled in the artifact (session deliverable, banked VERBATIM by the harness)

HEADLINE: CONFIRMED/PASS. The exact ordered-partition count is 75 = 13 with x=y + 31 with x>y + 31 with x<y; the prior 44-with-x=y statement is a count-label error, because 44 counts x≤y (equivalently x≥y after symmetry), not equality alone. The corrected replay independently validates the 31 strict chambers, 31 D=F boundary chambers, all signed certificate identities, the Q3-L/Q4-R transfer, and the strict-floor mechanism; no uncovered chamber, invalid boundary, or invalid signed certificate was found.

# q_2e_34_reconciled_certificate_independent_replay — theorem audit

## Verdict

[PROVED-HERE] **CONFIRMED/PASS.** The erroneous statement `44 with x=y` is only a prose/count-label error. It does not alter the chamber set, exhaustiveness, disjointness, D<F/D=F coverage, the corrected signs, the L-active residual, the equality case L_V=H_V+1, the strict-facet H certificate, the separate D=F atlas, or the exclusion of invalid H-active use of S_H^V.

[COMPUTED] The repaired in-session replay returned `VERDICT PASS`; its persisted result is `outputs/artifacts/reconciled_q_2e_34_signed_full_diagonal_certificate_20260818/replay_results.json`, with result hash `58c6d5909596794f2561882c625afb3193d077b92f9918dc0fce656a0cbd1e8`. The JSON still contains the obsolete field label `x_eq_y: 44`; this audit corrects its meaning to `x_le_y: 44`, and replaces the equality count by the exact value 13 proved below.

## 1. Records and dependencies audited

[COMPUTED] The completed internal replay was located as the wiki projection `independent-replay-of-reconciled-q-2e-34-signed-full-diagona`, titled `Independent replay of reconciled Q-2E-34 signed full-diagonal certificate`. Its prior status was GAP because its first checker stopped at schema errors before certificate identities or Q-transfer rows. The banked certificate it audited was `q-2e-34-full-diagonal-certificates-and-closure-decision`, titled `Q-2E-34 full-diagonal certificates and closure decision`; that record was FAILED-AT only because the corrected L-active strict floor had not yet been independently replayed.

[ARGUED] The following certified Full-Cone dependencies were consumed with their recorded scopes:

| slug | node or recorded snapshot |
|---|---|
| `full-cone-te-2-1-theorem-closing-v-2e-tied-siblings` | node `kgn_d9e87643b122`; snapshot `cb2399fb98e28e2364846e9099afb50f4cb95fc33ec703538ee3549b4681a3e6` |
| `independent-full-cone-te-2-1-certificate-replay` | node `kgn_ed5c52361408`; snapshot `8e4ebaaf4c24ff2b9ddaeaf9d06e7bcf16f6a1f4b2e8d3ccbee45edefbb059a8` |
| `gated-te21-chamber-atlas-and-exact-certificates` | node `kgn_5eb432672414`; snapshot `4d51f9462d610f60e4531aeb94042c029e1ca57a3310426616802bd2046d27cd` |
| `exact-d-f-facet-certificate-atlas-for-guarded-te-2-1` | node `kgn_169d5d6d9e5c`; snapshot `02d3f82765bbe3c2840848fe7ee18c8faf0b1f8ac733c7cf4d970ea171fe751f` |
| `normalized-d-f-0-te-2-1-facet-certificate-atlas` | named in the Full-Cone record and boundary atlas record |
| `independent-exact-replay-of-the-d-f-facet-atlas` | named in the Full-Cone record and boundary replay record |
| `corrected-q-fiber-substrate` | recorded snapshot `38e39cb110261bb844814dba8d539c69ceafa81810783857b670dc5309592866` |
| `authoritative-q3-l-and-q4-r-six-permutation-fiber-event-subs` | recorded snapshot `e61cb9bb25a276492d36266c65f7377906cf9bcc70412e7803212c462ab9056b` |
| `q-two-equal-cells-versus-te-2-1-pin-exact-relationship-audit` | recorded snapshot `0928ef7f42e0753031a80aa2e6db0d7b69ed681f1e3b446bbf654822a69bb5d8` |
| `q3-l-corrected-v-transfer` | recorded snapshot `1fd7fe08ab6b54d2c72f5e0ca69cd3f113932edb841df0d657f3cfee84b03ff9` |
| `q4-r-corrected-v-transfer` | recorded snapshot `cdc86d1e9d18fb9419f1d15142bde6c161502548f8b4bace35782733e8cfc59` |
| `q3-q4-separate-d-branch-pin` | recorded snapshot `2be3970552e3f67d9d800e9ca31a5d8de31bebc111af3070c3eccdb16816b5db` |
| `r30-minimal-pin-literal-recovery-and-independent-exact-repla` | recorded snapshot `49726017e430c68e9ad307f3156eee69d49e1e7e14213387210b72e6032078ed` |
| `Round 33 Supervisor Verdict` | recorded snapshot `fcfd73e8c6ddd04aa35ecdb205b073d1173c44ef86ee6891c33207b087b06a7a` |

[ARGUED] The Full-Cone theorem dependency states that canonical sibling exchange gives D≤F and therefore the two cases D<F and D=F are mutually exclusive and exhaustive. Its strict branch uses the 31-chamber/62-certificate atlas; its boundary branch uses the separate 31-cell D=F atlas.

## 2. Exact definitions and corrected ordered-partition count

[PROVED-HERE] Start with the guarded V intervals

`I_p=[A,B]`, `I_q=[C0,D]`, `I_r=[E,F]`,

and normalize by exchanging the two siblings so that D≤F. Translate by D. Define

`x=D-A`, `y=D-B`, `c=D-C0`, `e=D-E`, `f=F-D`.

Then

`A=-x`, `B=-y`, `C0=-c`, `D=0`, `E=-e`, `F=f`.

The strict facet D<F has `f≥1`; the boundary facet D=F has `f=0`. The maximum-chain/non-singleton conditions give `x>y≥0`; the other normalized inequalities give `c≥1` and `e≥0` on D<F, and `e≥1` on D=F.

[PROVED-HERE] The relevant chamber partition is the weak order of the four labeled integer quantities `{x,y,c,e}`, listed from lowest to highest. A block denotes equality and a bar denotes a strict level increase. Each strict level gap is parameterized as `1+z_i` with `z_i≥0`; the lowest level is an offset plus a nonnegative `u`. On D<F, `f=1+v` with `v≥0`; on D=F, `f=0` and there is no v variable.

[PROVED-HERE] The total number of ordered set partitions of four labeled objects is the fourth ordered Bell/Fubini number:

`F_4 = 1·S(4,1) + 2!·S(4,2) + 3!·S(4,3) + 4!·S(4,4)`

`= 1 + 14 + 36 + 24 = 75`.

If x=y, contract x and y to one labeled super-object. The remaining ordered partitions are those of three labeled objects, hence

`F_3 = 1·S(3,1) + 2!·S(3,2) + 3!·S(3,3)`

`= 1 + 6 + 6 = 13`.

Swapping x and y is a bijection between x>y and x<y. Therefore the remaining 75−13=62 partitions split equally:

`x=y: 13`, `x>y: 31`, `x<y: 31`.

Consequently

`x≥y: 13+31=44`, and symmetrically `x≤y: 13+31=44`.

[COMPUTED] The session enumeration generated 75 total patterns and 31 patterns in the x>y set. Its output printed `x_eq_y: 44`, but the generator branch was effectively

`if position(x)>position(y): add to gt; else: add to eq`.

Thus its `eq` set is exactly x≤y, containing both x=y and x<y. The value 44 is numerically correct for the combined half-order but incorrectly labeled as equality. This is the first exact defect found.

[PROVED-HERE] The erroneous set was not used downstream to define either atlas. The strict pattern set was tested as `spats == gt`, and the boundary pattern set as `bpats == gt`; both are exactly the 31 x>y patterns. No equality pattern and no x<y pattern was inserted into either certificate atlas. Therefore the 44 label cannot affect chamber exhaustiveness, disjointness, or any signed certificate.

## 3. Exact fiber and signed quantities

[PROVED-HERE] The corrected V fiber contract is

`Γ_V={(i,j,k) in I_p×I_q×I_r : i≤j and i≤k}`,

with weight

`W_V(i,j,k)=1+[j=k]`.

Thus, with X_{j<k}, X_{k<j}, and Y the unweighted strict and tied slices,

`N_V=X_{j<k}+X_{k<j}+2Y`,

`O_{q<r,V}=X_{j<k}+Y`,

`O_{r<q,V}=X_{k<j}+Y`.

The pin statistics are literal strict tails:

`H_V = mass(i>A)`,

`L_V = mass(j<D)`.

[PROVED-HERE] The corrected Q fiber has the one-unit full-diagonal difference. At a full tie, V has weight 2 and Q has weight 3. Away from the full tie the weights agree. The corrected transfer is

`N_Q=N_V+1`, `H_Q=H_V+1`, `L_Q=L_V`.

The exact Q failure condition is

`N_Q>3H_Q` and `N_Q>3L_Q`.

Substitution and integrality give

`N_V-3H_V≥3` and `N_V-3L_V≥0`.

The aligned signed target is

`P_b=N_Q−3 max(H_Q,L_Q)`,

so the certificate sign is

`−P_b=3 max(H_Q,L_Q)−N_Q`.

In particular, on an H-active cell the sign is `3H_Q−N_Q`, not `N_Q−3H_Q`.

## 4. Q3-L and Q4-R chamber/boundary trace

[ARGUED] The banked Q3-L transfer is gap reversal followed by `(p',q',r')=(y,x,z)`. The extra Q unit is on original x<z and maps to transformed r'<q'. The banked Q4-R transfer is direct `(p,q,r)=(x,y,z)`. Its extra unit is on original z<y and maps to transformed r<q.

[ARGUED] Every Q3-L and Q4-R overlap instance maps into the same canonical normalized V domain described above. Canonical sibling exchange gives exactly one of D<F or D=F. Thus each branch has 31 strict weak-order cells when D<F and 31 boundary cells when D=F. The x=y and x<y portions of the full 75-pattern universe are not missing cells: x=y is outside the strict x>y non-singleton domain, while x<y is the exchanged noncanonical orientation.

[COMPUTED] The repaired direct atlas replay parsed the strict coefficient data with hash

`59e2b841ce2cb653d900a73092165f1b78547f4bf6023c4b04adf677a878174d`,

and the D=F coefficient data with hash

`7aad8e7378dfe5475ba1dc3b8283e8250adf64dafe3359a0a0460b23c6288a5a`.

It reconstructed every endpoint from its chamber blocks and checked the finite normalized envelope. The exact output was:

`STRICT_ATLAS patterns=31, certificates=62, identity_numeric_points=32768, residual_terms=1147, negative_residual_coefficients=0, coverage_rows=7776, coverage_pattern_min=84, coverage_pattern_max=378`.

`BOUNDARY_ATLAS patterns=31, identities=31, identity_numeric_points=4096, residual_terms=391, negative_residual_coefficients=0, coverage_rows=2304, coverage_pattern_min=28, coverage_pattern_max=126, constant_min=1`.

[PROVED-HERE] The general chamber parameterization is a bijection: sort x,y,c,e, group equal values into one block, and recover u and each nonnegative gap z_i. Therefore the finite coverage check is a load-bearing sanity check, while the block/slack construction proves universal disjointness and exhaustiveness of the 31-cell strict and 31-cell boundary atlases.

[COMPUTED] The independent D=F replay separately reported:

`FAILURE_COUNT 0`, `PATTERN_COUNT 31`, `IDENTITY_EXPANSIONS 31`, `IDENTITY_RESIDUAL_TERMS 391`, `NEGATIVE_RESIDUAL_COEFFICIENTS 0`, `COVERAGE_ROWS 2304`, `COVERAGE_OVERLAPS 0`, `COVERAGE_UNCOVERED 0`, `COVERAGE_EXTRANEOUS 0`, `BOUNDARY_MIN_RESIDUAL 1`, `FACE_FAILURES 0`, `DIRECT_MODEL_MISMATCHES 0`, `SLICE_MISMATCHES 0`, `ALL_CHECKS_PASS True`.

[ARGUED] The separate D-branch ledgers remain covered by `q3-q4-separate-d-branch-pin` and the r29 genuine-chain-pair records. The 44 label is not used in those ledgers, so D-branch or boundary coverage is unchanged.

## 5. Signed certificate audit and strict-floor mechanism

[PROVED-HERE] Each strict cell contains an H and an L certificate. The exact checked identities have the form

`3H−N = α(N−3L)+β(N−3H)+R_H`,

`3L−N = α(N−3L)+β(N−3H)+R_L`,

where α, β are nonnegative rational numbers and every coefficient of the residual polynomial is nonnegative in the nonnegative chamber variables. The replay checked all 62 coefficient identities and found zero negative residual coefficients. The independent Full-Cone replay additionally recorded 49,152 exact identity-component checks and 32,768 strict-certificate numerical points.

[PROVED-HERE] On D=F, the separate 31-cell atlas checks `3L−N=R_L` coefficientwise. It has 391 nonzero residual terms, no negative coefficients, and constant coefficient minimum 1. Hence the boundary has the stronger universal floor `3L_V−N_V≥1`.

[PROVED-HERE] Let `S_H^V=3H_V−N_V` and `S_L^V=3L_V−N_V`.

If `H_V≥L_V`, the strict H certificate or the certified Full-Cone theorem gives `S_H^V≥0`. Since `H_Q=H_V+1` and `N_Q=N_V+1`,

`3H_Q−N_Q = S_H^V+2 ≥ 2`.

If `L_V>H_V+1`, then Q is L-active and

`3L_Q−N_Q = S_L^V−1`.

The Full-Cone theorem gives `S_L^V≥0`; the strict certificate identity upgrades this to `S_L^V≥1`. Indeed, equality `S_L^V=0` would imply `N_V=3L_V` and `N_V−3H_V=3(L_V−H_V)>0`. In the identity for `S_L^V`, the α term vanishes, while the β term is positive whenever β>0; if the residual has a positive constant, the residual is also positive. The only zero-constant strict residual exceptions were explicitly found as

`ye|c|x` with β=1/11,
`ye|xc` with β=2,
`ye|x|c` with β=2.

In those exceptional cells β>0, so equality is still impossible in the L-active regime. Since `S_L^V` is integral, `S_L^V≥1`, and therefore `3L_Q−N_Q≥0`.

[PROVED-HERE] The equality case `L_V=H_V+1` is covered separately and is load-bearing. Here `H_Q=L_Q=L_V`; the strict floor gives `N_V≤3L_V−1`, so

`N_Q=N_V+1≤3L_V=3H_Q=3L_Q`.

Thus the one-unit Q correction cannot create a failure on the equality face.

[COMPUTED] The repaired replay found exact equality-face examples, including strict pattern `c|y|e|x`, parameters `(1,0,0,0,0)`, with

`(N_V,H_V,L_V)=(60,39,40)` and `L_V=H_V+1`,

and `3L_V−N_V=60`. It also found the finite strict-envelope minimum `3L_V−N_V=1` whenever `L_V>H_V`; this finite minimum is diagnostic only, while the coefficient identity plus integrality is the universal argument.

[PROVED-HERE] Invalid H-active use is explicitly excluded. The replay found the witness

pattern `y|xce`, parameters `(0,0,0)`, `(N_V,H_V,L_V)=(11,3,4)`,

so `L_V>H_V` but `S_H^V=3·3−11=−2`. Therefore S_H^V is never used in the L-active regime; the proof dispatches to the L residual and strict floor instead.

## 6. Aligned sign and Q-transfer replay

[PROVED-HERE] On the aligned family, put `n=D−A+1≥2` and `m=F−D+1≥2`. Direct V enumeration gives

`N_V=m n(n+1)/2+n`,

`H_V=m n(n−1)/2+n−1`,

`L_V=m n(n−1)/2`.

After the corrected full-diagonal unit,

`N_Q=m n(n+1)/2+n+1`,

`H_Q=m n(n−1)/2+n`,

`L_Q=m n(n−1)/2`.

Therefore

`3H_Q−N_Q = m n(n−2)+2n−1≥3`.

At `(A,B,C0,D,E,F)=(0,1,0,1,1,2)`, the exact values are

`(N_V,H_V,L_V)=(8,3,2)`,

`(N_Q,H_Q,L_Q)=(9,4,2)`,

and `(3H_Q−N_Q,3L_Q−N_Q)=(3,−3)`. The aligned signed certificate is therefore `−P_b=3H_Q−N_Q=3`.

[COMPUTED] The repaired literal Q replay reported:

`literal_M=12`, `literal_rows_per_branch=286`, `literal_transfer_errors=0`, `literal_orientation_errors=0`, `literal_state_mass_sum_both=35750`,

and formula replay through M=32 reported `formula_rows_per_branch=5456`, `formula_errors=0`, `min_corrected_slack_M=−3`, `near_miss_count_M=66`.

The independent banked Q3/Q4 replay separately checked all 5,456 aligned records per branch, with `LITERAL_REPLAY_ERRORS 0`, `target_failures 0`, and `all_checks_true True` for both Q3-L and Q4-R. At the smallest aligned point it recorded Q3-L orientations `(O_xz,O_zx,O_yz,O_zy)=(3,6,1,8)` and Q4-R orientations `(8,1,6,3)`, exactly placing the additional unit on the stated branch-specific orientation.

## 7. Exact replay repairs and disposition

[COMPUTED] The prior checker stalled before certificate work because strict records stored `blocks` and `offset` under `parameterization`. The in-session repair supplied the nested accessors. Two further checker-level defects were corrected before accepting PASS: the numeric loop had compared a residual polynomial R alone with the left side instead of evaluating the current certificate identity, and residual polynomials with rational coefficients were incorrectly required to evaluate individually to integers. The repaired checker evaluated the full current-certificate right side exactly with Fractions and checked residual nonnegativity rationally. These were replay-harness defects, not failures of the certificate data.

[COMPUTED] The repaired run also checked the integer equivalence over all `21^3=9261` triples and returned `MISMATCHES 0`.

[PROVED-HERE] There is no first exact uncovered or invalid mathematical state. The only exact correction is the interpretation of the 44 count: it is x≤y, not x=y. Because the atlas selection, transfer maps, strict/boundary split, and signed identities use the 31 x>y set, the correction is non-load-bearing for theorem validity.

## 8. Banking status

[FAILED] A new wiki write under the supplied title `q_2e_34_reconciled_certificate_independent_replay` could not be executed because the live tool allotment was exhausted immediately after dependency hydration. The complete mathematical report is emitted here, and the load-bearing replay JSON was already persisted at `outputs/artifacts/reconciled_q_2e_34_signed_full_diagonal_certificate_20260818/replay_results.json`; however, durable banking under the exact supplied title is unconfirmed and must be completed by the operator.

## Final audit disposition

[PROVED-HERE] **CONFIRMED/PASS.** The corrected partition is exactly `75=13+31+31`; the 44 statement is only a misnamed x≤y count. Every Q3-L and Q4-R overlap image is covered by the 31-cell D<F atlas or the separate 31-cell D=F atlas, with the canonical split disjoint and exhaustive. Every H and L signed certificate remains valid, the corrected Q sign is `−P_b=3 max(H_Q,L_Q)−N_Q`, the L-active −1 residual is discharged by the strict floor, `L_V=H_V+1` is covered, invalid H-active use is excluded, and no boundary or chamber gap was found.

## Provenance

- kg_import | imported from wiki entry corrected-ordered-partition-audit-and-final-verdict-for-q-2e



---

## Banked record: `independent-q-2e-34-certificate-replay`

# independent-q-2e-34-certificate-replay

title: Independent Q-2E-34 Certificate Replay
type: computation | label: computed | verification: unverified
namespace: third23
mechanism: A corrected schema-aware checker independently executed every strict and boundary certificate and audited exhaustive chamber coverage.
[graph-node: kgn_416a6f32109c — this page is a PROJECTION; truth lives in the research KG]

## Statement

The repaired independent Q replay checked 31 strict chambers, 62 strict signed certificates, 31 D=F boundary identities, 7,776 strict coverage rows, and 2,304 boundary coverage rows. It found no uncovered, overlapping, or extraneous boundary state, no negative residual coefficient, and no failed identity. The load-bearing replay JSON has SHA-256 58c6d5909596794f2561882c625afb3193d077b92f9918dc0fce656a0cbd1e8.

## Content

The repaired independent Q replay checked 31 strict chambers, 62 strict signed certificates, 31 D=F boundary identities, 7,776 strict coverage rows, and 2,304 boundary coverage rows. It found no uncovered, overlapping, or extraneous boundary state, no negative residual coefficient, and no failed identity. The load-bearing replay JSON has SHA-256 58c6d5909596794f2561882c625afb3193d077b92f9918dc0fce656a0cbd1e8.

## Provenance

- supervisor | work_8d7166a8feca | banked per finding at effort end



---

## Banked record: `ordered-weak-partition-count-correction`

# ordered-weak-partition-count-correction

title: Ordered Weak-Partition Count Correction
type: computation | label: computed | verification: unverified
namespace: third23
mechanism: Direct ordered-partition enumeration, contraction of x=y to the 13 weak orders on three labels, and symmetry exchanging x and y.
[graph-node: kgn_e669449ad4aa — this page is a PROJECTION; truth lives in the research KG]

## Statement

The ordered weak partitions of four labeled quantities number 75: exactly 13 satisfy x=y, 31 satisfy x>y, and 31 satisfy x<y. Consequently, 44 counts the weak orientation x≥y or x≤y, not equality. The earlier field labeled x_eq_y:44 was a generator-label defect whose else branch actually collected x≤y; it was non-load-bearing because the strict and boundary certificate atlases use precisely the 31 canonical x>y patterns.

## Content

The ordered weak partitions of four labeled quantities number 75: exactly 13 satisfy x=y, 31 satisfy x>y, and 31 satisfy x<y. Consequently, 44 counts the weak orientation x≥y or x≤y, not equality. The earlier field labeled x_eq_y:44 was a generator-label defect whose else branch actually collected x≤y; it was non-load-bearing because the strict and boundary certificate atlases use precisely the 31 canonical x>y patterns.

## Provenance

- supervisor | work_8d7166a8feca | banked per finding at effort end




# Theorem 13.1 (The audited final assembly)

---

## Banked record: `three-defect-chain-theorem-audited-final-assembly`

# Three-Defect Chain Theorem — audited final assembly

status: proved
scope: Every finite ordinal-sum-indecomposable non-chain poset P with a maximum chain C and |P\C|<=3 has an incomparable pair {u,v} with 1/3 <= Pr(u<v) <= 2/3.
depends on: the exact-slug structural and shape-by-heavy-pattern ledger recorded below, including the independently replayed Full-Cone TE(2=1), Lambda reflection transfer, and corrected Q-2E-34 replay.

# Three-Defect Chain Theorem — audited final assembly

## Theorem and contradiction setup
Let P be a finite ordinal-sum-indecomposable non-chain poset, C a maximum chain, and |P\C|<=3. Then some incomparable pair {u,v} satisfies 1/3 <= Pr(u<v) <= 2/3. Assume conversely that every incomparable-pair orientation avoids the closed middle third. By `closed-third-strong-order-rigidity` and `corrected-strong-order-theorem-under-closed-third-avoidance`, the >2/3 orientation is a strict total order extending P. By `heavy-gap-alignment-corollary-under-closed-third-avoidance` and `heavy-gap-probabilistic-alignment`, every defect has a unique heavy gap and both strict tails have mass <N/3, where N=e(P). The exact legal-gap and fiber interface is supplied by `v-lambda-uniform-three-defect-foundation-audit-round-28-corr`; maximum-chain windows are nonsingleton by `maximum-chain-defect-windows-are-nonsingleton` and `maximum-chain-non-singleton-defect-windows`.

## Exhaustive structural reduction
The case |P\C|=0 contradicts that P is a non-chain. The cases |P\C|=1,2 are closed by `two-defect-chain-theorem`, `two-defect-chain-balance-theorem`, `k-2-uniform-to-doubled-diagonal-bridge-and-two-defect-chain`, and `round-28-audit-two-defect-and-three-chain-assembly-entries`. If |P\C|=3 and the three defects form a chain, `three-chain-defect-width-two-reduction` and `strict-reduction-atlas-for-three-chain-defects` reduce to width two, and `sah-theorem-certified-source-verbatim-the-literal-text-the-d` supplies a balanced pair; ordinal-sum indecomposability excludes its direct-sum exception. Otherwise the defect order is, up to duality, antichain A, V, Lambda, or one-relation Q. The three heavy indices are exhaustively all-distinct, exactly-two-equal, or all-equal, as recorded by `round-29-two-equal-cell-partition`.

## Exhaustive cell closures
A-D is closed by `antichain-defect-distinct-heavy-index-exclusion`, `corrected-antichain-distinct-heavy-index-exclusion-derivatio`, and `antichain-distinct-heavy-verification-debt-resolution`. A-2E is excluded by the same Helly conclusion, which forces all three heavy gaps equal. A-CH is closed by `centered-three-interval-ch-chamber-specific-global-decision`, `deepcheck-repaired-ch-global-residuals-next`, `exceptional-weak-chamber-ch-certificate`, and `antichain-common-heavy-closure-recovered-full-artifact`.

V-D is closed by `conditional-v-distinct-heavy-exclusion` in its unconditional r28-audited scope. V-CH is vacuous because a common heavy gap forces a singleton defect window, contradicting maximum-chain status. In V-2E, four cells are closed by `round-29-two-equal-cell-partition`; the tied-siblings fifth cell is closed by `full-cone-te-2-1-theorem-closing-v-2e-tied-siblings`, with independent replay `independent-full-cone-te-2-1-certificate-replay`. That replay passed 49,152 identity checks and an exhaustive disjoint cone partition.

L-D is closed by `conditional-lambda-distinct-heavy-exclusion` under the r28-audited duality interface; L-CH is the exact reflection dual of V-CH. L-2E is closed by gap reflection x->m-x: it bijects Lambda states {(i,j,k):j<=i,k<=i} with V states, preserves weight 1+1[j=k] and N, exchanges strict tails, and complements each same-label numerator S to N-S while preserving cuts, endpoints, diagonal fibers, and threshold equalities. It carries the Lambda tied-siblings survivor on both D<F and D=F to the Full-Cone TE(2=1) theorem. The independent regression checked 35,832 state/fiber cases through m=6 without failure.

Q-D is closed by `pairwise-distinct-heavy-q-exclusion`, `q-distinct-heavy-chamber-certificate-independent-decision-ro`, and `q-common-heavy-exclusion-is-presentation-general`. Q-CH is closed by `common-heavy-q-exclusion`, `q-common-heavy-closure-decision-round-23-repaired`, and `q-common-heavy-exclusion-is-presentation-general`. Q-2E cells Q1 and Q2 are closed by the round-30 structural reduction recorded in the validated ledger. Q3 and Q4 are closed by `corrected-ordered-partition-audit-and-final-verdict-for-q-2e`. The exact transfer is N_Q=N_V+1, H_Q=H_V+1, L_Q=L_V; simultaneous corrected-Q failure is equivalent by integrality to N_V-3H_V>=3 and N_V-3L_V>=0, and the aligned sign is -P_b=3H_Q-N_Q. The repaired independent replay passed 31 strict chambers, 62 strict certificates, 31 D=F boundary identities, 7,776 strict rows, and 2,304 boundary rows. Ordered weak partitions are 75=13+31+31; 44 denotes a weak orientation, not equality. Replay SHA-256: `58c6d5909596794f2561882c625afb3193d077b92f9918dc0fce656a0cbd1e8`.

## Validated ledger
Structural rows: S1 CLOSED-2D by the four two-defect slugs above; S2 CLOSED-2D by the two three-chain reduction slugs; S3 CLOSED-OP by the Sah source-verbatim slug; S4 CLOSED-2D by the two maximum-chain-window slugs; S5 CLOSED-2D by the two strong-order slugs; S6 CLOSED-2D by the two heavy-gap slugs; S7 CLOSED-LOGICAL by `round-29-two-equal-cell-partition`; S8 CLOSED-2D by `canonical-ordinal-sum-factorization-theorem-for-finite-poset`. Shape rows A-D, A-2E, A-CH, V-D, V-2E, V-CH, L-D, L-2E, L-CH, Q-D, Q-2E, Q-CH are closed exactly as listed above. Thus all 20 ledger rows are closed.

## Acyclic dependency tree
The theorem node consumes: (i) ordinal-sum and defect-count reductions; (ii) the common strong-order/heavy-gap/gap-fiber interface; (iii) the exhaustive shape and heavy-pattern partition; and (iv) the twelve cell closures. The cell closures consume only earlier structural lemmas, exact certificate theorems, and independent replay records. No cell closure consumes this theorem or this assembly. The dependency tree is therefore acyclic and noncircular. Historic uncorrected pending walks and mislabeled partition counts are superseded and are not load-bearing.

## Conclusion
Under the assumption that no incomparable pair is balanced, P must occupy one of the exhaustive closed ledger cells, but every such cell contradicts closed-third avoidance. Hence an incomparable pair {u,v} with 1/3 <= Pr(u<v) <= 2/3 exists. This proves the Three-Defect Chain Theorem.

---
provenance: actor=work_math_manager_streaming work_id=work_8d7166a8feca node_id=three_defect_chain_claim_audited_final_assembly banked=2026-08-18T12:18:47Z


---

## Banked record: `three-defect-chain-theorem`

# three-defect-chain-theorem

title: Three-Defect Chain Theorem
type: claim | label: proved | verification: unverified
namespace: third23
mechanism: A noncircular dependency walk closes all eight structural rows and all twelve shape-by-heavy-pattern rows of the validated ledger, using the independently replayed Lambda L-2E transfer and corrected Q-2E-34 certificate for the final two cells. The complete audited assembly was durably banked with receipt b11569bf81fe4370b5c2b851ced3505b.
[graph-node: kgn_493a26b3096d — this page is a PROJECTION; truth lives in the research KG]

## Statement

Every finite ordinal-sum-indecomposable non-chain poset P with a maximum chain C and |P\C|≤3 has an incomparable pair {u,v} such that 1/3≤Pr(u<v)≤2/3, where the probability is taken uniformly over the linear extensions of P.

## Content

Every finite ordinal-sum-indecomposable non-chain poset P with a maximum chain C and |P\C|≤3 has an incomparable pair {u,v} such that 1/3≤Pr(u<v)≤2/3, where the probability is taken uniformly over the linear extensions of P.

## Provenance

- supervisor | work_8d7166a8feca | banked per finding at effort end
- work_math_manager_streaming | work_8d7166a8feca | three_defect_chain_claim_audited_final_assembly | imported from wiki entry three-defect-chain-theorem-audited-final-assembly



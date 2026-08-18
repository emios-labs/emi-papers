# ASSEMBLY LEDGER — The Three-Defect Chain Theorem
# THE TYPED SUBSTRATE FOR THEOREM STATE (autopsy fix 1, 2026-08-17). Rows are data:
# every CLOSED row cites the slug(s) that close it; validate_ledger.py checks every slug
# exists and fails loudly otherwise. Councils and assembly rounds read THIS, never
# narrative. Statuses: CLOSED-2D (>=2 independent derivations) | CLOSED-1D (single) |
# CLOSED-OP (operator source certification) | CLOSED-LOGICAL (partition triviality) |
# PARTIAL (artifact banked, uncertified) | OPEN (attacked, routes refuted) |
# OPEN-AUDIT (no supporting entry located — discovered hole).
# Target: every finite ordinal-sum-indecomposable non-chain poset P with maximum chain C
# and |P\C| <= 3 has an incomparable pair {u,v} with 1/3 <= Pr(u<v) <= 2/3.

## STRUCTURAL CELLS
| id | cell | status | slugs |
|----|------|--------|-------|
| S1 | \|P\C\|<=2 entry (incl. \|P\C\|=1 reduction) | CLOSED-2D | two-defect-chain-theorem; two-defect-chain-balance-theorem; k-2-uniform-to-doubled-diagonal-bridge-and-two-defect-chain; round-28-audit-two-defect-and-three-chain-assembly-entries |
| S2 | three-chain defect order -> width 2 | CLOSED-2D | three-chain-defect-width-two-reduction; strict-reduction-atlas-for-three-chain-defects |
| S3 | width-2 -> balanced pair (Sah bridge, direct-sum exception) | CLOSED-OP | sah-theorem-certified-source-verbatim-the-literal-text-the-d |
| S4 | maximum-chain windows nonsingleton | CLOSED-2D | maximum-chain-defect-windows-are-nonsingleton; maximum-chain-non-singleton-defect-windows |
| S5 | strict strong-order rigidity | CLOSED-2D | closed-third-strong-order-rigidity; corrected-strong-order-theorem-under-closed-third-avoidance |
| S6 | heavy-gap rigidity (unique heavy gap, sub-1/3 tails) | CLOSED-2D | heavy-gap-alignment-corollary-under-closed-third-avoidance; heavy-gap-probabilistic-alignment |
| S7 | heavy-index patterns exhaust {all-distinct, exactly-two-equal, all-equal} | CLOSED-LOGICAL | round-29-two-equal-cell-partition (two-equal substructure; tri-partition is a logical triviality of three values) |
| S8 | ordinal-sum reduction to indecomposable | CLOSED-2D | canonical-ordinal-sum-factorization-theorem-for-finite-poset |

## SHAPE x HEAVY-PATTERN CELLS (|P\C| = 3)
| id | shape | pattern | status | slugs / notes |
|----|-------|---------|--------|---------------|
| A-D | antichain | all-distinct | CLOSED-2D | antichain-defect-distinct-heavy-index-exclusion; corrected-antichain-distinct-heavy-index-exclusion-derivatio; antichain-distinct-heavy-verification-debt-resolution |
| A-2E | antichain | two-equal | CLOSED-2D | same slugs as A-D: the Helly argument concludes ALL heavy gaps equal, excluding two-equal outright (quantifier audited, r28/r29) |
| A-CH | antichain | all-equal | CLOSED-2D | centered-three-interval-ch-chamber-specific-global-decision; deepcheck-repaired-ch-global-residuals-next; exceptional-weak-chamber-ch-certificate; antichain-common-heavy-closure-recovered-full-artifact (common-cut scope linkage audited r28) |
| V-D | V | all-distinct | CLOSED-1D | conditional-v-distinct-heavy-exclusion (unconditional form certified in r28 audit) |
| V-2E | V | two-equal (5 cells) | CLOSED-2D | 4 of 5 via round-29-two-equal-cell-partition; tied-siblings: full-cone-te-2-1-theorem-closing-v-2e-tied-siblings; independent-full-cone-te-2-1-certificate-replay (two-case theorem over gated-te21-chamber-atlas-and-exact-certificates + exact-d-f-facet-certificate-atlas-for-guarded-te-2-1 + normalized-d-f-0-te-2-1-facet-certificate-atlas; fresh independent replay VERDICT PASS, r37) |
| V-CH | V | all-equal | CLOSED-1D | PROVED VACUOUS r35: common heavy gap forces I_q singleton, contradicting the maximum-chain guard — independent of avoidance and the contested r17 lemma (see supervisor verdict r35) |
| L-D | Lambda | all-distinct | CLOSED-1D | conditional-lambda-distinct-heavy-exclusion (duality; unconditional form r28) |
| L-2E | Lambda | two-equal | CLOSED-2D | lambda-l-2e-exact-reflection-transfer; lambda-l-2e-exact-reflection-transfer-from-full-cone-te-2-1; independent-lambda-reflection-replay (reflection x↦m−x bijects states, preserves W and N, exchanges tails; replay: 173,613 triples, 6.36M tail identities, all 49,152 full-cone identities PASS, r38) |
| L-CH | Lambda | all-equal | CLOSED-1D | vacuous by the exact reflection duality (weight preserving) from V-CH (r35) |
| Q-D | Q | all-distinct | CLOSED-1D | pairwise-distinct-heavy-q-exclusion; q-distinct-heavy-chamber-certificate-independent-decision-ro; q-heavy-branch generality per q-common-heavy-exclusion-is-presentation-general (audit r28) |
| Q-2E-12 | Q | two-equal cells Q1,Q2 | CLOSED-1D | round-30 structural exclusion (see supervisor verdict r30); prior artifacts r29-q-two-equal-closure-certificate-round-29 subsumed |
| Q-2E-34 | Q | two-equal cells Q3,Q4 | CLOSED-2D | corrected-q3-l-q4-r-full-diagonal-transfer; aligned-corrected-q3-l-q4-r-formulas; q-2e-34-full-diagonal-certificates-and-closure-decision; independent-q-2e-34-certificate-replay; independent-replay-of-reconciled-q-2e-34-signed-full-diagona; corrected-ordered-partition-audit-and-final-verdict-for-q-2e; ordered-weak-partition-count-correction (N_Q=N_V+1, H_Q=H_V+1, L_Q=L_V; the +1 margin consumed from the certificate atlases, not the max inequality: D<F 31-chamber signed H-certificates + D=F boundary floor 3L_V−N_V≥1; replay: 31+62 strict, 31 boundary, 7,776+2,304 coverage rows PASS, r38) |
| Q-CH | Q | all-equal | CLOSED-1D | common-heavy-q-exclusion; q-common-heavy-closure-decision-round-23-repaired; q-common-heavy-exclusion-is-presentation-general |

## THE THEOREM (banked 2026-08-18, round 38)
| id | statement | status | slugs |
|----|-----------|--------|-------|
| T | Three-Defect Chain Theorem: every finite ordinal-sum-indecomposable non-chain poset P with maximum chain C, \|P\C\|<=3, has an incomparable pair with 1/3 <= Pr(u<v) <= 2/3 | CLOSED-1D | three-defect-chain-theorem; three-defect-chain-theorem-audited-final-assembly (noncircular slug-cited dependency walk over every row above; supervisor verdict r38: goal achieved) |

## OPEN-CELL SUMMARY
ALL CELLS CLOSED — the theorem is assembled and banked (r38, 2026-08-18).
Residual referee-grade debt (does not gate the theorem):
1. Single-derivation upgrades owed: V-D, L-D, Q-D, Q-CH, S3, V-CH/L-CH (vacuity), T (the walk itself ran once).
2. The r38 count-label erratum is recorded (ordered-weak-partition-count-correction): 75=13+31+31; the old x_eq_y:44 field counted x<=y; non-load-bearing (atlases use the 31 strict patterns).

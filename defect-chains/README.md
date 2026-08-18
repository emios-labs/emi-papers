# The Two- and Three-Defect Chain Theorems — paper and proof objects

This directory is the complete, self-verifying artifact package for:

- **`paper/`** — *The 1/3–2/3 Conjecture on the Defect Ladder: The Two- and
  Three-Defect Chain Theorems* (TeX + PDF). Main result: every finite non-chain poset
  that becomes a chain after deleting at most **three** elements has an incomparable
  pair {u,v} with 1/3 ≤ Pr(u≺v) ≤ 2/3.
- **`paper-two-defect/`** — the companion defect-two paper (TeX + PDF): the Two-Defect
  Chain Theorem and the equality-rigidity classification.
- **`SUPPLEMENT.md`** — the complete derivations behind every theorem the main paper
  states at citation level, reproduced verbatim from the research record.
- **`ASSEMBLY_LEDGER.md`** — the validated cell-by-cell dependency ledger of the
  three-defect assembly (every row cites its proof records).
- **`outputs/`** — the exact certificate corpora, generators, and independent
  checkers, in their original layout.
- **`SHA256SUMS`** — SHA-256 of every file in this directory. The hashes quoted in
  the paper (Section on proof objects) are of these exact files.

## Which artifact proves which theorem

| Paper item | Proof object(s) |
|---|---|
| Thm 10.2 (Centered CH inequality, 169 chambers) | `outputs/direct_CH_decision_20260817_PROVED.md` (complete certificate table + exceptional-chamber identity + exact coefficient audit) |
| Thm 11.4 (Full-Cone TE(2=1)), strict facet D<F | `outputs/artifacts/gated_te21_chamber_atlas_20260817/atlas.md`, data `outputs/data/gated_te21_chamber_atlas_20260817.json`, generator/replay `outputs/code/gated_te21_chamber_atlas_20260817.py` |
| Thm 11.4, boundary facet D=F | `outputs/artifacts/te21_D_eq_F_facet_atlas_20260818/` (atlas, replay report, equality-face report), data `outputs/data/te21_D_eq_F_facet_atlas_20260818.json` + `..._equality_faces_...json`, code `outputs/code/{preflight,generate,replay,equality_face_audit}_te21_D_eq_F_*.py`, independent verification `outputs/artifacts/independent_te21_D_eq_F_facet_verification_20260818/` |
| Thm 11.4, full-cone partition replay | `outputs/data/independent_repaired_full_cone_te21_replay_20260818.json` |
| Thm 11.5 (Λ reflection transfer) | `outputs/code/lambda_v_reflection_transfer_audit_20260818.py`, `outputs/code/lambda_l2e_independent_replay_20260818.py`, log `outputs/lambda-l2e-independent-replay-20260818.txt` |
| Thms 12.5–12.6 (corrected Q3/Q4) | `outputs/artifacts/reconciled_q_2e_34_signed_full_diagonal_certificate_20260818/replay_results.json`, checker `outputs/code/reconciled_q_2e_34_independent_replay_20260818.py` |
| Statement-level theorems (8.x, 9.x, 10.1, 11.1–11.3, 12.1–12.4, 13.1) | `SUPPLEMENT.md` (verbatim derivations) + `ASSEMBLY_LEDGER.md` |

## How to verify

Everything runs on stock Python 3 (standard library only; exact rational arithmetic via
`fractions`). From this directory:

```
python outputs/code/replay_te21_D_eq_F_facet_atlas_20260818.py
```

should end with:

```
KNOWN_POSET {'acyclic': True, 'q_parallel_r': True, 'height': 2, 'incomparability_connected': True, 'linear_extensions': 18, 'ledger': (18, 6, 11)}
ALL_CHECKS_PASS True
```

The other checkers run the same way (`outputs/code/*.py`); the atlas generators
regenerate the certificate data from the raw definitions so it can be diffed against
the shipped JSON. Integrity: `sha256sum -c SHA256SUMS`.

The checkers re-derive the certificate identities from raw definitions in exact
arithmetic — they are independent consumers, not re-runs of the generators. The
theorems rest on the exact symbolic identities in the certificate tables, which can
also be re-expanded with any computer algebra system.

#!/usr/bin/env python3
"""Independent equality-face and near-miss audit for the f=0 facet.

No interpolation is used.  The script parses the exact rational coefficient
lists, expands 3L-N, enumerates every {0,1} assignment of the chamber
parameters (all zero-gap/zero-offset faces and their intersections), and scans
the finite normalized envelope used by the main replay.  It writes a compact
ledger of coefficient zeros, boundary residuals, and equality events.
"""
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import json

DATA = Path('outputs/data/te21_D_eq_F_facet_atlas_20260818.json')
OUT = Path('outputs/artifacts/te21_D_eq_F_facet_atlas_20260818/equality_face_report.txt')
OUT_JSON = Path('outputs/data/te21_D_eq_F_facet_equality_faces_20260818.json')
PATTERNS = [
    'y|xce','yc|xe','yce|x','ye|xc','c|y|xe','c|ye|x','ce|y|x',
    'e|y|xc','e|yc|x','y|c|xe','y|ce|x','y|e|xc','y|x|ce',
    'y|xc|e','y|xe|c','yc|e|x','yc|x|e','ye|c|x','ye|x|c',
    'c|e|y|x','c|y|e|x','c|y|x|e','e|c|y|x','e|y|c|x',
    'e|y|x|c','y|c|e|x','y|c|x|e','y|e|c|x','y|e|x|c',
    'y|x|c|e','y|x|e|c'
]
ORDER = ['x', 'y', 'c', 'e']


def frac(s):
    return Fraction(str(s))


def parse_monomial(mon, names):
    exps = [0] * len(names)
    if mon == '1':
        return tuple(exps)
    for factor in mon.split('*'):
        if '^' in factor:
            name, power = factor.split('^')
            power = int(power)
        else:
            name, power = factor, 1
        exps[names.index(name)] += power
    return tuple(exps)


def coeff_map(rows, names):
    return {parse_monomial(r['monomial'], names): frac(r['coefficient'])
            for r in rows}


def add_scaled(*terms):
    out = {}
    for scale, poly in terms:
        for a, c in poly.items():
            out[a] = out.get(a, Fraction(0)) + scale*c
    return {a: c for a, c in out.items() if c}


def chamber_endpoint(rec, vals):
    bs = rec['blocks']
    offset = int(rec['offset'])
    shift = int(rec['lowest_level_shift'])
    lev = [offset + shift + vals[0]]
    for i in range(len(bs)-1):
        lev.append(lev[-1] + 1 + vals[i+1])
    d = {ch: lev[i] for i, block in enumerate(bs) for ch in block}
    return (-d['x'], -d['y'], -d['c'], 0, -d['e'], 0)


def direct_ledger(ep):
    A, B, C0, D, E, F = ep
    N = H = L = 0
    for i in range(A, B+1):
        for j in range(C0, D+1):
            for k in range(E, F+1):
                if i <= j and i <= k:
                    w = 1 + int(j == k)
                    N += w
                    H += w * int(i > A)
                    L += w * int(j < D)
    return N, H, L


def classify(x, y, c, e):
    vals = {'x': x, 'y': y, 'c': c, 'e': e}
    return '|'.join(''.join(ch for ch in ORDER if vals[ch] == level)
                    for level in sorted(set(vals.values())))


def parameters_for(rec, x, y, c, e):
    vals = {'x': x, 'y': y, 'c': c, 'e': e}
    levels = sorted(set(vals.values()))
    offset = int(rec['offset']); shift = int(rec['lowest_level_shift'])
    u = levels[0] - offset - shift
    z = [levels[i+1] - levels[i] - 1 for i in range(len(levels)-1)]
    return [u] + z


def main():
    D = json.loads(DATA.read_text(encoding='utf-8'))
    assert D['patterns'] == PATTERNS
    rows = []
    total_slots = total_zero_slots = total_residual_terms = 0
    total_boundary = total_face_incidents = total_boundary_equalities = 0
    boundary_min = None
    coverage = coverage_equalities = coverage_e_one = 0
    coverage_min = None
    coverage_max_deficit = None
    for rec in D['records']:
        names = rec['variables']; d = len(names)
        Np = coeff_map(rec['polynomials']['N_coefficients'], names)
        Hp = coeff_map(rec['polynomials']['H_coefficients'], names)
        Lp = coeff_map(rec['polynomials']['L_coefficients'], names)
        Rp = coeff_map(rec['certificate']['residual_coefficients'], names)
        expanded = add_scaled((3, Lp), (-1, Np))
        assert expanded == Rp
        slots = comb(d + 3, 3)
        all_polys = (Np, Hp, Lp, Rp)
        assert all(all(sum(a) <= 3 for a in p) for p in all_polys)
        neg = sum(c < 0 for p in all_polys for c in p.values())
        assert neg == 0
        zero_slots = slots - len(Rp)
        residual_values = []
        boundary_eq = 0
        for vals in product(range(2), repeat=d):
            N, H, L = direct_ledger(chamber_endpoint(rec, vals))
            r = 3*L - N
            assert r == sum(c * __import__('math').prod(v**a for v,a in zip(vals, exp))
                            for exp,c in Rp.items())
            assert r >= 0
            residual_values.append(r)
            boundary_eq += (r == 0)
        assert residual_values
        total_slots += slots; total_zero_slots += zero_slots
        total_residual_terms += len(Rp)
        total_boundary += 2**d
        total_face_incidents += d * 2**(d-1)
        total_boundary_equalities += boundary_eq
        boundary_min = min(residual_values) if boundary_min is None else min(boundary_min, min(residual_values))
        rows.append({
            'id': rec['id'], 'pattern': rec['pattern'], 'variables': names,
            'polynomial_slots_each_degree_le_3': slots,
            'N_terms': len(Np), 'H_terms': len(Hp), 'L_terms': len(Lp),
            'residual_terms': len(Rp), 'residual_zero_slots': zero_slots,
            'negative_coefficients_all_four_polynomials': neg,
            'boundary_assignments_0_1': 2**d,
            'boundary_zero_coordinate_incidents': d*2**(d-1),
            'boundary_target_equalities_3L_eq_N': boundary_eq,
            'boundary_min_residual_3L_minus_N': min(residual_values),
            'boundary_max_residual_3L_minus_N': max(residual_values),
        })

    records = D['records']
    for x, y, c, e in product(range(9), repeat=4):
        if not (x > y >= 0 and c >= 1 and e >= 1):
            continue
        p = classify(x, y, c, e)
        rec = records[PATTERNS.index(p)]
        vals = parameters_for(rec, x, y, c, e)
        N, H, L = direct_ledger((-x, -y, -c, 0, -e, 0))
        r = 3*L - N
        assert r >= 0
        coverage += 1
        coverage_equalities += (r == 0)
        coverage_min = r if coverage_min is None else min(coverage_min, r)
        coverage_max_deficit = r if coverage_max_deficit is None else max(coverage_max_deficit, r)
        coverage_e_one += (e == 1)
        names = rec['variables']
        Rp = coeff_map(rec['certificate']['residual_coefficients'], names)
        assert r == sum(c0 * __import__('math').prod(v**a for v,a in zip(vals, exp))
                        for exp,c0 in Rp.items())

    assert total_boundary == 328
    assert total_face_incidents == 580
    assert coverage == 2304
    assert coverage_e_one == 288
    result = {
        'pattern_count': len(rows), 'rows': rows,
        'coefficient_slots_degree_le_3_total': total_slots,
        'coefficient_zero_slots_residual_total': total_zero_slots,
        'residual_nonzero_terms_total': total_residual_terms,
        'boundary_assignments_total': total_boundary,
        'boundary_zero_coordinate_incidents_total': total_face_incidents,
        'boundary_target_equalities_total': total_boundary_equalities,
        'boundary_min_residual': boundary_min,
        'coverage_box_rows': coverage,
        'coverage_e_equals_1_rows': coverage_e_one,
        'coverage_target_equalities': coverage_equalities,
        'coverage_min_residual': coverage_min,
        'coverage_max_residual': coverage_max_deficit,
    }
    OUT_JSON.write_text(json.dumps(result, indent=2, sort_keys=True), encoding='utf-8')
    lines = [
        'TE(2=1) D=F facet equality-face and near-miss ledger',
        'ALL ARITHMETIC IS EXACT INTEGER/Fraction; no interpolation is used.',
        f"PATTERN_COUNT {len(rows)}",
        f'COEFFICIENT_SLOTS_DEGREE_LE_3_TOTAL {total_slots}',
        f'COEFFICIENT_ZERO_SLOTS_RESIDUAL_TOTAL {total_zero_slots}',
        f'RESIDUAL_NONZERO_TERMS_TOTAL {total_residual_terms}',
        'NEGATIVE_COEFFICIENTS_ALL_FOUR_POLYNOMIALS 0',
        f'BOUNDARY_0_1_ASSIGNMENTS_TOTAL {total_boundary}',
        f'BOUNDARY_ZERO_COORDINATE_INCIDENTS_TOTAL {total_face_incidents}',
        f'BOUNDARY_TARGET_EQUALITIES_3L_EQ_N {total_boundary_equalities}',
        f'BOUNDARY_MIN_RESIDUAL_3L_MINUS_N {boundary_min}',
        f'FINITE_COVERAGE_BOX_ROWS {coverage}',
        f'E_EQUALS_1_ROWS {coverage_e_one}',
        f'COVERAGE_TARGET_EQUALITIES_3L_EQ_N {coverage_equalities}',
        f'COVERAGE_MIN_RESIDUAL_3L_MINUS_N {coverage_min}',
        f'COVERAGE_MAX_RESIDUAL_3L_MINUS_N {coverage_max_deficit}',
        'ROW_LEDGER id pattern slots residual_terms zero_slots boundary_points boundary_equalities boundary_min',
    ]
    for r in rows:
        lines.append('ROW {id} {pattern} {polynomial_slots_each_degree_le_3} '
                     '{residual_terms} {residual_zero_slots} '
                     '{boundary_assignments_0_1} {boundary_target_equalities_3L_eq_N} '
                     '{boundary_min_residual_3L_minus_N}'.format(**r))
    lines.append('EQUALITY_FACE_AUDIT_PASS True')
    OUT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    for line in lines:
        print(line)


if __name__ == '__main__':
    main()

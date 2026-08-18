#!/usr/bin/env python3
"""Generate the exact D=F (f=0) guarded-V TE(2=1) chamber atlas.

This generator is intentionally separate from the replay consumer.  It obtains
N,H,L by direct finite enumeration, interpolates the degree<=3 chamber
polynomials over an exact rational basis, and then validates the interpolation
on a larger integer box.  The consumer in
replay_te21_D_eq_F_facet_atlas_20260818.py reads the resulting JSON and checks
it without using interpolation.
"""
from itertools import product
from functools import lru_cache
from pathlib import Path
import json
import sympy as sp

PATTERNS = [
    'y|xce','yc|xe','yce|x','ye|xc','c|y|xe','c|ye|x','ce|y|x',
    'e|y|xc','e|yc|x','y|c|xe','y|ce|x','y|e|xc','y|x|ce',
    'y|xc|e','y|xe|c','yc|e|x','yc|x|e','ye|c|x','ye|x|c',
    'c|e|y|x','c|y|e|x','c|y|x|e','e|c|y|x','e|y|c|x',
    'e|y|x|c','y|c|e|x','y|c|x|e','y|e|c|x','y|e|x|c',
    'y|x|c|e','y|x|e|c'
]


def blocks(pat):
    return [list(block) for block in pat.split('|')]


def chamber_info(pat):
    bs = blocks(pat)
    lower = {'x': 0, 'y': 0, 'c': 1, 'e': 0}
    offset = max(lower[ch] for ch in bs[0])
    # If e is on the lowest level and c is not there, e>=1 is an extra
    # facet condition.  Shift the lowest level by one so all variables are
    # genuinely unrestricted nonnegative variables.
    shift = int(offset == 0 and 'e' in bs[0])
    names = ['u'] + [f'z{i}' for i in range(len(bs)-1)]
    return bs, offset, shift, names


def endpoint_from_values(pat, vals):
    bs, offset, shift, names = chamber_info(pat)
    lev = [offset + shift + vals[0]]
    for i in range(len(bs)-1):
        lev.append(lev[-1] + 1 + vals[i+1])
    d = {ch: lev[i] for i, block in enumerate(bs) for ch in block}
    # D=F=0; (x,y,c,e) are relative endpoint widths.
    return (-d['x'], -d['y'], -d['c'], 0, -d['e'], 0)


def endpoint_expressions(pat):
    bs, offset, shift, names = chamber_info(pat)
    syms = [sp.Symbol(n) for n in names]
    # This is already the shifted nonnegative-u parameterization.
    lev = [sp.Integer(offset + shift) + syms[0]]
    for i in range(len(bs)-1):
        lev.append(lev[-1] + 1 + syms[i+1])
    d = {ch: lev[i] for i, block in enumerate(bs) for ch in block}
    return {'A': -d['x'], 'B': -d['y'], 'C0': -d['c'],
            'D': sp.Integer(0), 'E': -d['e'], 'F': sp.Integer(0)}, d


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
    return (N, H, L)


def monomials(d, degree=3):
    out = []
    def rec(q, left, cur):
        if q == d:
            out.append(tuple(cur))
            return
        for a in range(left + 1):
            rec(q+1, left-a, cur+[a])
    rec(0, degree, [])
    return out

@lru_cache(None)
def interpolation_basis(d):
    M = monomials(d)
    samples = [v for v in product(range(4), repeat=d) if sum(v) <= 3]
    V = sp.Matrix([[sp.prod(sp.Integer(v[q])**a[q] for q in range(d))
                    for a in M] for v in samples])
    return M, samples, V.inv()


def fit_poly(pat, which):
    d = len(chamber_info(pat)[3])
    M, samples, Vinv = interpolation_basis(d)
    vals = sp.Matrix([direct_ledger(endpoint_from_values(pat, v))[which]
                      for v in samples])
    co = Vinv * vals
    return {a: sp.factor(co[i]) for i, a in enumerate(M) if co[i] != 0}


def eval_poly(poly, vals):
    return int(sum(c * sp.prod(sp.Integer(vals[q])**a[q]
                              for q in range(len(vals)))
                   for a, c in poly.items()))


def add_scaled(*terms):
    out = {}
    for scale, poly in terms:
        for a, c in poly.items():
            out[a] = sp.factor(out.get(a, 0) + scale*c)
    return {a: c for a, c in out.items() if c != 0}


def monomial_string(a, names):
    bits = []
    for name, exponent in zip(names, a):
        if exponent == 1:
            bits.append(name)
        elif exponent > 1:
            bits.append(f'{name}^{exponent}')
    return '*'.join(bits) if bits else '1'


def coefficient_list(poly, names):
    M = monomials(len(names))
    return [{'monomial': monomial_string(a, names), 'coefficient': str(poly[a])}
            for a in M if a in poly]


def poly_string(poly, names):
    terms = []
    for row in coefficient_list(poly, names):
        mon = row['monomial']
        co = sp.Rational(row['coefficient'])
        if mon == '1':
            terms.append(str(co))
        elif co == 1:
            terms.append(mon)
        elif co == -1:
            terms.append('-' + mon)
        else:
            terms.append(str(co) + '*' + mon)
    return ' + '.join(terms).replace('+ -', '- ')


def record(idx, pat):
    bs, offset, shift, names = chamber_info(pat)
    # The fitted polynomials already use the shifted nonnegative u variable.
    N = fit_poly(pat, 0)
    H = fit_poly(pat, 1)
    L = fit_poly(pat, 2)
    R = add_scaled((3, L), (-1, N))
    # Independent generator-side exact box replay; the consumer repeats this
    # with no use of interpolation.
    fit_checks = 0
    for vals in product(range(7), repeat=len(names)):
        got = direct_ledger(endpoint_from_values(pat, vals))
        for poly, want in zip((N, H, L), got):
            assert eval_poly(poly, vals) == want, (pat, vals, got)
            fit_checks += 1
    negatives = [str(c) for c in R.values() if c < 0]
    assert not negatives, (idx, pat, negatives)
    ep_expr, level_expr = endpoint_expressions(pat)
    return {
        'id': idx, 'pattern': pat, 'blocks': bs, 'variables': names,
        'offset': offset, 'lowest_level_shift': shift,
        'strict_gap_rule': 'lambda[i+1]-lambda[i]=1+z_i',
        'parameter_domain': 'all listed variables are integers >=0',
        'endpoints': {k: str(v) for k, v in ep_expr.items()},
        'levels': {k: str(v) for k, v in level_expr.items()},
        'polynomials': {
            'N': poly_string(N, names), 'H': poly_string(H, names),
            'L': poly_string(L, names),
            'N_coefficients': coefficient_list(N, names),
            'H_coefficients': coefficient_list(H, names),
            'L_coefficients': coefficient_list(L, names),
        },
        'certificate': {
            'branch': 'L', 'alpha': '0', 'beta': '0', 'lhs': '3L-N',
            'residual': poly_string(R, names),
            'residual_coefficients': coefficient_list(R, names),
            'negative_coefficient_count': len(negatives),
        },
        'generator_box_checks': fit_checks,
    }


def main():
    assert len(PATTERNS) == 31
    records = [record(i, p) for i, p in enumerate(PATTERNS)]
    out = {
        'title': 'Exact normalized guarded-V TE(2=1) D=F facet chamber atlas',
        'status': 'COMPUTED generator output; proof labels are assigned in the companion artifact',
        'facet': 'f=F-D=0 after D=0 normalization',
        'normalized_domain': {
            'x_y_c_e': 'x>y>=0, c>=1, e>=1',
            'raw_endpoints': 'A=-x, B=-y, C0=-c, D=0, E=-e, F=0',
            'certificate_envelope': 'The 31-cell envelope is the displayed domain; exact structural guards may only shrink it.',
            'structural_realizability': 'exact acyclic/q||r/height=m/connected-incomparability guards applied before containment',
        },
        'patterns': PATTERNS,
        'pattern_count': len(records), 'records': records,
        'known_point': {
            'x': 2, 'y': 1, 'c': 2, 'e': 2, 'f': 0,
            'parameters': {'pattern': 0, 'u': 1, 'z0': 0},
            'expected_NHL': [18, 6, 11],
            'computed_NHL': list(direct_ledger((-2, -1, -2, 0, -2, 0))),
        },
    }
    path = Path('outputs/data/te21_D_eq_F_facet_atlas_20260818.json')
    path.write_text(json.dumps(out, indent=2), encoding='utf-8')
    print('PATTERN_COUNT', len(records))
    print('ALL_GENERATOR_BOX_CHECKS', sum(r['generator_box_checks'] for r in records))
    print('ALL_RESIDUAL_NEGATIVE_COUNTS', sum(r['certificate']['negative_coefficient_count'] for r in records))
    print('KNOWN_POINT', out['known_point']['computed_NHL'])
    print('DATA_PATH', str(path))

if __name__ == '__main__':
    main()

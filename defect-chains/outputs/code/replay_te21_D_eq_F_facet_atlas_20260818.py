#!/usr/bin/env python3
"""Independent consumer/replay for the exact f=0 TE(2=1) V atlas.

It deliberately does not interpolate or import the generator.  It reads the
machine-readable coefficient data, reconstructs each chamber directly from
its weak-order blocks, enumerates the exact weighted gap fibers, expands the
stored identities in a rational coefficient dictionary, and runs boundary,
coverage, and known-poset tests.
"""
from fractions import Fraction
from itertools import product, permutations
from pathlib import Path
import json

DATA = Path('outputs/data/te21_D_eq_F_facet_atlas_20260818.json')
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


def eval_poly(poly, vals):
    ans = Fraction(0)
    for a, c in poly.items():
        term = c
        for v, e in zip(vals, a):
            term *= v**e
        ans += term
    assert ans.denominator == 1, ans
    return ans.numerator


def chamber_endpoint(rec, vals):
    bs = rec['blocks']
    offset = int(rec['offset'])
    shift = int(rec['lowest_level_shift'])
    lev = [offset + shift + vals[0]]
    for i in range(len(bs)-1):
        lev.append(lev[-1] + 1 + vals[i+1])
    d = {ch: lev[i] for i, block in enumerate(bs) for ch in block}
    return (-d['x'], -d['y'], -d['c'], 0, -d['e'], 0)


def classify(x, y, c, e):
    vals = {'x': x, 'y': y, 'c': c, 'e': e}
    distinct = sorted(set(vals.values()))
    bs = []
    for q in distinct:
        bs.append(''.join(ch for ch in ORDER if vals[ch] == q))
    return '|'.join(bs)


def parameters_for(rec, x, y, c, e):
    vals = {'x': x, 'y': y, 'c': c, 'e': e}
    levels = sorted(set(vals.values()))
    offset = int(rec['offset'])
    shift = int(rec['lowest_level_shift'])
    u = levels[0] - offset - shift
    z = [levels[i+1] - levels[i] - 1 for i in range(len(levels)-1)]
    return [u] + z


def reconstruct_params(rec, vals):
    ep = chamber_endpoint(rec, vals)
    A, B, C0, D, E, F = ep
    return (-A, -B, -C0, -E)


def check_known_poset():
    # Point m=2, Ip=[0,1], Iq=Ir=[0,2].
    m = 2
    nodes = ['c1', 'c2', 'p', 'q', 'r']
    rel = set()
    for i in range(1, m+1):
        for j in range(i+1, m+1):
            rel.add((f'c{i}', f'c{j}'))
    intervals = {'p': (0, 1), 'q': (0, 2), 'r': (0, 2)}
    for u, (a, b) in intervals.items():
        for t in range(1, m+1):
            if t <= a:
                rel.add((f'c{t}', u))
            elif t > b:
                rel.add((u, f'c{t}'))
    rel.update({('p', 'q'), ('p', 'r')})
    # Transitive closure.
    changed = True
    while changed:
        changed = False
        for a, b in list(rel):
            for c, d in list(rel):
                if b == c and (a, d) not in rel:
                    rel.add((a, d)); changed = True
    acyclic = all((u, u) not in rel for u in nodes)
    q_incomp = ('q', 'r') not in rel and ('r', 'q') not in rel
    # Height by longest directed path in a topological order.
    indeg = {u: 0 for u in nodes}
    for a, b in rel:
        indeg[b] += 1
    todo = [u for u in nodes if indeg[u] == 0]
    topo = []
    while todo:
        u = todo.pop(); topo.append(u)
        for a, b in list(rel):
            if a == u:
                indeg[b] -= 1
                if indeg[b] == 0: todo.append(b)
    dp = {u: 1 for u in nodes}
    for u in topo:
        for a, b in rel:
            if a == u:
                dp[b] = max(dp[b], dp[u] + 1)
    height = max(dp.values())
    # Incomparability graph.
    adj = {u: set() for u in nodes}
    for i, u in enumerate(nodes):
        for v in nodes[i+1:]:
            if (u, v) not in rel and (v, u) not in rel:
                adj[u].add(v); adj[v].add(u)
    seen = set(); stack = [nodes[0]]
    while stack:
        u = stack.pop()
        if u in seen: continue
        seen.add(u); stack.extend(adj[u] - seen)
    connected = len(seen) == len(nodes)
    # Direct linear-extension count is an independent check of N.
    linext = 0
    for order in permutations(nodes):
        pos = {u: i for i, u in enumerate(order)}
        if all(pos[a] < pos[b] for a, b in rel):
            linext += 1
    return {
        'acyclic': acyclic, 'q_parallel_r': q_incomp, 'height': height,
        'incomparability_connected': connected, 'linear_extensions': linext,
        'ledger': direct_ledger((-2, -1, -2, 0, -2, 0)),
    }


def main():
    D = json.loads(DATA.read_text(encoding='utf-8'))
    assert D['patterns'] == PATTERNS
    records = D['records']
    assert len(records) == 31
    identity_count = 0
    identity_terms = 0
    negative_residual = 0
    negative_NHL = 0
    box_checks = 0
    boundary_checks = 0
    for rec in records:
        names = rec['variables']
        polys = rec['polynomials']
        Np = coeff_map(polys['N_coefficients'], names)
        Hp = coeff_map(polys['H_coefficients'], names)
        Lp = coeff_map(polys['L_coefficients'], names)
        Rp = coeff_map(rec['certificate']['residual_coefficients'], names)
        # Symbolic coefficient dictionary expansion of the certificate identity.
        expanded = add_scaled((3, Lp), (-1, Np))
        assert expanded == Rp, (rec['id'], expanded, Rp)
        identity_count += 1
        identity_terms += len(Rp)
        negative_residual += sum(c < 0 for c in Rp.values())
        negative_NHL += sum(c < 0 for p in (Np, Hp, Lp) for c in p.values())
        d = len(names)
        for vals in product(range(7), repeat=d):
            ep = chamber_endpoint(rec, vals)
            got = direct_ledger(ep)
            assert (eval_poly(Np, vals), eval_poly(Hp, vals),
                    eval_poly(Lp, vals)) == got, (rec['id'], vals, got)
            assert eval_poly(Rp, vals) == 3*got[2] - got[0]
            assert got[0] <= 3*got[2]
            box_checks += 3
        # All-zero is the minimal strict/equality boundary for this cell;
        # all {0,1} vectors exercise every z_i=0 and u=0/1 boundary face.
        for vals in product(range(2), repeat=d):
            ep = chamber_endpoint(rec, vals)
            got = direct_ledger(ep)
            assert eval_poly(Np, vals) == got[0]
            assert eval_poly(Hp, vals) == got[1]
            assert eval_poly(Lp, vals) == got[2]
            assert got[0] <= 3*got[2]
            boundary_checks += 1
    # Finite coverage audit of the entire normalized certificate envelope.
    coverage = 0
    pattern_hits = {p: 0 for p in PATTERNS}
    e_one = 0
    for x, y, c, e in product(range(9), repeat=4):
        if not (x > y >= 0 and c >= 1 and e >= 1):
            continue
        p = classify(x, y, c, e)
        assert p in pattern_hits, (x, y, c, e, p)
        rec = records[PATTERNS.index(p)]
        vals = parameters_for(rec, x, y, c, e)
        assert all(v >= 0 for v in vals)
        assert reconstruct_params(rec, vals) == (x, y, c, e)
        assert chamber_endpoint(rec, vals) == (-x, -y, -c, 0, -e, 0)
        N, H, L = direct_ledger(chamber_endpoint(rec, vals))
        names = rec['variables']
        Np = coeff_map(rec['polynomials']['N_coefficients'], names)
        Hp = coeff_map(rec['polynomials']['H_coefficients'], names)
        Lp = coeff_map(rec['polynomials']['L_coefficients'], names)
        assert (eval_poly(Np, vals), eval_poly(Hp, vals), eval_poly(Lp, vals)) == (N, H, L)
        pattern_hits[p] += 1; coverage += 1
        if e == 1: e_one += 1
    assert all(pattern_hits.values()), pattern_hits
    known = D['known_point']
    known_ledger = direct_ledger((-2, -1, -2, 0, -2, 0))
    assert tuple(known_ledger) == tuple(known['expected_NHL']) == tuple(known['computed_NHL'])
    # The known point is pattern 0 with (u,z0)=(1,0).
    rec0 = records[0]
    assert chamber_endpoint(rec0, [1, 0]) == (-2, -1, -2, 0, -2, 0)
    assert direct_ledger(chamber_endpoint(rec0, [1, 0])) == (18, 6, 11)
    poset = check_known_poset()
    assert poset == {
        'acyclic': True, 'q_parallel_r': True, 'height': 2,
        'incomparability_connected': True, 'linear_extensions': 18,
        'ledger': (18, 6, 11)
    }, poset
    # Hash the data actually consumed, so the replay record is auditable.
    import hashlib
    data_sha = hashlib.sha256(DATA.read_bytes()).hexdigest()
    print('DATA_SHA256', data_sha)
    print('PATTERN_COUNT', len(records))
    print('PATTERN_COVERAGE_BOX', coverage)
    print('PATTERN_HIT_COUNTS', ' '.join(f'{i}:{pattern_hits[p]}' for i, p in enumerate(PATTERNS)))
    print('IDENTITY_EXPANSIONS', identity_count)
    print('IDENTITY_RESIDUAL_TERMS', identity_terms)
    print('NEGATIVE_RESIDUAL_COEFFICIENTS', negative_residual)
    print('NEGATIVE_NHL_COEFFICIENTS', negative_NHL)
    print('DIRECT_BOX_CHECKS', box_checks)
    print('BOUNDARY_EQUALITY_CHECKS', boundary_checks)
    print('E_EQUALS_1_DOMAIN_ROWS', e_one)
    print('KNOWN_POINT', 'x=2 y=1 c=2 e=2 f=0 parameters=pattern0(u=1,z0=0) N=18 H=6 L=11')
    print('KNOWN_POSET', poset)
    print('ALL_CHECKS_PASS', True)

if __name__ == '__main__':
    main()

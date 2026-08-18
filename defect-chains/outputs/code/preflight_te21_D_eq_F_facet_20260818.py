#!/usr/bin/env python3
"""Pre-enumeration resource audit for the normalized f=0 TE(2=1) atlas.

This script deliberately performs no chamber polynomial enumeration.  It counts
ordered weak-order patterns combinatorially, derives the exact number of direct
ledger calls in the planned generator/replay, counts their innermost candidate
triples on the prescribed small boxes, and benchmarks the literal ledger on
small equal intervals.  The displayed timeout and memory budget are part of the
replay contract.
"""
from collections import Counter
from itertools import permutations, product
from time import perf_counter

LABELS = ('x', 'y', 'c', 'e')
PATTERNS = [
    'y|xce','yc|xe','yce|x','ye|xc','c|y|xe','c|ye|x','ce|y|x',
    'e|y|xc','e|yc|x','y|c|xe','y|ce|x','y|e|xc','y|x|ce',
    'y|xc|e','y|xe|c','yc|e|x','yc|x|e','ye|c|x','ye|x|c',
    'c|e|y|x','c|y|e|x','c|y|x|e','e|c|y|x','e|y|c|x',
    'e|y|x|c','y|c|e|x','y|c|x|e','y|e|c|x','y|e|x|c',
    'y|x|c|e','y|x|e|c'
]
TIMEOUT_SECONDS = 300
MEMORY_BUDGET_MIB = 256


def all_ordered_partitions(labels):
    """Unique ordered set partitions via permutation + cut encoding."""
    got = set()
    n = len(labels)
    for p in permutations(labels):
        for mask in range(1 << (n - 1)):
            blocks = []
            cur = [p[0]]
            for i in range(n - 1):
                if mask & (1 << i):
                    blocks.append(tuple(sorted(cur, key=labels.index)))
                    cur = [p[i + 1]]
                else:
                    cur.append(p[i + 1])
            blocks.append(tuple(sorted(cur, key=labels.index)))
            got.add(tuple(blocks))
    return got


def weak_order_string(blocks):
    return '|'.join(''.join(block) for block in blocks)


def chamber_values(pat, vals):
    blocks = [list(b) for b in pat.split('|')]
    # The f=0 envelope has y>=0, c,e>=1, x>y.  This is only sizing.
    lower = {'x': 0, 'y': 0, 'c': 1, 'e': 0}
    offset = max(lower[ch] for ch in blocks[0])
    shift = int(offset == 0 and 'e' in blocks[0])
    levels = [offset + shift + vals[0]]
    for z in vals[1:]:
        levels.append(levels[-1] + 1 + z)
    d = {ch: levels[i] for i, block in enumerate(blocks) for ch in block}
    return (-d['x'], -d['y'], -d['c'], 0, -d['e'], 0)


def loop_count(ep):
    A, B, C0, D, E, F = ep
    return (B-A+1) * (D-C0+1) * (F-E+1)


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


def main():
    partitions = all_ordered_partitions(LABELS)
    strict_xy = {weak_order_string(p) for p in partitions
                 if next(i for i,b in enumerate(p) if 'x' in b)
                 > next(i for i,b in enumerate(p) if 'y' in b)}
    assert len(partitions) == 75
    assert len(strict_xy) == 31
    assert set(PATTERNS) == strict_xy
    dims = Counter(p.count('|') + 1 for p in PATTERNS)
    # d = number of nonnegative parameters = number of blocks (u plus gaps).
    sample_counts = {d: (d+3)*(d+2)*(d+1)//6 for d in dims}
    interpolation_calls = 3 * sum(dims[d] * sample_counts[d] for d in dims)
    validation_direct_calls = sum(dims[d] * (7 ** d) for d in dims)
    validation_component_checks = 3 * validation_direct_calls
    boundary_direct_calls = sum(dims[d] * (2 ** d) for d in dims)
    replay_direct_calls = validation_direct_calls + boundary_direct_calls
    total_direct_calls = interpolation_calls + validation_direct_calls + replay_direct_calls

    # Exact innermost candidate-loop counts for all planned generator/replay
    # boxes, without evaluating or storing any chamber polynomials.
    generator_interpolation_triples = 0
    generator_validation_triples = 0
    replay_validation_triples = 0
    replay_boundary_triples = 0
    max_one_call = 0
    for pat in PATTERNS:
        dim = pat.count('|') + 1
        # interpolation samples: nonnegative vectors with total degree <=3
        samples = [v for v in product(range(4), repeat=dim)
                   if sum(v) <= 3]
        assert len(samples) == sample_counts[dim]
        for v in samples:
            q = loop_count(chamber_values(pat, v))
            generator_interpolation_triples += q
            max_one_call = max(max_one_call, q)
        for v in product(range(7), repeat=dim):
            q = loop_count(chamber_values(pat, v))
            generator_validation_triples += q
            replay_validation_triples += q
            max_one_call = max(max_one_call, q)
        for v in product(range(2), repeat=dim):
            replay_boundary_triples += loop_count(chamber_values(pat, v))
    # Every interpolation/validation call computes three statistics, while
    # the replay also checks the residual once per validation/boundary call.
    all_triples = (3 * (generator_interpolation_triples +
                        generator_validation_triples) +
                   4 * replay_validation_triples +
                   4 * replay_boundary_triples)

    print('PLANNED_TIMEOUT_SECONDS', TIMEOUT_SECONDS)
    print('MEMORY_BUDGET_MIB', MEMORY_BUDGET_MIB)
    print('ALL_ORDERED_WEAK_PARTITIONS', len(partitions))
    print('FILTERED_BY_x_gt_y', len(strict_xy))
    print('PATTERN_DIMENSION_COUNTS', dict(sorted(dims.items())))
    print('INTERPOLATION_SAMPLE_COUNTS_BY_DIMENSION', dict(sorted(sample_counts.items())))
    print('GENERATOR_INTERPOLATION_DIRECT_CALLS', interpolation_calls)
    print('GENERATOR_VALIDATION_DIRECT_CALLS', validation_direct_calls)
    print('GENERATOR_VALIDATION_COMPONENT_CHECKS', validation_component_checks)
    print('REPLAY_VALIDATION_DIRECT_CALLS', validation_direct_calls)
    print('REPLAY_BOUNDARY_DIRECT_CALLS', boundary_direct_calls)
    print('TOTAL_DIRECT_LEDGER_CALLS', total_direct_calls)
    print('MAX_SINGLE_CALL_TRIPLES', max_one_call)
    print('GENERATOR_INTERPOLATION_CANDIDATE_TRIPLES', generator_interpolation_triples)
    print('GENERATOR_VALIDATION_CANDIDATE_TRIPLES', generator_validation_triples)
    print('REPLAY_VALIDATION_CANDIDATE_TRIPLES', replay_validation_triples)
    print('REPLAY_BOUNDARY_CANDIDATE_TRIPLES', replay_boundary_triples)
    print('WEIGHTED_INNER_LOOP_ESTIMATE', all_triples)

    # Small literal benchmark.  One call uses an equal triple of intervals
    # [-n,0], so its candidate-loop count is (n+1)^3.  Repeat enough times to
    # smooth timer granularity, then extrapolate linearly in the loop count.
    print('BENCHMARK_HEADER n repeats candidate_triples elapsed_seconds loops_per_second extrapolated_seconds_at_n64')
    rates = []
    for n, repeats in ((2, 2000), (4, 1000), (8, 300), (12, 100)):
        ep = (-n, 0, -n, 0, -n, 0)
        calls = repeats
        t0 = perf_counter()
        checksum = 0
        for _ in range(calls):
            checksum += direct_ledger(ep)[0]
        elapsed = perf_counter() - t0
        triples = calls * (n + 1) ** 3
        rate = triples / elapsed
        rates.append(rate)
        extrap = (65 ** 3) / rate
        print('BENCHMARK', n, repeats, triples, f'{elapsed:.9f}',
              f'{rate:.3f}', f'{extrap:.9f}', 'checksum', checksum)
    print('BENCHMARK_MEDIAN_LOOPS_PER_SECOND', sorted(rates)[len(rates)//2])
    print('EXTRAPOLATION_NOTE', 'n=64 means one literal equal-interval ledger call; this is a performance estimate, not a proof step')
    print('PREFLIGHT_PASS', True)


if __name__ == '__main__':
    main()

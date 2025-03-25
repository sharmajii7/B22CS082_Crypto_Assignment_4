def factors(prime_factors):
    if len(prime_factors) == 1: return [1] + prime_factors
    _factors = factors(prime_factors[1:])
    return list(set(_factors + [prime_factors[0] * f for f in _factors]))
p = 28151
p_factors = sorted(factors([2, 5, 5, 563]))
for g in range(1, p):
    if all(pow(g, n, p) != 1 for n in p_factors[:-1]):
        print(g)
        break
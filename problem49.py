# vim: sw=4:ts=4:et:ai

import itertools
from eulertools import primes_upto

results = {}
for prime in primes_upto(9999):
    if prime >= 1000:
        number_hash = ''.join(sorted(x for x in str(prime)))
        if not results.get(number_hash, False):
            results[number_hash] = []
        results[number_hash].append(prime)

for number_hash, prime_list in results.items():
    if len(prime_list) < 3:
        continue
    for a, b, c in itertools.combinations(prime_list, 3):
        if b - a == c - b:
            print(a, b, c)


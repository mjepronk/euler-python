# vim: sw=4:ts=4:et:ai

import itertools
from eulertools import primes_upto

def main():
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
            if (a, b, c) == (1487, 4817, 8147):
                continue
            if b - a == c - b:
                return int(''.join(str(i) for i in (a, b, c)))

if __name__ == '__main__':
    print("Result: %i" % main())


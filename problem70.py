# vim: sw=4:ts=4:et:ai
# coding: utf8
"""
Problem:
  Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n and
  the ratio n/φ(n) produces a minimum.

Approach:
  The ratio n/φ(n) is mininaml when n is a prime.
  But, using a prime number for n is not interesting, because that will result
  in φ(n) = n-1. The combination n and n-1 will never be a permutation.
  So we need to build n using more than one prime.
  Analysing the formula for the totient function, shows that using multiples of
  the same prime numbers will not result in a lower n/φ(n) ratio, so don't need
  to bother with n's that are based on multiples of a prime.
  
  So we choose to build an n based on a few (2) prime numbers.
"""

from eulertools import phi, primes_erat
import itertools

def is_permutation(a, b):
    """
    >>> is_permutation(87109, 79180)
    True
    >>> is_permutation(123, 234)
    False
    """
    return sorted(str(a)) == sorted(str(b))

def main(limit=10**7):
    i = 1
    n = 1
    min_ratio = None
    min_n = None
    for p1 in primes_erat():
        for p2 in itertools.takewhile(lambda p: p < p1, primes_erat()):
            n = p1 * p2
            if n > limit:
                break
            phi_n = (p1 - 1) * (p2 - 1)
            ratio = n / phi_n
            if (min_ratio is None or ratio < min_ratio) and is_permutation(n, phi_n):
                min_ratio = ratio
                min_n = n
        if p1 * 2 > limit:
            break
    return min_n

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Result: %i" % main())


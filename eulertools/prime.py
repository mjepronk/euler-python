# vim: sw=4:ts=4:et:ai
from __future__ import division
import itertools
from math import sqrt, ceil, factorial
import array

primes_cache_n = None
primes_cache = None

def is_prime(n):
    """
    Return True if n is a prime, otherwise False

    >>> is_prime(79)
    True
    >>> is_prime(4)
    False
    """
    if n <= 1:
        return False
    m = 2
    while m <= sqrt(n):
        if n % m == 0:
            return False
        m += 1
    return True

def primes_erat():
    """
    Optimized calculation of primes using Eratosthenes

    Source:
    http://oreilly.com/pub/a/python/excerpt/pythonckbk_chap1/index1.html?page=last

    >>> list(itertools.islice(primes_erat(), 25))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p


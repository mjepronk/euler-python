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

def primes_upto_sundaram(n):
    """
    Calculate all prime numbers up to n, using the Sieve of Sundaram

    Complexity: O(n log n) operations using O(n) bits of memory

    >>> list(primes_upto_sundaram(100))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    nk = (n-1)//2
    ks = list(range(nk+1))
    for i in itertools.count(1):
        step  = 2*i+1
        start = i*(step + 1)
        if start > nk:
            break
        ks[start::step] = (0 for _ in range(start, nk+1, step))
    return (p for p in [2] + [2*k+1 for k in filter(None, ks)])

def primes_upto_eratosthenes(n):
    """
    Calculate all prime numbers up to n, using the Sieve of Eratosthenes

    >>> list(primes_upto_eratosthenes(100))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    global primes_cache_n, primes_cache
    if primes_cache_n and n <= primes_cache_n:
        return (x for x in primes_cache if x <= n)
    nroot = int(sqrt(n))
    sieve = list(range(n+1))
    sieve[1] = 0

    for i in range(2, nroot+1):
        if sieve[i] != 0:
            m = n//i - i
            sieve[i*i: n+1:i] = [0] * (m+1)

    primes_cache_n = n
    primes_cache = [x for x in sieve if x != 0]
    return (x for x in primes_cache if x <= n)

primes_upto = primes_upto_sundaram


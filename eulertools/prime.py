# vim: sw=4:ts=4:et:ai
from __future__ import division
from math import sqrt, ceil, factorial

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

def primes_upto(n):
    """
    Calculate all prime numbers up to n, using the Sieve of Eratosthenes

    >>> list(primes_upto(100))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    nroot = int(sqrt(n))
    sieve = list(range(n+1))
    sieve[1] = 0

    for i in xrange(2, nroot+1):
        if sieve[i] != 0:
            m = n//i - i
            sieve[i*i: n+1:i] = [0] * (m+1)

    return (x for x in sieve if x != 0)



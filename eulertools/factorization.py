# vim: sw=4:ts=4:et:ai
from __future__ import division
from math import sqrt, ceil, factorial

from eulertools.prime import primes_upto

def factors(n):
    """ 
    Generator for the factors of n

    >>> list(factors(1)) 
    [1]
    >>> list(factors(4)) 
    [1, 2, 4]
    >>> list(factors(15)) 
    [1, 3, 5, 15]
    >>> list(factors(28)) 
    [1, 2, 4, 7, 14, 28]
    >>> list(factors(64)) 
    [1, 2, 4, 8, 16, 32, 64]
    >>> list(factors(79)) 
    [1, 79]
    """ 
    top = int(sqrt(n))
    l = []
    for i in range(1, top+1):
        if n % i  == 0:
            if not (i == top and top*top == n):
                l.append(i)
            yield i
    for i in reversed(l):
        yield n // i

def num_factors(n):
    """
    Calculate the number of factors for n

    >>> num_factors(1)
    1
    >>> num_factors(6) 
    4
    >>> num_factors(16) 
    5
    >>> num_factors(28)
    6
    """
    top = int(sqrt(n))
    num_divisors = 0
    for i in range(1, top+1):
        if n % i == 0:
            num_divisors += 2
    # Correction if the number is a perfect square
    if top * top == n:
        num_divisors -= 1;
    return num_divisors

def prime_factors(n, largest_to_lowest=False):
    """
    Generator for the prime factors of n

    >>> prime_factors(13195, True).next()
    29
    >>> prime_factors(600851475143, True).next()
    6857
    """
    primes = list(primes_upto(int(sqrt(n))))
    if largest_to_lowest:
        primes.reverse()
    for prime in primes:
        if n % prime == 0:
            yield prime

def prime_factors2(n):
    """
    Generator for the prime factors of n
    """
    primeind = 0
    primes = list(primes_upto(int(sqrt(n))))
    p = primes[primeind]
    while p <= n:
        if n % p == 0:
            yield p
            n //= p
        else:
            primeind += 1
            p = primes[primeind]

def prime_factors_with_e(n):
    """
    Factorize n in prime factors with their exponent.
    Returns a dictionary with the prime factors as keys,
    and their exponents as values.

    >>> prime_factors_with_e(36)
    {2: 2, 3: 2}
    """
    factor_dict = {}
    primes = primes_upto(n)
    while True:
        try:
            test_prime = primes.next()
        except StopIteration:
            break
        if n % test_prime == 0:
            if factor_dict.has_key(test_prime):
                factor_dict[test_prime] += 1
            else:
                factor_dict[test_prime] = 1
            primes = primes_upto(n)
            n = n // test_prime
    return factor_dict

def prime_factors_with_e2(a):
    for p in primes():
        j = 0
        while a%p == 0:
            a /= p
            j += 1
        if j > 0:
            yield (p,j)
        if a < p*p: break
    if a > 1:
        yield (a,1)


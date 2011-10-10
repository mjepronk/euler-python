# vim: sw=4:ts=4:et:ai
from __future__ import division
from math import sqrt, ceil, factorial

def gcd(a, b):
    """ Calculate the greatest common divisor """
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """ Calculate the least common multiple """
    return a * b // gcd(a, b)

def fibonacci(n=4000000):
    """
    >>> list(fibonacci(150))
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    """
    yield 1
    a, b = 1, 2
    while a < n:
        yield a
        a, b = b, a+b

def num_combinations(n, k):
    """
    Calculate the number of combinations
    (i.e. a way of selecting several things out of a larger group, where
    (unlike permutations) order does not matter)

    >>> num_combinations(41, 6)
    4496388L
    >>> num_combinations(52, 5)
    2598960L
    """
    if k > n:
        return 0
    return factorial(n) // (factorial(n-k) * factorial(k))

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
    for i in xrange(1, top+1):
        if n % i  == 0:
            l.append(i)
            yield i
    if top * top == n:
        l = l[:-1]
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
    for i in xrange(1, top+1):
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

if __name__ == '__main__':
    import doctest
    doctest.testmod()


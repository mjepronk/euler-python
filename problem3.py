#!/bin/python
# vim: sw=4:ts=4:et:ai
"""

Problem description:
  The prime factors of 13195 are 5, 7, 13 and 29.
  What is the largest prime factor of the number 600851475143 ?

Approach:
  Use the Euclidean algorythm to solve the problem.

"""
import math

from eulertools import primes_upto

def grootste_priemfactor(x):
    """
    >>> grootste_priemfactor(13195)
    29
    >>> grootste_priemfactor(600851475143)
    6857
    """
    primes = list(primes_upto(int(math.sqrt(x))))
    primes.reverse()
    for i in primes:
        if x % i == 0:
            return i
    return None
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()



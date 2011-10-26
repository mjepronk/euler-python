# vim: sw=4:ts=4:et:ai
from __future__ import division
import itertools

from eulertools.factorization import *
from eulertools.modular import *
from eulertools.prime import *
from eulertools.probability import *

def fibonacci():
    """
    Generator for the Fibonacci sequence

    >>> list(itertools.takewhile(lambda n: n < 150, fibonacci()))
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    """
    yield 1
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a+b

def triangle_numbers(start=1):
    """
    Generator for Triangle numbers

    >>> list(itertools.takewhile(lambda n: n < 30, triangle_numbers()))
    [1, 3, 6, 10, 15, 21, 28]
    >>> list(itertools.takewhile(lambda n: n < 30, triangle_numbers(4)))
    [10, 15, 21, 28]
    """
    i = start
    n = (i * (i + 1)) // 2
    while True:
        yield n
        i += 1
        n += i

def primorials():
    """
    Generator for Primorials

    >>> list(itertools.takewhile(lambda n: n < 10000000, primorials()))
    [2, 6, 30, 210, 2310, 30030, 510510, 9699690]
    """
    primorial = 1
    for prime in primes_erat():
        primorial *= prime
        yield primorial


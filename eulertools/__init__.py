# vim: sw=4:ts=4:et:ai
from __future__ import division

from eulertools.factorization import *
from eulertools.modular import *
from eulertools.prime import *
from eulertools.probability import *

def fibonacci(n=4000000):
    """
    Generator for the Fibonacci sequence

    >>> list(fibonacci(150))
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    """
    yield 1
    a, b = 1, 2
    while a < n:
        yield a
        a, b = b, a+b


# vim: sw=4:ts=4:et:ai
from __future__ import division
from math import factorial

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


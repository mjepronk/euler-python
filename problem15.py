# vim: sw=4:ts=4:et:ai
"""
Problem:
 Starting in the top left corner of a 2x2 grid, there are 6 routes (without
 backtracking) to the bottom right corner. How many routes are there through a
 20x20 grid?

Approach:
 Calculate the permutations of 20 times RIGHT and 20 times DOWN.

"""
import itertools
from math import factorial

def brute_force(n):
    """
    Brute force method, for large n this takes a very long time.
    Calculate the number of unique permutations for 20 times RIGHT and 20 times DOWN
    """
    routes = set(''.join(r) for r in itertools.permutations('R' * n + 'D' * n, n*2))
    return len(routes)

def multiset_permutations(n):
    """
    If M is a finite multiset, then a multiset permutation is a sequence of
    elements of M in which each element appears exactly as often as is its
    multiplicity in M. If the multiplicities of the elements of M (taken in some
    order) are m1, m2, ..., ml and their sum (i.e., the size of M) is n, then the
    number of multiset permutations of M is given by the multinomial coefficient:
    """
    num_routes = factorial(n*2) // (factorial(n) * factorial(n))
    return num_routes

def main(n=20):
    # return brute_force(n)
    return multiset_permutations(n)

if __name__ == '__main__':
    print("Result: %i" % main())


# vim: sw=4:ts=4:et:ai

import operator
from eulertools import *

def triangle_numbers(limit=100, start=1):
    """
    >>> list(triangle_numbers(7))
    [1, 3, 6, 10, 15, 21, 28]
    >>> list(triangle_numbers(7, 4))
    [10, 15, 21, 28]
    """
    for n in xrange(start, limit+1):
        yield (n*(n+1))//2


def find_highly_composite(num_divisors):
    """
    http://en.wikipedia.org/wiki/Highly_composite_number
    """
    sum(1 for f in factors)
    return number


def main(max_num_factors=200):
    start = 50000
    for i, n in enumerate(triangle_numbers(999999, start), start):
        num_factors = sum(1 for f in factors(n))
        print n, num_factors
        if num_factors > max_num_factors:
            break
    print "Triangle %i with value %i is the first to have over %i divisors." % (i, n, max_num_factors)



if __name__ == '__main__':
    #import doctest
    #doctest.testmod()
    #main()
    find_number_with_n_factors(500)


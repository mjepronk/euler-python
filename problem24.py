# vim: sw=4:ts=4:et:ai
"""
Problem:
 What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
 5, 6, 7, 8 and 9?

Approach:
 There are n! = 10! = 3628800 permutations of 0-9.
 Brute force them using the help of itertools.

"""

import itertools

def main(use_set=range(10), n=1000000):
    """
    >>> main((0, 1, 2), 5)
    '201'
    """
    count = 1
    for p in itertools.permutations(use_set, len(use_set)):
        if count == n:
            return ''.join(str(x) for x in p)
        count += 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print("Result: %s" % main())


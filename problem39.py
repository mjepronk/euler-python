# vim: sw=4:ts=4:et:ai
import itertools
from math import sqrt, ceil
from eulertools import pythagorean_triples

def main():
    combinations_dict = {}
    for a, b, c in itertools.takewhile(lambda triplet: triplet[0] < 1000, pythagorean_triples()):
        p = a + b + c
        if p > 1000:
            # Skip triplets with perimeter over 1000
            continue
        if p in combinations_dict:
            combinations_dict[p] += 1
        else:
            combinations_dict[p] = 1
    c, p =  max((c, p) for p, c in combinations_dict.items())
    return p

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print("Result: %i" % main())



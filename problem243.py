# vim: sw=4:ts=4:et:ai

from fractions import Fraction, gcd
from eulertools import phi


def ratio_resilient_fractions(d):
    """
    Determine the ratio of "resilient fractions" for a given denominator.

    For the denominator 12 there are 4 resilient fractions (out of 11 proper fractions):
    >>> ratio_resilient_fractions(12)
    Fraction(4, 11)

    For the denominator 100 there are 40 resilient fractions (out of 99 proper fractions):
    >>> ratio_resilient_fractions(100)
    Fraction(40, 99)

    For prime numbers all the fractions will be resilient:
    >>> ratio_resilient_fractions(97327)
    Fraction(1, 1)
    """
    num = 0
    for i in range(1, d):
        # For every proper fraction...
        if gcd(i, d) == 1:
            # If the numerator and the denominator are coprime,
            # than the fraction is "resilient"...
            num += 1
    return Fraction(num, d-1)    

def main(smaller_than=None):
    if not smaller_than:
        smaller_than = Fraction(15499, 94744)
    d = 2
    while True:
        ratio = Fraction(phi(d), d-1)
        if ratio < smaller_than:
            break
        d += 1
    return d

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Result: %i" % main())

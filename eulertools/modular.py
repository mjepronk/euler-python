# vim: sw=4:ts=4:et:ai
from __future__ import division
from fractions import gcd

from eulertools.factorization import prime_factors_with_e


def lcm(a, b):
    """ Calculate the least common multiple """
    return a * b // gcd(a, b)

def multi_order(a, m):
    """
    Calculate the multiplicative order

    Sources:
    http://en.wikipedia.org/wiki/Multiplicative_order
    http://rosettacode.org/wiki/Multiplicative_order

    >>> multi_order(37, 1000)
    100
    >>> multi_order(4, 7)
    3
    """
    def multi_order1(a, (p, e)):
        m = p**e
        # Calculate Phi(p**e) where p prime
        t = (p-1)*(p**(e-1))
        qs = [1,]
        for f in prime_factors_with_e(t).iteritems():
            qs = [q * f[0]**j for j in xrange(1+f[1]) for q in qs]
        qs.sort()
        for q in qs:
            if pow(a, q, m) == 1: break
        return q

    assert gcd(a, m) == 1
    mofs = (multi_order1(a, r) for r in prime_factors_with_e(m).iteritems())
    return reduce(lcm, mofs, 1)

def period_len_fraction(p, q):
    """
    Calculate the period (repeating decimals) length for a specific fraction

    Sources:
    http://en.wikipedia.org/wiki/Repeating_decimal
    http://www.lrz.de/~hr/numb/period.html

	p = numerator
	q = denominator

    >>> period_len_fraction(1, 7)
    6
    >>> period_len_fraction(1, 17)
    16
    >>> period_len_fraction(1, 97)
    96
    """
    try:
        assert p == 1, "Sorry only 1 allowed for numerator."
        # A fraction in lowest terms with a prime denominator other than 2 or 5
        # (i.e. coprime to 10) always produces a repeating decimal
        assert gcd(p, q) == 1, "This fraction is not expressed in it's lowest terms."
        assert gcd(10, q) == 1, "This fraction will not result in repeating decimals."
        return multi_order(10, q)
    except:
        return 0


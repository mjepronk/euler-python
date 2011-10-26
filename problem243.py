# vim: sw=4:ts=4:et:ai
from math import sqrt, floor, ceil
from fractions import Fraction, gcd
from eulertools import phi, primes_upto, primes_erat
from functools import reduce
import operator


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
    return Fraction(phi(d), d-1)    

def main(smaller_than=None):
    if not smaller_than:
        smaller_than = Fraction(15499, 94744)
    # We know that phi(n)/n is the smallest when n is a primorial,
    # so first look for Phi(priomorial)/primorial which is smaller than our
    # target faction.
    primorial = 1
    prime_list = []
    for prime in primes_erat():
        primorial *= prime
        prime_list.append(prime)
        phi_primorial = reduce(operator.mul, ((p-1) for p in prime_list))
        ratio = Fraction(phi_primorial, primorial)
        print(primorial, ratio)
        if ratio < smaller_than:
            break
    #return primorial
    # Then search for Phi(n)/n-1 which is smaller than our target fraction.
    found = False
    for n in range(primorial, primorial+100000):
        ratio = Fraction(phi(n), n-1)
        if n % 1000 == 0:
            print(n, ratio)
        if ratio < smaller_than:
            found = True
            break
    if found:
        return n
    else:
        return 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Result: %i" % main())


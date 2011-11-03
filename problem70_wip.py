# vim: sw=4:ts=4:et:ai
from eulertools import phi, primes_erat
import itertools

def is_permutation(a, b):
    """
    >>> is_permutation(87109, 79180)
    True
    >>> is_permutation(123, 234)
    False
    """
    return sorted(str(a)) == sorted(str(b))

def main(limit=10000000):
    # We know that n/phi(n) is a minimum for primes
    i = 1
    for n in itertools.takewhile(lambda n: n < limit, primes_erat()):
        if is_permutation(n, phi(n)):
            return n
        if i % 1000 == 0:
            print(i, n)
        i += 1
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Result: %i" % main())


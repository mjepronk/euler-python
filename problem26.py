# vim: sw=4:ts=4:et:ai
import itertools
from functools import reduce
from eulertools import period_len_fraction, primes_erat

def main():
    def tup_max(a, b):
        if a[1] > b[1]:
            return a
        else:
            return b

    return reduce(tup_max, ((p, period_len_fraction(1, p)) for p in itertools.takewhile(lambda p: p < 1000, primes_erat())))[0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print("Result: %i" % main())


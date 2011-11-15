# vim: sw=4:ts=4:et:ai
import itertools
from eulertools import primes_erat

def main():
    return next(itertools.islice(itertools.takewhile(lambda p: p < 200000, primes_erat()), 10000, None))

if __name__ == '__main__':
    print("Result: %i" % main())


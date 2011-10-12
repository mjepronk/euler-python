# vim: sw=4:ts=4:et:ai
import itertools
from eulertools import primes_upto

def main():
    return next(itertools.islice(primes_upto(200000), 10000, None))

if __name__ == '__main__':
    print("Result: %i" % main())


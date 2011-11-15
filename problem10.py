# vim: sw=4:ts=4:et:ai
import itertools
from eulertools import primes_erat

def main():
    return sum(itertools.takewhile(lambda x: x < 2000000, primes_erat()))

if __name__ == '__main__':
    print("Result: %i" % main())


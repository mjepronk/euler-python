# vim: sw=4:ts=4:et:ai
from eulertools import phi, primorials
import itertools


def main(limit=1000000):
    # We know that n/phi(n) is highest when n is a primorial
    for n in itertools.takewhile(lambda n: n < limit, primorials()):
        pass
    return n    

if __name__ == "__main__":
    print("Result: %i" % main())


# vim: sw=4:ts=4:et:ai
from eulertools import *
import itertools

def main():
    for i in range(3, 100000, 2):
        if is_prime(i):
            continue
        found = False
        for p in itertools.takewhile(lambda p: p < i, primes_erat()):
            rest = i - p
            square_int = sqrt(rest / 2)
            if square_int == int(square_int):
                found = True
                break
        if not found:
            return i

if __name__ == '__main__':
    print("Result: %i" % main())


# vim: sw=4:ts=4:et:ai
import itertools
from eulertools import primes_erat

def main():
    limit = 10**9
    pandigital = list(range(1, 10))
    largest = None
    for prime in primes_erat():
        if prime > limit:
            break
        digits = str(prime)
        if sorted(int(d) for d in digits) == pandigital[:len(digits)]:
            largest = prime
    return largest
    
if __name__ == '__main__':
    print("Result: %i" % main())


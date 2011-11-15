# vim: sw=4:ts=4:et:ai
import itertools
from eulertools import primes_erat

def main():
    pandigital = list(range(1, 10))
    largest = None
    for prime in primes_erat():
        if prime < 10**6:
            # numbers below 7 digits are not interesting
            continue
        elif prime > 10**7:
            # pandigital numbers with 8 or 9 digits,
            # are all divisible by 9 (non prime)
            break
        digits = str(prime)
        if sorted(int(d) for d in digits) == pandigital[:len(digits)]:
            largest = prime
    return largest
    
if __name__ == '__main__':
    print("Result: %i" % main())


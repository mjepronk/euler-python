# vim: sw=4:ts=4:et:ai
import itertools
from math import log, ceil
from collections import deque
from eulertools import primes_erat, is_prime

def main(top=1000000):
    prime_found = None

    # Generate a list with cumalitive sum
    cum_sum_primes = [0]
    cum_sum = 0
    for p in primes_erat():
        cum_sum += p
        cum_sum_primes.append(cum_sum)
        if cum_sum > top:
            break

    num_primes = len(cum_sum_primes)
    num_terms = num_primes
    while True:
        for offset in range(0, 10):
            if offset + num_terms >= num_primes:
                break
            sum_of_primes = cum_sum_primes[offset+num_terms] - cum_sum_primes[offset]
            if sum_of_primes < top and is_prime(sum_of_primes):
                prime_found = sum_of_primes
                break
        if prime_found:
            break
        num_terms -= 1
    return prime_found

if __name__ == '__main__':
    assert main(100) == 41
    assert main(1000) == 953
    print("Result: %i" % main())


# vim: sw=4:ts=4:et:ai
import itertools
from eulertools import primes_erat, is_prime, rotations

def main(max_prime=1000000):
    prime_list = set(p for p in itertools.takewhile(lambda x: x < max_prime, primes_erat()))
    count = 0
    for n in prime_list:
        is_circular = True
        for x in rotations(str(n)):
            x = int(x)
            if x == n:
                continue
            if x < max_prime and not x in prime_list:
                is_circular = False
                break
            elif x >= max_prime and not is_prime(x):
                is_circular = False
                break
        if is_circular:
            count += 1
    return count

if __name__ == '__main__':
    print("Result: %i" % main())

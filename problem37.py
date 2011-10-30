# vim: sw=4:ts=4:et:ai
import itertools
from eulertools import primes_erat

def main(max_prime=1000000):
    total = 0
    count = 0
    prime_list = set()
    for n in primes_erat():
        prime_list.add(n)
        if n < 10:
            continue
        n = str(n)
        is_truncatable = True
        # Remove digits from the right
        for l in range(len(n)-1, 0, -1):
            x = n[:l]
            if not int(x) in prime_list:
                is_truncatable = False
                break
        if not is_truncatable:
            continue
        # Remove digits from the left
        for l in range(1, len(n)):
            x = n[l:]
            if not int(x) in prime_list:
                is_truncatable = False
                break
        if not is_truncatable:
            continue
        # If all above test have passed, it's one of the numbers we're after
        total += int(n)
        count += 1
        if count == 11:
            break
    return total

if __name__ == '__main__':
    print("Result: %i" % main())

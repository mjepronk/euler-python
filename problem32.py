# vim: sw=4:ts=4:et:ai
import itertools
from math import ceil

def main():
    pandigital = list(range(1, 10))
    products_found = set()
    print("Pandigital %s" % pandigital)
    for a in range(1, 99):
        if a % 10 == 0 or a % 11 == 0:
            # Skip powers of 10 and 11
            continue
        start = ceil(10000/a)
        for b in range(start, 1, -1):
            product = a * b
            if product < 1000:
                break
            digits = '%i%i%i' % (a, b, product)
            digits = sorted(int(d) for d in digits)
            if digits == pandigital:
                print("%i x %i = %i" % (a, b, product))
                products_found.add(product)
    return sum(product for product in products_found)

if __name__ == '__main__':
    print("Result: %i" % main())


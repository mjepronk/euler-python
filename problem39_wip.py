# vim: sw=4:ts=4:et:ai
from math import sqrt, ceil

def combinations_for_p(p):
    """
    >>> combinations_for_p(120)
    3
    """
    count = 0
    for a in range(1, ceil(p/3)):
        for b in range(a, p):
            c = sqrt(a ** 2 + b ** 2)
            if a + b + c == p:
                count += 1
    return count

def main():
    max_count = 0
    max_p = 0
    for p in range(1000, 1, -1):
        count = combinations_for_p(p)
        if count > max_count:
            max_count = count
            max_p = p
    return max_p

if __name__ == '__main__':
    print("Result: %i" % main())


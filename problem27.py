# vim: sw=4:ts=4:et:ai

from eulertools import is_prime


def try_formula(a, b):
    """
    >>> try_formula(1, 41)
    40
    >>> try_formula(-79, 1601)
    80
    """
    n = 0
    while True:
        x = (n**2) + (a*n) + b
        if not is_prime(x):
            break
        n += 1
    return n

def main():
    """
    """
    max_n, a, b = max((try_formula(a, b), a, b) for a in range(-999, 1000) for b in range(-999, 1000))
    return a * b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print("Result: %i" % main())


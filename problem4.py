# vim: sw=4:ts=4:et:ai
import math
from eulertools import is_palindromic

def grootste_palindroom(aantal_cijfers):
    """
    >>> grootste_palindroom(2)
    9009
    >>> grootste_palindroom(3)
    906609
    """
    grootste_palindroom = 0
    max_aantal = int(math.pow(10, aantal_cijfers))

    for x in range(max_aantal, 0, -1):
        for y in range(x, 0, -1):
            test = x * y
            if is_palindromic(test) and test > grootste_palindroom:
                grootste_palindroom = test

    return grootste_palindroom

def main(n=3):
    return grootste_palindroom(3)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print("Result: %i" % main())


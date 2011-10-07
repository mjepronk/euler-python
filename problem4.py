# vim: sw=4:ts=4:et:ai

import math

def is_palindroom(n):
    """
    >>> is_palindroom(9009)
    True
    >>> is_palindroom(12321)
    True
    >>> is_palindroom(1234)
    False
    """
    a = list(str(n))
    b = list(str(n))
    b.reverse()
    return a == b

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
            if is_palindroom(test) and test > grootste_palindroom:
                grootste_palindroom = test

    return grootste_palindroom


if __name__ == '__main__':
    import doctest
    doctest.testmod()


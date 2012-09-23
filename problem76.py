# vim: sw=4:ts=4:et:ai
from eulertools import partition_num

def main(n=100):
    """
    >>> main(1)
    0
    >>> main(3)
    2
    >>> main(5)
    6
    >>> main(7)
    14
    """
    c = 0
    for i in partition_num(n):
        c += 1
    return c - 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print("Result: %i" % main())

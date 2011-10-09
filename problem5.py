# vim: sw=4:ts=4:et:ai

from eulertools import lcm

def main(n):
    """
    >>> main(5)
    60.0
    >>> main(10)
    2520.0
    >>> main(20)
    232792560.0
    """
    num = lcm(1, 2)
    for i in range(2, n+1):
        num = lcm(num, i)
    return num

if __name__ == '__main__':
    import doctest
    doctest.testmod()


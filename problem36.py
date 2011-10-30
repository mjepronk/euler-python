# vim: sw=4:ts=4:et:ai
import math
from eulertools import is_palindromic

def main():
    return sum(i for i in range(1, 1000000) if is_palindromic(str(i)) and is_palindromic(bin(i)[2:]))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print("Result: %i" % main())


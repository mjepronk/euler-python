# vim: sw=4:ts=4:et:ai
from math import factorial

def main(n=100):
    return sum(int(d) for d in str(factorial(n)))

if __name__ == '':
    print("Result: %i" % main())


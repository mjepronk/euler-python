# vim: sw=4:ts=4:et:ai

from eulertools import primes_upto

def main():
    return sum(primes_upto(2000000))

if __name__ == '__main__':
    print("Result: %i" % main())


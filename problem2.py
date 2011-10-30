# vim: sw=4:ts=4:et:ai
import itertools
from eulertools import fibonacci

def main():
    return sum([i for i in itertools.takewhile(lambda x: x <= 4000000, fibonacci()) if i % 2 == 0])

if __name__ == '__main__':
    print("Result: %i" % main())

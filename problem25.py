# vim: sw=4:ts=4:et:ai
import itertools
from eulertools import fibonacci

def main():
    for i, f in enumerate(fibonacci(), 1): 
        if len(str(f)) >= 1000:
            return i

if __name__ == '__main__':
    print("Result: %i" % main())

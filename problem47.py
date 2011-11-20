# vim: sw=4:ts=4:et:ai
import itertools
from collections import deque
from eulertools import *

def main():
    num_integers = 4
    num_pfactors = 4
    d = deque([], num_integers)
    for i in range(100000, 1000000, 1):
        pfactors = list((p, e) for p, e in prime_factors_with_e(i))
        d.appendleft(pfactors)
        if len(d) == num_integers:
            # Check all factors in deque are unique
            uniq_pfactors = set()
            is_uniq = True
            for pfactor_list in d:
                for pfactor in pfactor_list:
                    if pfactor in uniq_pfactors:
                        is_uniq = False
                        break
                    else:
                        uniq_pfactors.add(pfactor)
                if not is_uniq:
                    break
            if is_uniq and len(uniq_pfactors) == num_integers * num_pfactors:
                return i - (num_integers - 1)

if __name__ == '__main__':
    print("Result: %i" % main())


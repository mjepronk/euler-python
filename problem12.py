# vim: sw=4:ts=4:et:ai

import operator
from eulertools import num_factors, triangle_numbers

def main(min_num_factors=500):
    start = 1
    for i, n in enumerate(triangle_numbers(999999, start), start):
        num_fact = num_factors(n)
        if num_fact > min_num_factors:
            break
    #print("Triangle %i with value %i is the first to have over %i (%i) divisors." % (i, n, min_num_factors, num_fact))
    return n

if __name__ == '__main__':
    print("Result: %i" % main(500))


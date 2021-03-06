# vim: sw=4:ts=4:et:ai

import operator
from eulertools import num_factors, triangle_numbers

def main(min_num_factors=500):
    for n in triangle_numbers():
        num_fact = num_factors(n)
        if num_fact > min_num_factors:
            break
    return n

if __name__ == '__main__':
    print("Result: %i" % main(500))


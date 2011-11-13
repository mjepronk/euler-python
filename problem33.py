# vim: sw=4:ts=4:et:ai
import operator
from fractions import Fraction, gcd
from functools import reduce

def main():
    curious_fractions = []
    for d1 in range(10, 99):
        for n1 in range(10, d1):
            # Calculate the new numerator and the digit we remove
            n2, rem_n = divmod(n1, 10)
            # Calculate the new denominator and the digit we remove
            rem_d, d2 = divmod(d1, 10)
            if (n1 * d2) == (n2 * d1) and rem_n == rem_d:
                # If the fraction is still the same and the digit we remove
                # from both the numerator and the denominator is the same:
                curious_fractions.append(Fraction(n2, d2))
    result = reduce(operator.mul, curious_fractions)
    return result.denominator

if __name__ == '__main__':
    print("Result: %i" % main())


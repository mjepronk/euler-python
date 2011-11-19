# vim: sw=4:ts=4:et:ai
import itertools

"""
Approach:
 The largest pandigital number is:
   987654321

 One of larger pandigital number which is also a concatenated product is given
 as an example:
   918273645

 The first multiplier is one so the integer must start with a 9.
 The integer must be of length 1 or 3. One is already tried, so we try integer 912-987

"""

def main():
    largest_pandigit = 0
    pandigital = [str(i) for i in range(1, 10)]
    for x in itertools.chain(
        range(9, 10),
        range(91, 99),
        range(912, 988),
        range(9123, 9877)):
        concat_product = ''
        n = 1
        while len(concat_product) < 9:
            concat_product += str(x*n)
            n += 1
        if len(concat_product) > 9:
            continue
        if sorted(concat_product) == pandigital:
            if int(concat_product) > largest_pandigit:
                largest_pandigit = int(concat_product)
    return largest_pandigit

if __name__ == '__main__':
    print("Result: %i" % main())

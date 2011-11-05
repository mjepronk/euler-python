# vim: sw=4:ts=4:et:ai
import itertools

def main():
    pandigital = list(range(10))
    divisors = [2, 3, 5, 7, 11, 13, 17]
    #start = 1023456789
    #limit = 10**10
    results = []
    #for n in range(start, limit):
    #    digits = str(n)
    for digits in itertools.permutations('0123456789', 10):
        if digits[0] == '0':
            continue
        if not sorted(int(d) for d in digits) == pandigital:
            continue
        digits = ''.join(digits)
        divisible = True
        for i, d in enumerate(divisors, 1): 
            substr = digits[i:i+3]
            if not int(substr) % d == 0:
                divisible = False
                break
        if divisible:
            n = int(digits)
            results.append(n)
    return sum(results)

if __name__ == '__main__':
    print("Result: %i" % main())


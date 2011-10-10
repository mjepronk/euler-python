# vim: sw=4:ts=4:et:ai

from eulertools import factors

def main():
    result = 0
    test_numbers = range(1, 10000)
    for i in test_numbers:
        a = sum(list(factors(i))[:-1])
        b = sum(list(factors(a))[:-1])
        if i == b and a != b:
            test_numbers.remove(max(a, b))
            result += a + b
    return result

if __name__ == '__main__':
    print "Result: %i" % main()


# vim: sw=4:ts=4:et:ai
from eulertools import factorial

def main():
    n = 11
    factorions = []
    while n <= 40585:
        sum_fact_digits = sum(factorial(int(d)) for d in str(n))
        if n == sum_fact_digits:
            factorions.append(n)
        n += 1
    return sum(n for n in factorions)

if __name__ == '__main__':
    print("Result: %i" % main())


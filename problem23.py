# vim: sw=4:ts=4:et:ai

from eulertools import factors

def abundant_numbers(n=1000):
    # find all abundant numbers up to n
    for i in range(12, n):
        a = sum(list(factors(i))[:-1])
        if a > i:
            yield i

def main():
    top = 28124
    total = 0
    abundant_set = set(n for n in abundant_numbers(top))
    for i in range(1, top):
        is_sum_of_abundant = False
        for n in abundant_set:
            if n >= i:
                break
            rest = i - n
            if rest in abundant_set:
                is_sum_of_abundant = True
                break
        if not is_sum_of_abundant:
            total += i
    return total

if __name__ == '__main__':
    print("Result: %i" % main())


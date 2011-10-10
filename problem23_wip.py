# vim: sw=4:ts=4:et:ai

from eulertools import factors

def main():
    # find all abundant numbers
    for i in range(1, 20):
        a = sum(list(factors(i))[:-1])
        if a > i:
            print i, list(factors(i))[:-1]
    return 1

if __name__ == '__main__':
    print "Result: %i" % main()


# vim: sw=4:ts=4:et:ai

from eulertools import fibonacci

def main():
    return sum([i for i in fibonacci() if i % 2 == 0])

if __name__ == '__main__':
    print("Result: %i" % main())

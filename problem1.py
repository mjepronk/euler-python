# vim: sw=4:ts=4:et:ai

def main():
    return sum(filter(lambda n: n%3 == 0 or n%5 == 0, range(1000)))

if __name__ == '__main__':
    print("Result: %i" % main())


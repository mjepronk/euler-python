# vim: sw=4:ts=4:et:ai

def main():
    return sum(int(d) for d in str(2**1000))

if __name__ == '__main__':
    print("Result: %i" % main())


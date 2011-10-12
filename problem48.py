# vim: sw=4:ts=4:et:ai

def main():
    result = sum(i ** i for i in range(1, 1001))
    return int((str(result)[-10:]))

if __name__ == '__main__':
    print("Result: %i" % main())


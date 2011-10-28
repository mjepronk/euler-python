# vim: sw=4:ts=4:et:ai

def main():
    terms = set(a**b for a in range(2, 101) for b in range(2, 101))
    return len(terms)

if __name__ == '__main__':
    print("Result: %i" % main())


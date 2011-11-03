import operator
from functools import reduce

def main():
    d = [(10**i)-1 for i in range(7)]
    temp = ''.join(str(i) for i in range(1, 500000))
    return reduce(operator.mul, (int(temp[x]) for x in d))

if __name__ == '__main__':
    print("Result: %i" % main())


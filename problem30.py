# vim: sw=4:ts=4:et:ai

def main():
    total = 0
    for i in range(10, 1000000):
        sum_of_powers = sum(int(digit) ** 5 for digit in str(i))
        if i == sum_of_powers:
            total += i
    return total

if __name__ == '__main__':
    print("Result: %i" % main())


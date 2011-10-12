# vim: sw=4:ts=4:et:ai

def calc_collatz(c, n):
    if n not in c:
        if n % 2 == 0:
            # Even
            c[n] = calc_collatz(c, n//2) + 1
        else:
            # Odd
            c[n] = calc_collatz(c, (3*n + 1)//2) + 2
    return c[n]

def main():
    collatz = {1:1}
    max_chain = 0
    max_i = None
    for i in range(999999, 750000, -2):
        n = calc_collatz(collatz, i)
        if max_chain < n:
            max_chain = n
            max_i = i
    return max_i

if __name__ == '__main__':
    #import cProfile
    #cProfile.run('main()')
    print("Result: %i" % main())


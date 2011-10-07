# vim: sw=4:ts=4:et:ai

def fibonacci(n=4000000):
    a, b = 1, 2
    while a < n:
        yield a
        a, b = b, a+b

result = sum([i for i in fibonacci() if i % 2 == 0])

print("Result: %i" % result)

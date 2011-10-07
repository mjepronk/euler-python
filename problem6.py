# vim: sw=4:ts=4:et:ai

a = sum(i**2 for i in range(1, 101))
b = sum(i for i in range(1, 101))**2
print("Result: %i" % (b - a))


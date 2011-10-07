# vim: sw=4:ts=4:et:ai

result = sum(filter(lambda n: n%3 == 0 or n%5 == 0, range(1000)))

print("Result: %i" % result)

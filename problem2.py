# vim: sw=4:ts=4:et:ai

from eulertools import fibonacci

result = sum([i for i in fibonacci() if i % 2 == 0])

print("Result: %i" % result)

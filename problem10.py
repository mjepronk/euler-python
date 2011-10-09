# vim: sw=4:ts=4:et:ai

from eulertools import primes_upto

result = sum(primes_upto(2000000))

print("Result: %i" % result)

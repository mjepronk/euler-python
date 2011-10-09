# vim: sw=4:ts=4:et:ai
import math

upper_limit = 1000

found = False
for a in range(1, upper_limit):
    for b in range(1, upper_limit):
        c = math.sqrt(a**2 + b**2)
        if a + b + c == 1000:
            found = True
            break
    if found == True:
        break

print("%i + %i + %i == 1000" % (a, b, c))
print("product = %i" % (a * b * c))

            

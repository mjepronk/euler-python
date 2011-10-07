
from prime import is_prime

i = 1
count = 0
while True:
    if is_prime(i):
        count += 1
        if count == 10001:
            print("10.001ste priemgetal is: %i" % i)
            break
    i += 1


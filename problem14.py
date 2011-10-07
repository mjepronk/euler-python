

def func(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1

longest_chain = None
longest_start = None
for i in range(1000000):
    count = 0
    n = i
    while n > 1:
        n = func(n)
        count += 1
    if not longest_chain or count > longest_chain:
        longest_chain = count
        longest_start = i

print(longest_start, longest_chain)


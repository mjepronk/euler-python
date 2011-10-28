# vim: sw=4:ts=4:et:ai
import heapq
from eulertools import pentagonal_numbers

def main():
    penta_set = set()
    inspect_queue = []
    heapq.heapify(inspect_queue)
    for a in pentagonal_numbers():
        for b in penta_set:
            difference = a - b
            if difference in penta_set:
                # The difference is a pentagonal number
                # store in temporary list to evaluate later
                heapq.heappush(inspect_queue, (a+b, a, b))
        found = False 
        penta_set.add(a)
        while len(inspect_queue) > 0 and inspect_queue[0][0] <= a:
            # Now inspect the sums of two pentagonals
            # which difference is already confirmed to be a pentagonal
            s, x, y = heapq.heappop(inspect_queue)
            if s in penta_set:
                found = True
                break
        if found:
            break
    return x - y

if __name__ == '__main__':
    print("Result: %i" % main())


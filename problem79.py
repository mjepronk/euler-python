# vim: sw=4:ts=4:et:ai
import string
import itertools

class InvalidKey(Exception):
    pass

def backtrack_search(constraints, domain, key):
    # Check if key matches constraints
    num_constraints_matched = 0
    for i, char in enumerate(key):
        for char_a, char_b in constraints:
            if char == char_b:
                # Check that char_a is in key before char
                if not char_a in key[:i]:
                    raise InvalidKey
                num_constraints_matched += 1
    # If all constraints are satisfied, we've found our key
    if len(constraints) == num_constraints_matched:
        return key
    # Recursively try a new key with a character from the domain appended
    for char in domain:
        # Do not use a character twice, therefore everytime limit the domain.
        # However, the problem doesn't specify that a char can occur only once.
        new_domain = [c for c in domain if c != char]
        try:
            key = backtrack_search(constraints, new_domain, key + [char])
        except InvalidKey:
            continue
        return key

def main():
    fp = open('resources/keylog.txt', 'r')
    data = fp.readlines()
    fp.close()

    # Set of constraints
    # tuple pairs of (a, b), where a should be before b
    constraints_set = set()
    domain = set()
    for line in data:
        line = line.strip()
        prev_char = None
        for char in line:
            domain.add(char)
            if prev_char:
                constraints_set.add((prev_char, char))
            prev_char = char
    key = backtrack_search(constraints_set, domain, [])
    return int(''.join(key))

if __name__ == '__main__':
    print("Result: %i" % main())


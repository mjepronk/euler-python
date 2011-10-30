# vim: sw=4:ts=4:et:ai
import itertools
import string
from eulertools import triangle_numbers

def main():
    # Generate a set of the first x triangle numbers
    triangle_set = set(n for n in itertools.islice(triangle_numbers(), 100))

    # Loop over the words in the file and count the number of triangle words
    count = 0
    words = (word.strip('"') for word in open('resources/words.txt', 'r').read().split(','))
    for word in words:
        word_value = sum(string.ascii_uppercase.index(letter) + 1 for letter in word)
        if word_value in triangle_set:
            count += 1

    return count

if __name__ == '__main__':
    print("Result: %i" % main())


# vim: sw=4:ts=4:et:ai

import string

def is_triangle_word(word, triangle_numbers):
    word_value = sum(string.ascii_uppercase.index(letter) + 1 for letter in word)
    return word_value in triangle_numbers

def main():
    # Generate a list of the first n triangle numbers
    n = 1
    triangle_numbers = set()
    for i in range(2, 1000):
        triangle_numbers.add(n)
        n += i

    # Loop over the words in the file and count the number of triangle words
    count = 0
    words = (word.strip('"') for word in open('resources/words.txt', 'r').read().split(','))
    for word in words:
        if is_triangle_word(word, triangle_numbers):
            count += 1

    return count

if __name__ == '__main__':
    print("Result: %i" % main())


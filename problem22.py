# vim: sw=4:ts=4:et:ai

import string

def alpha_value(word):
    return sum(string.ascii_uppercase.index(letter) + 1 for letter in word)

def main():
    # Loop over the names in the file and count the score
    sum_of_names = 0
    names = [word.strip('"') for word in open('resources/names.txt', 'r').read().split(',')]
    names.sort()
    for i, name in enumerate(names, start=1):
        sum_of_names += alpha_value(name) * i
    return sum_of_names

if __name__ == '__main__':
    print("Result is: %i" % main())



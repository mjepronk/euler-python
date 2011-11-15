# vim: sw=4:ts=4:et:ai
import string
import itertools

def main():
    fp = open('resources/cipher1.txt', 'r')
    data = fp.read()
    fp.close()

    key_length = 3
    key_chars = [ord(c) for c in string.ascii_lowercase]
    english_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + ' .,'
    data = [int(c) for c in data.split(',')]
    for key_values in itertools.permutations(key_chars, key_length):
        decrypted = ''.join(chr(dc ^ pc) for dc, pc in zip(data, itertools.cycle(key_values)))
        decrypted_english = ''.join(c for c in decrypted if c in english_chars)
        ratio = len(decrypted_english) / len(decrypted)
        if ratio > 0.99:
            #print(ratio, decrypted)
            return sum(dc ^ pc for dc, pc in zip(data, itertools.cycle(key_values)))
    return 0

if __name__ == '__main__':
    print("Result: %i" % main())


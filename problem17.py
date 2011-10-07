# vim: sw=4:ts=4:et:ai

ones = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen"]
 
tens = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"]
 

def number_to_words(n, sep=' '):
    """
    >>> number_to_words(8)
    'eight'
    >>> number_to_words(14)
    'fourteen'
    >>> number_to_words(115)
    'one hundred and fifteen'
    >>> number_to_words(342)
    'three hundred and forty two'
    >>> number_to_words(1000)
    'one thousand'
    >>> number_to_words(9999)
    'nine thousand nine hundred and ninety nine'
    """
    assert n > 0, "We support from 1 only"
    assert n < 10000, "We support up to 9999 only"
    
    words = []

    # Convert the thousands
    r, n = n/1000, n%1000
    if r > 0:
        words.append(ones[r])
        words.append('thousand')

    # Convert the hundreds
    r, n = n/100, n%100
    if r > 0:
        words.append(ones[r])
        words.append('hundred')

    # Optionally, add 'and'
    if len(words) > 0 and n > 0:
        words.append('and')

    # Convert the tens and ones
    if n < 20:
        words.append(ones[n])
    else:
        r, n = n/10, n%10
        words.append(tens[r])
        words.append(ones[n])
        
    return sep.join(filter(lambda w: len(w) > 0, words))


def length_in_words(n):
    """
    >>> length_in_words(342)
    23
    >>> length_in_words(115)
    20
    """
    words = number_to_words(n, sep='')
    return len(words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print("Result: %i" % sum(length_in_words(n) for n in range(1, 1001)))


# vim: sw=4:ts=4:et:ai
import itertools

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

ONE_PAIR       = 2
TWO_PAIRS      = 3
THREE_OF_KIND  = 4
STRAIGHT       = 5
FLUSH          = 6
FULL_HOUSE     = 7
FOUR_OF_KIND   = 8
STRAIGHT_FLUSH = 9
ROYAL_FLUSH    = 10

def lookup_value(card_count, frequency, count_freq=1):
    """
    Given a list of tuples (value, frequency)
    find the card(s) with the given frequency,
    and return the value that is the highest.
    """
    if count_freq > 1:
        # This is used to determine Two Pairs
        cards = [v[0] for v in card_count if v[1] == frequency]
        if len(cards) != count_freq:
            return None
        else:
            return max(cards)
    else:
        try:
            return next(v[0] for v in card_count if v[1] == frequency)
        except StopIteration:
            return None

def is_straight(card_list):
    """
    Is the list of card values a Straight?
    """
    offset = card_list[0]
    limit = card_list[0] + len(card_list)
    if card_list == list(range(offset, limit)):
        return True
    return False


def calculate_hand(hand):
    """
    Calculate the rank of the hand.
    Returns a tuple of the rank and the value that the rank is made up of.

    >>> calculate_hand(['TH', 'JH', 'QH', 'KH', 'AH']) == (ROYAL_FLUSH, 12)
    True
    >>> calculate_hand(['2H', '3H', '4H', '5H', '6H']) == (STRAIGHT_FLUSH, 4)
    True
    >>> calculate_hand(['2H', '5H', '7H', '8H', '9H']) == (FLUSH, 7)
    True
    >>> calculate_hand(['5H', '5C', '6S', '7S', 'KD']) == (ONE_PAIR, 3)
    True
    >>> calculate_hand(['2H', '2D', '4C', '4D', '4S']) == (FULL_HOUSE, 2)
    True
    >>> calculate_hand(['2H', '3D', '4C', '5D', '6S']) == (STRAIGHT, 4)
    True
    """
    # Create a list of all the different suits that are in the hand
    suits_in_hand = {c[1] for c in hand}

    # Create a list of all card values ordered by their value
    card_list = sorted(CARDS.index(c[0]) for c in hand)

    # All cards are of the same suite?
    if len(suits_in_hand) == 1:
        value = max(card_list)

        # Royal flush
        if card_list == list(range(8, 13)):
            return (ROYAL_FLUSH, value)
        # Straight Flush
        if is_straight(card_list):
            return (STRAIGHT_FLUSH, value)
        # Flush
        return (FLUSH, value)
    else:
        # Count the number of cards with the same value
        card_count = [(v, card_list.count(v)) for v in set(card_list)]

        # Four of a Kind
        value = lookup_value(card_count, 4)
        if value is not None:
            return (FOUR_OF_KIND, value)
        # Full House
        value = lookup_value(card_count, 3)
        value2 = lookup_value(card_count, 2)
        if value is not None and value2 is not None:
            return (FULL_HOUSE, value)
        # Straight
        if is_straight(card_list):
            value = max(card_list)
            return (STRAIGHT, value)
        # Three of a Kind
        if value is not None:
            return (THREE_OF_KIND, value)
        # Two Pairs
        value = lookup_value(card_count, 2, 2)
        if value is not None:
            return (TWO_PAIRS, value)
        # One Pair
        value = lookup_value(card_count, 2)
        if value is not None:
            return (ONE_PAIR, value)

    # Calculate the value of the highest card
    value = max(card_list)
    return (0, value)

def is_player_one_winner(line):
    """
    Given a line from the file, deterime if Player 1
    is the winner.

    >>> is_player_one_winner('5H 5C 6S 7S KD 2C 3S 8S 8D TD')
    False
    >>> is_player_one_winner('5D 8C 9S JS AC 2C 5C 7D 8S QH')
    True
    >>> is_player_one_winner('2D 9C AS AH AC 3D 6D 7D TD QD')
    False
    >>> is_player_one_winner('4D 6S 9H QH QC 3D 6D 7H QD QS')
    True
    >>> is_player_one_winner('2H 2D 4C 4D 4S 3C 3D 3S 9S 9D')
    True
    """
    line = line.split(' ')
    hand1, hand2 = line[:5], line[5:]
    rank1, value1 = calculate_hand(hand1)
    rank2, value2 = calculate_hand(hand2)
    if rank1 > rank2:
        # Player one has a higher rank than player two.
        return True
    elif rank1 == rank2 and value1 > value2:
        # If two players have the same ranked hands
        # then the rank made up of the highest value
        # wins; for example, a pair of eights beats a
        # pair of fives.
        return True
    elif rank1 == rank2 and value1 == value2:
        # But if two ranks tie, for example, both
        # players have a pair of queens, then highest
        # cards in each hand are compared.
        # If the highest cards tie then the next
        # highest cards are compared, and so on.
        cards1 = sorted((CARDS.index(c[0]) for c in hand1), reverse=True)
        cards2 = sorted((CARDS.index(c[0]) for c in hand2), reverse=True)
        for i in range(len(cards1)):
            if cards1[i] > cards2[i]:
                return True
            if cards1[i] < cards2[i]:
                return False
    return False

def main():
    num_hands_won = 0
    with open('resources/poker.txt', 'r') as fp:
        for line in fp:
            if is_player_one_winner(line):
                num_hands_won += 1
    return num_hands_won

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print("Result: %i" % main())



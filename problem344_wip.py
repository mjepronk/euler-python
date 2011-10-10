#!/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4:ts=4:et:ai
"""

Problem:

  One variant of N.G. de Bruijn's silver dollar game can be described as follows:
  
  On a strip of squares a number of coins are placed, at most one coin per square.
  Only one coin, called the silver dollar, has any value. Two players take turns
  making moves. At each turn a player must make either a regular or a special
  move.
  
  A regular move consists of selecting one coin and moving it one or more squares
  to the left. The coin cannot move out of the strip or jump on or over another
  coin.
  
  Alternatively, the player can choose to make the special move of pocketing the
  leftmost coin rather than making a regular move. If no regular moves are
  possible, the player is forced to pocket the leftmost coin.
  
  The winner is the player who pockets the silver dollar.

Approach:

  A first idea would be consider the number of squares between two neighboring
  coins to be a subgame. However, we will first insert a coin at position 0. By
  the rules in the game this coin cannot be moved. This will make it easier for us
  to deal with the first coin that is not at position 0. For instance, if we have
  coins at positions 0, 2, 5, and 8, then we would have a pile of size 2-0 = 2,
  one of size 5-2 = 3, and finally one of size 8-5 = 3.
  
  These piles seem to somehow corresponds to piles in Nim. It is clear that
  whenever a player moves a coin (for instance by moving the coin at 5 to 3), he
  decreases a pile by the number of squares that he moves the coin. However, there
  is a slight problem with this decomposition into subgames. By moving a coin, we
  will also increase the size of another pile. For instance, if we move the coin
  at 5 to 3, then we decrease one pile by 2, but also increase a pile by 2. This
  decomposition does not really work, because subgames must by definition be
  independent. We should now be asking ourselves whether there is a way to make
  this idea work.
  
  With the above ideas in mind, it would be a good idea to play around with the
  The Silver Dollar game before proceeding.
  
  There was a problem with adjacent piles in the above decomposition into
  subgames. We can try to skip every other pile and define our subgames by this.
  So for example if we have coins at positions 0, 4, 10, 20 and 35, then we would
  have piles of size 4, 6, 10, 15, but now we will ignore every second one. So we
  have only the piles of size 4 and 10. Now, a move will either decrease the size
  of a pile, or it will increase the size of one pile. This is good because
  subgames are independent as we require them to be. For instance, if we move the
  coin at 4 to 2, we decrease the first pile by 2, and if move the coin at 10 to
  7, we increase the second pile by 3. There is still a problem however because
  moving the coin at position 35 has no effect on any of the piles. This is not
  good because in some sense it allows a player to choose not to make a move, and
  this is not allowed by the rules of impartial games. We can fairly easily fix
  this problem by selecting the piles from the other end instead. So if we have
  piles of size 4, 6, 10 and 15 as before, we simply select our piles to be first
  pile from the end, and then skipping every other pile. In this case, we get the
  piles 15 and 6. This decomposition into independent subgames is now correct, and
  every move in the real game corresponds to a move in our subgame, and vice
  versa.
  
  Now, we have been able to decompose the game into independent subgames, so we
  just need to figure out what the Grundy number of each position is, xor them and
  check if it equal to 0. If it is, we lose and otherwise we win.
  
  So in our decomposition into subgames, a subgame is essentially just Nim, but we
  may also increase the size of a pile. We now argue that this type of move can be
  disregarded. If a player increases the size of a pile, we may make a move to
  immediately decrease the size of the pile again leaving the player in the exact
  same position as before he increased the pile. Hence the move is not useful. You
  may wonder whether the game terminates, but it is quite obvious from the rules
  of the problem statement that it does.
  
  To recap the algorithm to solve the problem is to compute the difference between
  each coin starting from the last one, ignore every second, xor the numbers and
  output that the player to begin loses iff the xor is 0, and otherwise we output
  that the starting player wins. The complexity of determining the winner is O(N),
  where N is the number of coins in the input.
  
Links used:
 - http://www.codechef.com/wiki/tutorial-coin-game
 - http://www.cut-the-knot.org/Curriculum/Games/SilverDollar.shtml
 - http://www.itu.dk/people/brit/Brits%20thesis.pdf
 - http://web.mit.edu/sp.268/www/nim.pdf
"""

import operator
import itertools

X_SILVER_COIN = 2
X_COIN        = 1
X_EMPTY       = 0

def calculate_number_of_moves(strip):
    """"
    Calculate how many moves we can make with each coin

    We calculate the number of moves every coin can make.
    Pocketing the coin is a seperate move.

    >>> calculate_number_of_moves([1, 0, 2, 1, 1, 1])
    [1, 0, 1, 0, 0, 0]
    >>> calculate_number_of_moves([0, 0, 0, 0, 2, 1])
    [0, 0, 0, 0, 4, 0]
    >>> calculate_number_of_moves([0, 1, 0, 0, 0, 2])
    [0, 1, 0, 0, 0, 3]
    """
    list_number_of_moves = []
    empty_since = None

    for i, x in enumerate(strip):
        number_of_moves = 0
        if x != X_EMPTY:
            if i == 0:
                # Special move
                number_of_moves = 1
            elif empty_since is not None:
                # Check how many moves to left are possible
                number_of_moves = (empty_since - i) * -1
            empty_since = None
        else:
            # This position is empty, mark it
            if empty_since is None:
                empty_since = i
        list_number_of_moves.append(number_of_moves)
    return list_number_of_moves

def calculate_nim_piles(strip):
    """"
    Calculate the piles for nim from the Silver Coin game strip
    Highly experimental

    >>> calculate_nim_piles([1, 0, 2, 1, 1, 1])
    [1, 1]
    >>> calculate_nim_piles([0, 0, 0, 0, 2, 1])
    [1]
    >>> calculate_nim_piles([0, 1, 0, 0, 0, 2])
    [2, 1]
    """
    nim_pile_list = []
    #strip = strip[:strip.index(X_SILVER_COIN)+1]
    for i, x in enumerate(strip):
        number_of_moves = 0
        if x != X_COIN:
            nim_pile_list.append(i+1)
        #if x == X_SILVER_COIN:
        #    nim_pile_list.append(1)
    return nim_pile_list


def is_winning_configuration(strip):
    """
    A winning configuration is an arrangement of coins on the strip where the
    first player can force a win no matter what the second player does.

    We calculate this position by calculating the Nim sum of the game.
    The winning configurations are namely exactly the ones with Nim sum zero.
    I.e. a winning move is a move to a position with Nim sum zero (and vice versa).
    
    >>> is_winning_configuration([0, 1, 0, 0, 1, 0, 1, 2, 0, 1])
    True
    """
    # For W(10,2) this situation happens 210 out of 840 configurations
    # Which is of course not 25% by coincidence...
    left_most_coin = (x for x in strip if x > 0).next()
    if left_most_coin == X_SILVER_COIN:
        return True
    """
    If we have piles of size 4, 6, 10 and 15, we simply select our
    piles to be first pile from the end, and then skipping every other pile. In
    this case, we get the piles 15 and 6. This decomposition into independent
    subgames is now correct, and every move in the real game corresponds to a
    move in our subgame, and vice versa.
    """
    pile_list = filter(lambda x: x > 0, calculate_nim_piles(strip))
    #pile_list = filter(lambda x: x > 0, calculate_number_of_moves(strip))
    #pile_list = pile_list[len(pile_list)::-2]

    """"
    Now, we have been able to decompose the game into independent subgames, so we
    just need to figure out what the Nimber of each position is, xor them and
    check if it equal to 0. If it is, we lose and otherwise we win.
    """
    nim_number = reduce(operator.xor, (n for n in pile_list))

    return nim_number != 0

def unique(iterable):
    """
    >>> list(unique("ABABCBAACBA"))
    ['A', 'B', 'C']
    """
    seen = set()
    seen_add = seen.add
    for element in itertools.ifilterfalse(seen.__contains__, iterable):
        seen_add(element)
        yield element

def number_of_winning_configurations(num_squares, num_coins):
    """
    >>> number_of_winning_configurations(10, 2)
    (840, 324)

    #>>> number_of_winning_configurations(100, 10)
    #1514704946113500
    """
    num_coins += 1

    square_set = [2] + ([1] * num_coins) + ([0] * (num_squares-num_coins-1))

    # Create every possible strip from square_set
    # and check if it's a winning strip
    count = 0
    winning_count = 0
    for strip in unique(itertools.permutations(square_set)):
        count += 1
        if is_winning_configuration(strip):
            winning_count += 1

    return count, winning_count

    

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)

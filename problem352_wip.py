# vim: sw=4:ts=4:et:ai
# -*- coding: utf-8 -*-
"""
"""

import math.factorial as factorial

def combination(a, b):
    """
    >>> combination(41, 6)
    4496388L
    """
    return factorial(a) / (factorial(a-b) * factorial(b))

def prob_infected(group_size, prob_infected):
    """
    Geeft de kans dat tenminste één schaap besmet is in een groep.
    """
    return 1 - ((1-prob_infected)**group_size)

def prob_no_last_test_needed(group_size, prob_infected):
    """
    De kans dat van een besmette groep, alleen het schaap dat het laatste van
    de groep getest wordt, besmet is.
    
    Aanpak:
     A. bereken de kans dat van de groep slechts één schaap besmet is;
        de kans dat er tenminste één besmet is, is 1!
        binomiale verdeling of standaard verdeling?
     B. bereken de kans dat dit het laatste schaap is dat gekozen wordt;
     C. bereken de voorwaardelijke kans op B. gegeven gebeurtenis A.
    
    http://www.wiswijzer.nl/pagina.asp?nummer=57
    
    >>> round(prob_no_last_test_needed(3, 0.4), 3)
    0.432
    """
    # Bereken de kans dat van alle schapen in de groep, slechts 1 schaap geïnfecteerd is
    #  ???
    prob_one_sheep_infected = combination(group_size, 1) * (prob_infected**1) * ((1-prob_infected)**(group_size-1))
    # Bereken de kans dat het enige geïnfecteerde schaap als laatste overblijft
    #
    prob_last_sheep_infected = 
    # Bereken de voorwaardelijke kans
    return (prob_last_sheep_infected * prob_one_sheep_infected) / prob_one_sheep_infected 

if __name__ == '__main__':
    import doctest
    doctest.testmod()

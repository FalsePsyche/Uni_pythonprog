"""Higher Order Functions used for simulations of dice rolls.

Definition: An n-sided dice function takes no arguments and always returns an int from 1 to n, inclusive.

Types of n-sided dice functions:
 -  Randomized: a randomized dice function can be fair, meaning that ir produce each possible outcome 
    from 1 to n with equal probability. Examples: four_sided, six_sided
 -  Deterministic: a deterministic dice function will be used for testing.  Deterministic test dice functions always cycle
    through a fixed sequence of n values. 
 -  We write a make_fair_dice higher-order function to return a fair, randomized n-sided dice function.
 -  We write a make_test_dice higher-order function that will return a deterministic, testing n-sided dice function.
"""

from random import randint

def make_fair_dice(n):
    """Returns an n-sided fair dice function."""
    assert type(n) == int and n >= 1, 'Illegal value for number of sides'
    def dice():
        return randint(1,n)
    return dice

four_sided = make_fair_dice(4)
six_sided = make_fair_dice(6)

def make_test_dice(*outcomes):    
    """Return an n-sided dice function that cycles deterministically through outcomes - a rest parameter.

    >>> dice = make_test_dice(4, 1, 3)
    >>> dice(), dice(), dice(), dice()
    (4, 1, 3, 4)
    
    """
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1
    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]
    return dice
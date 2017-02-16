# Tanner Bornemann
# Homework01 - Python Programming - Section 001
# 2017-02-12

"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1
    sum = 0
    count = 0
    while count < num_rolls:
        this_roll = dice()
        # print statement for debugging
        # print("this_roll: {0}".format(this_roll))
        if this_roll == 1:
            sum = 1
            count += num_rolls  # immediately return 1 for score
        else:
            sum += this_roll
        count += 1
    return sum
    # END Question 1


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    this_score = 1  # default to one for use if we get a 1 value return from roll_dice
    if num_rolls > 0:
        this_score = roll_dice(num_rolls, dice)
    else:
        if opponent_score < 10:
            this_score = opponent_score + 1
        else:
            opponent_score_string = str(opponent_score)
            opp_score_tens = opponent_score_string[
                0]  # get the tens digit in the score
            opp_score_ones = opponent_score_string[
                1]  # get the ones digit in the score

            this_score = max(int(opp_score_ones), int(opp_score_tens)) + 1
    return this_score

    # END Question 2


def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    sum = score + opponent_score
    if sum % 7 == 0:
        return four_sided
    else:
        return six_sided
    # END Question 3

def swine_swap(score0, score1):
    """Enforces the 'Swine Swap' rule in the game. this will return the scores given
    in the function arguments either swapped or not swapped depending on the result 
    from is_swap func. For example: if is_swap returns true then this function's
    return values will consist of score1 first, then score0.
    i.e. 
    return score1, score0 # when is_swap returns True
    """
    if is_swap(score0, score1):
        return score1, score0
    else:
        return score0, score1



def is_swap(score0, score1):
    """Return True if ending a turn with SCORE0 and SCORE1 will result in a
    swap.

    Swaps occur when the last two digits of the first score are the reverse
    of the last two digits of the second score.
    """
    # BEGIN Question 4
    # check to make sure we don't end up with 3 chars for the swap comparision
    # if score0 >= 100:
    #     score0 -= 100
    # if score1 >= 100:
    #     score1 -= 100
    if score0 < 10:
        player0_tens = '0'
    else:
        player0_tens = str(score0)[-2] # get the second to right most digit
    player0_ones = str(score0)[-1] # get the right most digit
    if score1 < 10:
        player1_tens = '0'
    else:
        player1_tens = str(score1)[-2]
    player1_ones = str(score1)[-1]
    if player0_tens + player0_ones == player1_ones + player1_tens:
        return True
    elif player1_tens + player1_ones == player0_ones + player0_tens:
        return True
    else:
        return False
    # END Question 4


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5

    playing = True
    while playing:
        # if a player has reached the goal score then stop playing and return
        # the players' scores.
        if score0 >= goal or score1 >= goal:
            playing = False
            break
        # play player0
        if who is 0:
            score0 += take_turn(strategy0(score0, score1), score1, select_dice(score0, score1))
        # play player1
        elif who is 1:
            score1 += take_turn(strategy1(score1, score0), score0, select_dice(score1, score0))
        score0, score1 = swine_swap(score0, score1) # enforce Swine Swap rule
        who = other(who)

    # END Question 5
    return score0, score1


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

"""Required questions for lab 1"""

## Boolean Operators ##

# Q4
def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    "*** YOUR CODE HERE ***"
    if x > 0 and y > 0:
        return True
    else:
        return False
    # return x and y > 0  # note: why does this fail the doctest?


## while Loops ##

# Q7
def factors(n):
    """Prints out all of the numbers that divide `n` evenly.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    # todo: fix this, only prints one item?
    for divisor in range(1, n):
        quotient = n % divisor
        if quotient == 0:
            return divisor

# Q8
def fib(n):
    """Returns the nth Fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(100)
    354224848179261915075
    """
    "*** YOUR CODE HERE ***"
    if n is 0 or 1:
        return n
    else:
        return fib(n + 1) + fib(n + 2)
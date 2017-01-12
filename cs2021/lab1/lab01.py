import doctest

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
    >>> factors(30)
    30
    15
    10
    6
    5
    3
    2
    1
    """
    "*** YOUR CODE HERE ***"
    for divisor in range(n, 0, -1):  # start loop at n then iterate using -1 until 0
        remainder = n % divisor  # get remainder of division of n and loop step
        if remainder == 0:  # check if remainder is 0 to make sure the divisor 'evenly' divides into the argument
            print(divisor)


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
    a = 0
    b = 1
    # a, b = 0, 1
    for i in range(n):
        # a, b = b, a + b  # note: everything on the right side of the assignment is
        #  evaluated before the assignment happens so this single line is the same as the
        # next 3 lines:
        temp = a
        a = b
        b = temp + b
    return a


def _test():
    doctest.testmod()

if __name__ == "__main__":
    doctest.testmod()
    _test()

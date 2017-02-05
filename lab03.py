# Tanner Bornemann
# Lab03 - Python Programming - Section 001
# 2017-02-04

import doctest

# Q1
def skip_add(n):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    """
    "*** YOUR CODE HERE ***"
    # if number is 0 then return the value and break Recursion
    # else add n to skip_add(n - 2) and return that value
    if n <= 0:
        # print(n)
        return 0
    # print(n)
    x = n + skip_add(n - 2)  # do the math s owe can print it for debugging
    # print(x)  # print for debugging
    return x


# Q6
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    min_val = min(a, b)  # get max and min
    max_val = max(a, b)
    x = max_val % min_val  # find remainder of max divided by min
    if x is 0:  # if no remainder then we can return divisor as the greatest common denominator
        return min_val
    else:
        mod = max_val % min_val
        return gcd(min_val, mod)



# Q7
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n <= 1:
        return 1
    else:
        if n % 2 == 0:
            return hailstone(n // 2) + 1
        else:
            return hailstone(n * 3 + 1) + 1


# Q8
def fibonacci(n):
    """Return the nth fibonacci number.

    >>> fibonacci(11)
    89
    >>> fibonacci(5)
    5
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    """
    "*** YOUR CODE HERE ***"
    if n is 1:
        return 1
    elif n is 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Q9
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m is 1:  # if m is 1 then we have a grid the size of 1 x n. any grid with a size 1 for any axis means we have only one path left so return 1
        return 1
    elif n is 1:
        return 1
    x = m - 1  # get the next size down on the m axis
    y = n - 1  # get the next size down on the n axis
    return paths(x, n) + paths(m, y)



# print("final: " + str(skip_add(5)))
# doctest.testmod(verbose=True)

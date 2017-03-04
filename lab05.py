import doctest

## Lab 5: Linked Lists ##

#Q1

def len_link(lst):
    """Returns the length of the link.

    >>> lst = link(1, link(2, link(3, link(4))))
    >>> len_link(lst)
    4
    >>> len_link(empty)
    0
    """
    link_count = 0
    if is_link(lst) and lst != empty:  # make sure we have a linked list for lst
        first_item = first(lst)
        link_count = 1  # start at 1 because we have the first item in first_item
        remainder_items = rest(lst)  # get the items that are after the first one
        more_items = True
        while more_items:
            if is_link(remainder_items) and remainder_items != empty:  # check to verify that the remainder of the list is not empty
                link_count += 1
                remainder_items = rest(remainder_items)
            else:
                more_items = False  # since there are no more items in the list, we break out
    else:
        assert "the arg is not a linked list"
    return link_count

#Q2

def sum_linked_list(lst, fn):
    """ Applies a function FN to each number in LST and returns the sum
    of the resulting values

    >>> square = lambda x: x * x
    >>> double = lambda y: 2 * y
    >>> lst1 = link(1, link(2, link(3, link(4))))
    >>> sum_linked_list(lst1, square)
    30
    >>> lst2 = link(3, link(5, link(4, link(10))))
    >>> sum_linked_list(lst2, double)
    44
    """
    "*** YOUR CODE HERE ***"


#Q3

def map(fn, lst):
    """Returns a list of the results produced by applying f to each
    element in lst.

    >>> my_list = link(1, link(2, link(3, link(4, empty))))
    >>> print_link(map(lambda x: x * x, my_list))
    1 4 9 16
    >>> pokemon = link('bulbasaur', link('charmander', link('squirtle', empty)))
    >>> print_link(map(print, pokemon))
    bulbasaur
    charmander
    squirtle
    None None None
    """
    "*** YOUR CODE HERE ***"


#Q4

def insert(lst, item, index):
    """ Returns a link matching lst but with the given item inserted at the
    specified index. If the index is greater than the current length, the item
    is appended to the end of the list.

    >>> lst = link(1, link(2, link(3)))
    >>> new = insert(lst, 9001, 1)
    >>> print_link(new)
    1 9001 2 3
    """
    "*** YOUR CODE HERE ***"


# Linked list ADT

# Linked List definition
empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))

def link(first, rest=empty):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)


if __name__ == "__main__":
    doctest.testmod()
    _test()

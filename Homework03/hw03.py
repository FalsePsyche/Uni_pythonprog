def is_sorted(lst):
    """Returns True if the linked list is sorted.

    >>> lst1 = link(1, link(2, link(3, link(4))))
    >>> is_sorted(lst1)
    True
    >>> lst2 = link(1, link(3, link(2, link(4, link(5)))))
    >>> is_sorted(lst2)
    False
    >>> lst3 = link(3, link(3, link(3)))
    >>> is_sorted(lst3)
    True
    """
    if rest_is_empty(lst): #return true if lst at 1 is empty using rest_is_empty()
        return True
    if first(lst) <= first(rest(lst)): # if first is less than or equal to the first of the rest of the list
        return is_sorted(rest(lst))
    return False


def interleave(s0, s1):
    """Interleave linked lists s0 and s1 to produce a new linked
    list.

    >>> evens = link(2, link(4, link(6, link(8, empty))))
    >>> odds = link(1, link(3, empty))
    >>> print_link(interleave(odds, evens))
    1 2 3 4 6 8
    >>> print_link(interleave(evens, odds))
    2 1 4 3 6 8
    >>> print_link(interleave(odds, odds))
    1 1 3 3
    """
    if rest_is_empty(s0):
        if rest_is_empty(s1):
            return link(first(s0), link(first(s1)))
        return link(first(s0), link(first(s1), rest(s1)))
    if rest_is_empty(s1):
        return link(first(s0), link(first(s1), rest(s0)))
    return link(first(s0), link(first(s1), interleave(rest(s0), rest(s1))))


def height(t):
    """Return the depth of the deepest node in the tree.

    >>> height(tree(1))
    0
    >>> height(tree(1, [tree(2), tree(3)]))
    1
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> height(numbers)
    2
    """
    def depth_finder(t, depth):
        x=[]
    depth = 0
    max_depth = 0
    if is_leaf(t): return 0
    for i in branches(t):
        something = depth_finder(i, depth + 1)
        if something > max_depth:
            max_depth = something


def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    def add_leaves(leaf, vals):
        for i in range(len(vals)):
            vals[i] = tree(vals[i])
        return tree(leaf, vals)

    if is_leaf(t):
        t = add_leaves(t, vals)
        return t

    for i in range(len(branches(t))):
        current_branch = branches(t)[i]
        if is_leaf(current_branch):
            current_branch = add_leaves(current_branch, vals)
        else:
            current_branch = sprout_leaves(current_branch, vals)
    return t


###################
# Linked List ADT #
###################

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

def rest_is_empty(s):
    if s[1] is empty:
        return True
    return False

def first_is_empty(s):
    if s[0] is empty:
        return True
    return False

############
# Tree ADT #
############

def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the entry.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(root(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
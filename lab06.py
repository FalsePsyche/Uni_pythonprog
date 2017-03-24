## Lab 6: Trees ##

# pyTunes
def make_pytunes(username):
    """Return a pyTunes tree as shown in the diagram with USERNAME as the value
    of the root.

    >>> pytunes = make_pytunes('i_love_music')
    >>> print_tree(pytunes)
    i_love_music
      pop
        justin bieber
          single
            what do you mean?
        2015 pop mashup
      trance
        darude
          sandstorm
    """
    # create the two main trees with free songs
    poptree = tree('pop',
                   [tree('justin bieber',
                         [tree('single',
                               [tree('what do you mean?')])]),
                    tree('2015 pop mashup')])
    trancetree = tree('trance', [tree('darude', [tree('sandstorm')])])
    t = tree(username, [poptree, trancetree])
    return t

def num_songs(t):
    """Return the number of songs in the pyTunes tree, t.

    >>> pytunes = make_pytunes('i_love_music')
    >>> num_songs(pytunes)
    3
    """
    if is_leaf(t):
        return 1
    else:
        s = 0
        for b in branches(t):
            s+=num_songs(b)
        return s

def add_song(t, song, category):
    """Returns a new tree with SONG added to CATEGORY. Assume the CATEGORY
    already exists.

    >>> indie_tunes = tree('indie_tunes',
    ...                  [tree('indie',
    ...                    [tree('vance joy',
    ...                       [tree('riptide')])])])
    >>> new_indie = add_song(indie_tunes, 'georgia', 'vance joy')
    >>> print_tree(new_indie)
    indie_tunes
      indie
        vance joy
          riptide
          georgia

    """
    # need to dig down into the tree to find the matching category
    for b in branches(t):
        b_root = root(b)
        if b_root == category:
            new_leaves = branches(b) + [tree(song)]
            new_branch = tree(b_root, new_leaves)
            new_tree = tree(root(t), [new_branch])
            return new_tree
        else:
            new_song = add_song(b, song, category)
            t = tree(root(t), [new_song])
    return t


# Tree ADT
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

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(root(t), [copy_tree(b) for b in branches(t)])


def delete(t, target):
    """Returns the tree that results from deleting TARGET from t. If TARGET is
    a category, delete everything inside of it.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                            tree('uptown funk'),
    ...                            tree('see you again')])])
    >>> new = delete(my_account, 'pop')
    >>> print_tree(new)
    kpop_king
      korean
        gangnam style
        wedding dress
    >>> my_account = tree('kpop_king',
    ...                     [tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                            tree('uptown funk'),
    ...                            tree('see you again')]),
    ...                     tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')])])
    >>> new = delete(my_account, 'pop')
    >>> print_tree(new)
    kpop_king
      korean
        gangnam style
        wedding dress
    >>> my_account = tree('kpop_king',
    ...                     [tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                            tree('uptown funk'),
    ...                            tree('see you again')]),
    ...                     tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('korean2',
    ...                          [tree('gangnam style2'),
    ...                           tree('wedding dress2')])
    ...                     ]
    ...                   )
    >>> new = delete(my_account, 'pop')
    >>> print_tree(new)
    kpop_king
      korean
        gangnam style
        wedding dress
      korean2
        gangnam style2
        wedding dress2
    """
    # need to dig down into the tree to find the matching category
    tree_root = root(t)
    if is_leaf(t):
        return t
    for b in branches(t):
        b_root = root(b)  # get root of b for comparison to target
        is_a_leaf = is_leaf(b)  # check to make sure this branch is not actually a leaf
        target_found = b_root == target
        if is_a_leaf:  # if branch is a leaf then continue on with the next iteration of the for loop of brnaches
            continue
        elif target_found:  # if target found then we will not return with this branch, which will remove it from t?
            continue
        else:
            tree_with_deleted_target = delete(b, target)
            t = tree(tree_root, [tree_with_deleted_target])
    return t


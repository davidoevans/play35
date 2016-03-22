import re
import itertools


def decent_number(n):
    if n < 10:
        set_of_threes = ['33333' * (i+1) for i in range(int(n/5))]
        set_of_fives = ['555' * (i+1) for i in range(int(n/3))]
        options = map(''.join, itertools.chain(itertools.product(set_of_threes, set_of_fives), itertools.product(set_of_fives, set_of_threes)))
        full_set = [int(x) for x in set_of_threes if len(x) == n]
        full_set = full_set + list([int(x) for x in set_of_fives if len(x) == n])
        full_set = full_set + list([int(x) for x in options if len(x) == n])
        if len(full_set) == 0:
            return -1
        elif len(full_set) > 1:
            return max(full_set)
        else:
            return full_set[0]
    else:
        # from discussion board
        z = n
        while z % 3 != 0:
            z -= 5
            if z < 0:
                return -1
            else:
                return int(z * '5' + (n-z) * '3')


def grid_search(p, g):
    """
    Solution to the https://www.hackerrank.com/challenges/the-grid-search challenge.

    Note that the regular expression repeats the search at every index which decreases performance but catches
    edge cases where the submatrix contains repeating characters.  See test #9.
    
    :param p: parent matrix
    :param g: submatrix to find
    :return: YES if submatrix found in parent, otherwise NO
    """
    for g_i in range(len(g)):
        for found in re.finditer(r'(?=(' + p[0] + '))', g[g_i]):
            if found.start() + len(p[0]) <= len(g[0]):
                if [g[i][found.start():len(p[0]) + found.start()] for i in range(g_i, len(p) + g_i)] == p:
                    return "YES"
    return "NO"


def utopian_tree(n):
    h = 1
    # debug_here()
    for i in range(n):
        if not i % 2:
            h *= 2
        else:
            h += 1

    return h
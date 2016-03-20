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


def grid_search(P, G):
    result = ""
    # debug_here()
    for G_i in range(len(G)):
        for found in re.finditer(P[0], G[G_i]):
            start_column = found.start()
            start_row = G_i
            result = "YES"
            for P_i in range(1, len(P)):

                if G[G_i + P_i].find(P[P_i]) == start_column:
                    result = "YES"
                else:
                    result = "NO"
                    break

    return result


def utopian_tree(n):
    h = 1
    # debug_here()
    for i in range(n):
        if not i % 2:
            h *= 2
        else:
            h += 1

    return h
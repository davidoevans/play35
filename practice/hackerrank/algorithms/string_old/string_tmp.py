from IPython.core.debugger import Tracer
debug_here = Tracer()


def can_be_palindrome(s):
    """
    :param s: string to be tested
    :return: "YES" or "NO"
    """
    ord_s = [ord(x) for x in s]
    while len(ord_s) > 0:
        # debug_here()
        if ord_s.count(max(ord_s) == len(s)):
            return "YES"

        count_max = ord_s.count(max(ord_s))
        if not count_max % 2 or ord_s.count(max(ord_s) == len(s)):
            ord_s = list(filter(max(ord_s).__ne__, ord_s))
            can_be_palindrome(ord_s)
        else:
            return "NO"


def cbp(s):
    """
    :param s: string to be tested
    :return: "YES" or "NO"
    """

    """ create list of ASCII values """
    ord_s = [ord(x) for x in s]
    odds = 0
    # debug_here()
    while len(ord_s) > 0:
        if ord_s.count(max(ord_s)) % 2:
            odds += 1

        # remove occurances of the max number
        ord_s = list(filter(max(ord_s).__ne__, ord_s))

    if odds <= 1:
        return "YES"
    else:
        return "NO"


def print_a_triangle(n):
    print("*" * (n+3))
    for i in range(n):
        print("{}{}{}".format("*", str(" ").rjust(n-i), "*"))

    print("*")


def intersect_w_dupes(x, y):
    """Find intesects of two lists.  Since lists can have duplicates, straight set logic won't suffice.

    Keyword arguments:
    x -- 1st list
    y -- 2nd list
    """

    """ Create dictionary of counts by value """
    x_dict = {i : x.count(i) for i in set(x)}
    y_dict = {i : y.count(i) for i in set(y)}

    """ Initialize total (and dict? of symmetric_intersections?) """
    tot = 0
    result_dict = {}

    """ Iterate over union of all keys """
    for i in (set(x_dict.keys()) | set(y_dict.keys())):
        if i in x_dict and i in y_dict:
                tot += abs(x_dict[i] - y_dict[i])
                result_dict[i] = tot
        elif i in x_dict:
            tot += x_dict[i]
            if i in result_dict:
                result_dict[i] += x_dict[i]
            else:
                result_dict = x_dict[i]
        else:
            tot += y_dict[i]
            result_dict[i] = tot

    return tot, result_dict




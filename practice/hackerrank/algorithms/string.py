def make_anagram(s):
    """
    Solve the `HackerRank Anagram Challenge <https://www.hackerrank.com/challenges/anagram>`_

    Divide a string into 2 strings and indicate the number of changes that need to be made to the first string
    to make it an anagram of the second string.

    :param s: input string
    :return:
    """
    if len(s) % 2:
        return -1
    else:
        x = s[0:int(len(s) / 2)]
        y = s[int(len(s) / 2):]
        xs = {i: x.count(i) for i in set(x)}
        ys = {i: y.count(i) for i in set(y)}

        """ calculate changes required """
        result = 0
        # debug_here()
        for i in ys:
            if i in xs:
                if xs[i] <= ys[i]:
                    result += ys[i] - xs[i]
            else:
                result += ys[i]

        return result

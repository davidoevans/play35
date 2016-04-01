def insertion_sort1(alist):
    """
    Solve the `Insertion Sort 2 Challenge <>`_
    """
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position -= 1
            print(' '.join(map(str, alist)))

        alist[position] = currentvalue

    print(' '.join(map(str, alist)))


def insertion_sort2(alist):
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index

        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = current_value
        print(' '.join(map(str, alist)))


def insertion_sort3(l):
    """
    This is the exact code taken from the https://www.hackerrank.com/challenges/correctness-invariant challenge.
    It works locally but fails on the site.  By simply replacing the algorithm on the site with one of the previous
    insertion_sort algorithms, it passes.

    Not sure why this passes locally but not on the site??

    :param l:
    :return:
    """
    for i in range(1, len(l)):
        j = i - 1
        key = l[i]
        while (j > 0) and (l[j] > key):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key


def running_time(alist):
    """
    Solve running time https://www.hackerrank.com/challenges/runningtime challenge.
    :param alist:
    :return: the number of times an item had to be shifted to complete the insertion sort algorithm
    """
    shifts = 0
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index

        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position -= 1
            shifts += 1

        alist[position] = current_value
    return shifts


def counting_sort3(l):
    """
    There's not a nice way to fit this into a list comprehension so am implementing as a generator.
    :param l:
    :return:
    """
    count = 0
    for x in range(0, 100):
        count += l.count(x)
        yield count

def quick_sort1(l):
    """
    Solve the first quick sort challenge.

    :param l:
    :return:
    """
    mid = [l[0]]
    left = []
    right = []
    for i in l[1:]:
        if i == l[0]:
            mid.append(i)
        elif i < l[0]:
            left.append(i)
        else:
            right.append(i)
    return " ".join(repr(e) for e in left + mid + right)


def quick_sort2(l):
    """
    Solve the second quick sort challenge.

    :param l:
    :return:
    """
    mid = []
    left = []
    right = []
    if len(l) > 1:
        mid.append(l[0])
        for i in l[1:]:
            if i == l[0]:
                mid.append(i)
            elif i < l[0]:
                left.append(i)
            else:
                right.append(i)
        left = quick_sort2(left)
        if len(left) > 1:
            print(" ".join(repr(x) for x in left))
        right = quick_sort2(right)
        if len(right) > 1:
            print(" ".join(repr(x) for x in right))
        return left + mid + right
    else:
        return l
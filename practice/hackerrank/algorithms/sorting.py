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

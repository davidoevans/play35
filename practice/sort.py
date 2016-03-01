from IPython.core.debugger import Tracer; debug_here = Tracer()


def insertion_sort(alist):
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


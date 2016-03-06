"""
Solve the `Insertion Sort 2 Challenge <>`_
"""

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

if __name__ == "__main__":
    n = int(input().split()[0])
    arr = list(map(int, input().split()))
    insertion_sort(arr)


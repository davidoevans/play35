"""
Solve the `Insertion Sort2 Challenge <https://www.hackerrank.com/challenges/insertionsort2>`_
"""
def insertion_sort2(alist):
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index

        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = current_value
        print(' '.join(map(str, alist)))

if __name__ == "__main__":
    n = input()
    l = list(map(int, input().split()))
    insertion_sort2(l)

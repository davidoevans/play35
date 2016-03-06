"""
Solve the `Utopian Tree Challenge https://www.hackerrank.com/challenges/utopian-tree`_
"""
from IPython.core.debugger import Tracer
debug_here = Tracer()


def utopian_tree(n):
    h = 1
    # debug_here()
    for i in range(n):
        if not i % 2:
            h *= 2
        else:
            h += 1

    return h


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(utopian_tree(n))
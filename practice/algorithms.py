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
"""
Demonstrate list comprehension
"""
def print_result(var):
    print("{} = {}".format(var, eval(var)))

if __name__ == "__main__":
    A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
    A1 = range(10)
    A2 = sorted([i for i in A1 if i in A0])
    A3 = sorted([A0[s] for s in A0])
    A4 = [i for i in A1 if i in A3]
    A5 = {i: i * i for i in A1}
    A6 = [[i, i * i] for i in A1]
    A7 = [i for s in [A1, A2, A3] for i in s]

    for i in ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']:
        print_result(i)

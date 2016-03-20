"""
Sovle the `Fibonacci Modified Challenge <https://www.hackerrank.com/challenges/fibonacci-modified>`_
"""
def fib_modified(data):
    result = [data[0]]
    a, b = data[0], data[1]
    for i in range(data[2] - 1):
        result.append(b)
        a, b = b, b ** 2 + a

    return result[len(result) - 1]

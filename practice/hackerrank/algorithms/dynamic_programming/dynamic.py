"""
Sovle the `Fibonacci Modified Challenge <https://www.hackerrank.com/challenges/fibonacci-modified>`_
"""
def fib_modified(n):
    result = [0]
    a, b = 0, 1
    for i in range(n - 1):
        result.append(b)
        a, b = b, b ** 2 + a

    return result


if __name__ == "__main__":
    input = list(map(int, input().split(' ')))

    result = [input[0]]
    a, b = input[0], input[1]
    for i in range(input[2] - 1):
        result.append(b)
        a, b = b, b ** 2 + a

    print(result[len(result) - 1])

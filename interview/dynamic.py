def fib_modified(n):
    result = [0]
    a, b = 0, 1
    for i in range(n - 1):
        result.append(b)
        a, b = b, b ** 2 + a

    return result

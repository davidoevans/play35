import random
import math
import itertools


def decent_number(n):
    if n < 10:
        set_of_threes = ['33333' * (i+1) for i in range(int(n/5))]
        set_of_fives = ['555' * (i+1) for i in range(int(n/3))]
        options = map(''.join, itertools.chain(itertools.product(set_of_threes, set_of_fives), itertools.product(set_of_fives, set_of_threes)))
        full_set = [int(x) for x in set_of_threes if len(x) == n]
        full_set = full_set + list([int(x) for x in set_of_fives if len(x) == n])
        full_set = full_set + list([int(x) for x in options if len(x) == n])
        if len(full_set) == 0:
            return -1
        elif len(full_set) > 1:
            return max(full_set)
        else:
            return full_set[0]
    else:
        # from discussion board
        z = n
        while z % 3 != 0:
            z -= 5
            if z < 0:
                return -1
            else:
                return int(z * '5' + (n-z) * '3')


def decent_number2(n):
    z = n
    while z % 3 != 0:
        z -= 5
        if z < 0:
            print(-1)
        else:
            print(z * '5' + (n-z) * '3')




def isolve(a, b, c):
    q, r = divmod(a, b)
    if r == 0:
        return [0, c/b]
    else:
        sol = isolve(b, r, c)
        u = sol[0]
        v = sol[1]
        return [v, u-q*v]


def numbers_in_sum(n, s):
    result = n
    remainder = s - result
    if remainder == 0:
        return result
    elif decent_number(remainder) in [3, 5]:
        return result + decent_number(remainder)


def pollardRho(N):
    if N%2 == 0:
        return 2

    x = random.randint(1, N-1)
    y = x
    c = random.randint(1, N-1)
    g = 1
    while g==1:
        x = ((x*x)%N+c)%N
        y = ((y*y)%N+c)%N
        y = ((y*y)%N+c)%N
        g = math.gcd(abs(x-y), N)

    return g


def factor(n):
    if n == 1:
        return None
    return n ** 1 / pollardRho(n)


def factors(n):
    possibles = [[pollardRho(x), factor(x)] for x in reversed(range(n)) if x > 1.0]
    likly = [x for x in possibles if x[0] in [3, 5]]
    return likly


def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)


def is_funny(s):
    r = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
            return "Not Funny"

    return "Funny"


def count_deletes(x):
    d = 0
    p = 0
    for i in range(1, len(x)):
        print(p, x[p], i-1, x[i-1])
        if x[i] == x[i-1]:
            d += 1
        else:
            p = i + 1

    return d

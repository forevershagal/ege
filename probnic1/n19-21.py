from functools import lru_cache

lru_cache(None)


def f(a, b, cnt=0):
    if a + b >= 205:
        return 0
    if cnt > 6:
        return 10 ** 5

    moves = []
    if a > b:
        moves = [f(a, b + a, cnt + 1), f(a, b * 2, cnt + 1)]
    else:
        moves = [f(a + b, b, cnt + 1), f(a * 2, b, cnt + 1)]

    n = [g for g in moves if g <= 0]
    if n:
        return -max(n) + 1
    return -max(moves)


for i in range(1, 197):
    if f(9, i) == -2:
        print(i)

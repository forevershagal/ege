from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10**9)
@lru_cache(maxsize=None)
def F(n):
    if n >= 21:
        return F(n-8) + 1095
    else:
        return 10 * (G(n-7) - 36)

@lru_cache(maxsize=None)
def G(n):
    if n >= 22560:
        return n / 23 + 33
    else:
        return G(n+11)-4


print(F(548))

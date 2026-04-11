from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(2000)

@lru_cache
def f(n):
    if n == 1:
        return 1
    elif n > 2 and n % 2 == 0:
        return 2*n * f(n-1) + f(n-3)
    elif n > 2 and n%2 != 0:
        return f(n-2) * 3

for i in range(1, 5000):
    f(i)

print(f(2026)/f(2021))

from functools import *


@lru_cache(None)
def f(n):
    if n == 1:
        return 4
    return 4 * f(n - 1)


for i in range(1, 10 ** 5):
    f(i)

print(f(4040) // (2 ** 8059))

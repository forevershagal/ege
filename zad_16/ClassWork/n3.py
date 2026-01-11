from functools import *


@lru_cache(None)
def f(n):
    if n < 0:
        return 2
    elif n % 3 == 0:
        return 9 * n + f(n - 3)
    return n + f(n - 1)


for i in range(11000):
    f(i)

print(f(10344) - f(10342))

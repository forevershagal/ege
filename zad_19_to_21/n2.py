from functools import *


@lru_cache(None)
def f(a, b):
    #Если сумма камней в кучах стало больше 43
    if a + b >= 43:
        #Прекращаем игру
        return 0
    t = [f(a + 2, b), f(a * 3, b), f(a, b + 2), f(a, b * 3)]
    n = [i for i in t if i <= 0]
    if n:
        # Выигрышный ход Пети
        return -max(n) + 1
    # Выигрышный ход Вани
    else:
        return -max(t)


for s in range(1, 37):
    if f(6, s) == -2:
        print(s)

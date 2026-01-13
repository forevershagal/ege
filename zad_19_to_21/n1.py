from functools import lru_cache


@lru_cache(None)
def f(a):
    # Если камней в куче стало больше 38
    if a >= 39:
        # прекращаем игру
        return 0
    t = [f(a + 1), f(a+2), f(a * 2)]
    n = [i for i in t if i <= 0]
    # Проверяем, есть ли выигрыш Пети в данной позиции
    if n:
        return -max(n) + 1
    # Если в данной позиции выигрыш Вани
    return -max(t)


for i in range(1, 38):
    if f(i) == -2:
        print(i)

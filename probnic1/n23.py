def f(x, y):
    if x < y:
        return 0
    elif x == y:
        return 1
    else:
        return f(x-3, y) + f(x-5, y) + f(x // 3, y)

print(f(86, 35) * f(35, 14) * f(14, 4))
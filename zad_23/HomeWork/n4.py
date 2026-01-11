def f(a, b, c=0):
    if (a > b) or (a == 11) or (a == 14):
        return 0
    if a == 17:
        c += 1
    if a == b:
        return c
    return f(a + 1, b, c) + f(a * 2, b, c) + f(a * 3, b, c)


print(f(1, 32))

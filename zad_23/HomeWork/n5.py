def f(a, b, c=0):
    if (a > b) or (a == 10):
        return 0
    if a == b:
        return c
    if a == 8:
        c += 1
    return f(a + 1, b, c) + f(a * 2, b, c) + f(a + 5, b, c)


print(f(1, 16))

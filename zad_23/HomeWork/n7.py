def f(a, b, c=0):
    if a > b or a == 14:
        return 0
    if a == b:
        return c
    if a == 10:
        c += 1
    return f(a + 1, b, c) + f(a + 2, b, c) + f(a * 3, b, c)


print(f(2, 15))

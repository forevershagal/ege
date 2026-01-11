def f(a, b, c=0):
    if (a > b) or (a == 40):
        return 0
    if a == 16:
        c = 1
    if a == b:
        return c
    return f(a + 1, b, c) + f(a * 3, b, c)

print(f(1, 60))

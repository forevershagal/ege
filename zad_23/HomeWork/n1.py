def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a + 2, b) + f(4 * a, b)


print(f(2, 17))

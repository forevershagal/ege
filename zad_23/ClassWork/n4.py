def f(a, b, c=0):
    if a > b:
        return 0
    if a == 9 or a == 11:
        c += 1
    if a == b:
        return c // 2
    return f(a + 1, b, c) + f(a + 2, b, c) + f(a * 2, b, c)


print(f(3, 13))

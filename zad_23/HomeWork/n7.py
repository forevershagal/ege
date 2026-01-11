def f(a, b, c=0):
    if a > b or a == 19:
        return 0
    if a == b:
        return 1
    if a == 10:
        c += 1
    return f(a + 1, b, c) + f(a + 2, b, c) + f(a * 3, b, c)


print(f(2, 15))

def f(a, b, c=0):
    if a > b or (a == 13) or (a == 18):
        return 0
    if a == 11:
        c += 1
    if a == b:
        return c

    return f(a + 4, b, c) + f(a + 5, b, c) + f(a * 2, b, c)


print(f(3, 23))


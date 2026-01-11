def f(a, b, c=0):
    if a > b or a == 16:
        return 0
    if a == b:
        return 1
    if a == 14:
        c += 1
    return f(a + 1, b, c) + f(a * 2, b, c) + f(a * 3, b, c)


print(f(1, 50))

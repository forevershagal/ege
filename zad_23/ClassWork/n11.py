def f(a, b, c=0):
    if a > b:
        return 0
    if a == b:
        return 1
    if c < 2:
        return f(a+1, b, c) + f(a+2, b, c) + f(a*2, b, c+1) + f(a*4, b, c+1)
    else:
        return f(a + 1, b, c) + f(a + 2, b, c)
print(f(1, 13, 0))
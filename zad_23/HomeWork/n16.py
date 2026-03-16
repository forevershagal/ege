def f(a, b, c=0):
    if a > b or a < 1:
        return 0
    if a == b:
        return 1
    o1 = 0
    if c < 1:
        o1 = f(a-1, b, c+1)
    return o1 + f(a*2, b, 0) + f(a*3, b, 0)
print(f(3, 15, 0))

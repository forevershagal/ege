def f(a, b, c1=0):
    if a > b:
        return 0
    if a == b:
        return 1
    o2 = 0
    if c1 < 1:
        o2 = f(a+2, b, c1+1)
    return f(a+1, b, 0) + o2 + f(a*2, b, 0)
print(f(2, 22))

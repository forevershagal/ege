def f(a, b, f1=0, f2=0):
    if a > b:
        return 0
    if a == b:
        return 1
    o1 = o2 = 0
    if f1 < 2:
        o1 = f(a+1, b, f1+1, 0)
    if f2 < 2:
        o2 = f(a*2, b, 0, f2+1)
    return o1 + o2
print(f(1, 14))
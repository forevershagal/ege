def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+1, b) + f(a+5, b) + f(a*2, b)
print(f(4, 11) * f(11, 17) * f(17, 24))
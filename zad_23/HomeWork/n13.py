def f(a, b):
    if a > b or a == 10:
        return 0
    if a == b:
        return 1
    return f(a+1, b) + f(a*2, b) + f(a+5, b)
print(f(1, 8) * (f(8, 16)))
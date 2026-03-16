def f(a, b, f1, f2):
    if a < b:
        return 0
    if a == 14:
        f1 = 1
    if a == 35:
        f2 = 1
    if a == b:
        return f1 * f2
    return f(a-3, b, f1, f2) + f(a-5, b, f1, f2) + f(a//3, b, f1, f2)
print(f(68, 4, 0, 0))
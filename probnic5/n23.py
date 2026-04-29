def f(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    else:
        return f(a-1, b) + f(a-4, b) + f(a//2, b)
print(f(60, 56) * f(56, 30) * f(30, 18) * f(18, 10))
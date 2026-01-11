def f(n):
    if n <= 2:
        return 1
    return f(n - 1) * n + f(n - 5) * 5


print(f(15))

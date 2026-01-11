def f(n):
    if n <= 5:
        return n - 1
    return f(n - 1) * f(n - 1) - g(n - 4) - 2


def g(n):
    if n <= 5:
        return n - 4
    return g(n - 3) * g(n - 3) - f(n - 4) + 2


print(f(9))

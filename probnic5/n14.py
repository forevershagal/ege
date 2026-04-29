def f(x):
    s = ''
    while x > 0:
        s = str(x%4) + s
        x //= 4
    return s

a = 4**2023 + 4**115 - 3 * 4 ** 523 - 2378
print(f(a).count('3'))
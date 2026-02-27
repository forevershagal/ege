n = 6 ** 2020 + 36 ** 34 - 216 ** 12

def f(x):
    s = ''
    while x > 0:
        s = str(x%6) + s
        x //= 6
    return s

print(f(n).count('5'))
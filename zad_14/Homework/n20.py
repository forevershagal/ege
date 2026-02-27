n = 49 ** 12 + 7 ** 10 - 28

def f(x):
    s = ''
    while x > 0:
        s = str(x%7) + s
        x //= 7
    return s

print(f(n).count('0'))
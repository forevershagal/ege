n = 25 ** 20 + 4 * 5**11 - 2

def f(x):
    s = ''
    while x > 0:
        s = str(x%5) + s
        x //= 5
    return s

print(f(n).count('3'))
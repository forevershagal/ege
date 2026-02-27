n = 11 ** 6 + 11 ** 11 - 34

def f(x):
    alf = '0123456789A'
    s = ''
    while x > 0:
        s = alf[x%11] + s
        x //= 11
    return s

print(f(n).count('0'))
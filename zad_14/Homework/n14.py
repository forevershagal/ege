n = 25**20 + 5**15 - 125**3

def f(x):
    s = ''
    while x > 0:
        s = str(x%5) + s
        x //= 5
    return s

print(f(n).count('4'))
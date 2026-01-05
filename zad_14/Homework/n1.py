x = 25 ** 20 + 4 * 5 ** 11 - 2

s = ''

while x > 0:
    s = str(x % 5) + s
    x = x // 5

print(s.count('3'))
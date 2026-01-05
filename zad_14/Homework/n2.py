x = 6 * 343 ** 6 + 5 * 49**7 - 40

s = ''

while x > 0:
    s = str(x % 7) + s
    x = x // 7

print(s.count('6'))
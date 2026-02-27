x = 5 * 216 ** 6 + 3 * 36 ** 4 - 10
s = ''
while x > 0:
    s = str(x%6) + s
    x //= 6
print(s)
print(s.count('5'))
x = 8 ** 190 + 8 ** 100 - 64 ** 3
s = ''
while x > 0:
    s = str(x%8) + s
    x //= 8
print(s)
print(s.count('0'))
x = 5 ** 14 + 25 ** 3 - 117

s = ''
while x > 0:
    s = str(x%5) + s
    x //= 5
print(s)
print(s.count('4'))
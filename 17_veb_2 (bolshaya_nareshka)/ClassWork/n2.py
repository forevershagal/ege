def b7(x): # функция для перевода числа в семеричную СИ
    s = ''
    while x > 0:
        s = str(x % 7) + s
        x //= 7
    return s

f = open()
a = [int(i) for i in f]

mk63 = max([i for i in a if i % 63 == 0])
c = 0
mn = 10000000000000000000000000000000
for i in range(len(a) - 1):
    if ((a[i] + a[i+1]) > mk63) and (('55' in b7(a[i])) or ('55' in b7(a[i]))):
        c += 1
        mn = min(mn, abs(a[i]) + abs(a[i+1]))

print(c, mn)
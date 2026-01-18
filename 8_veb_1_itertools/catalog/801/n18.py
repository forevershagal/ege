from itertools import product

alf = product('ВДЗЕА', repeat=6)
c = 0
for i in alf:
    s = ''.join(i)
    c += 1
    if s == 'ЗВЕЗДА':
        print(c)
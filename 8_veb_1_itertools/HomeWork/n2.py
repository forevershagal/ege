from itertools import product

c = 0
for x in product('МЫШИ', repeat=7):
    s = ''.join(x)
    if 'МЫШ' in s:
        c += 1

print(c)
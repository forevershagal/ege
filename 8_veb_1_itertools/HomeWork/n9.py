from itertools import product

c = set()

for x in product('УСПЕХ', repeat=6):
    s = ''.join(x)
    if s.count('У') >= 2:
        c.add(s)

print(len(c))
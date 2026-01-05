from itertools import product

c = set()

for x in product('ЦИФРА', repeat=5):
    s = ''.join(x)
    if s[0] not in 'ИА':
        c.add(s)

print(len(c))
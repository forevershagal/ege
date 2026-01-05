from itertools import product

c = set()

for x in product('ABCDE', repeat=4):
    s = ''.join(x)
    c.add(s)

print(len(c))
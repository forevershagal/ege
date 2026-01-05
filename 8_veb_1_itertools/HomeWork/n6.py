from itertools import permutations

c = set()

for x in permutations('БАОБАБ', 6):
    s = ''.join(x)
    c.add(s)

print(len(c))
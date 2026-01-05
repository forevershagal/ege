from itertools import permutations

c = set()
for x in permutations('НАПИТОК', 7):
    s = ''.join(x)
    if s[-1] == 'П':
        c.add(s)

print(len(c))
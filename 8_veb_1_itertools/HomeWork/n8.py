from itertools import permutations

c = set()

for x in permutations('ABCD', 3):
    s = ''.join(x)
    c.add(s)

print(len(c))
from itertools import *

alf = product('РЕЦПТ', repeat=6)
c = 0
for i in alf:
    s = ''.join(i)
    c += 1

print(c)
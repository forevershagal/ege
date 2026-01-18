from itertools import *

alf = product('МЩНО', repeat=5)
c = 0
for i in alf:
    s = ''.join(i)
    c += 1
    if s == 'МОЩНО':
        print(c)
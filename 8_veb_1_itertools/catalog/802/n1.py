from itertools import *

alf = product('АБВГД', repeat=5)
c = 0
for i in alf:
    s = ''.join(i)
    c += 1

print(c)
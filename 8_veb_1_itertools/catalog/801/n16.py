from itertools import *

alf = product('АНМШИ', repeat=6)
c = 0
for i in alf:
    s = ''.join(i)
    c += 1
    if s == 'МАШИНА':
        print(c)
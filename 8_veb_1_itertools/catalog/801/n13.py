from itertools import *

alf = product('ЯМРВЕ', repeat=5)
c = 0
for i in alf:
    s = ''.join(i)
    c += 1
    if s == 'ВРЕМЯ':
        print(c)
from itertools import *

alf = product('ЗАИТК', repeat=6)
c = 0
for i in alf:
    s = ''.join(i)
    c += 1
    if s == 'АЗАТИК':
        print(c)
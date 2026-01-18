from itertools import *

alf = permutations('ПРАВНУК',7)
c = 0
for i in alf:
    s = ''.join(i)
    if s[0] == 'П' and s[-1] == 'Р':
        c += 1

print(c)
from re import *

s = r'aaaa0123+456-7894aaaa567+0+789aaa'

d = r'(0|[1-9][0-9]*)'
p = rf'{d}([+-]{d})+'

for i in finditer(p, s):
    res = i.group()
    print(res)
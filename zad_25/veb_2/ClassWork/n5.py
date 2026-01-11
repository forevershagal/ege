from fnmatch import *

for x in range(0, 10**10, 12345):
    s = str(x)
    if fnmatch(s, '21?498*4*'):
        print(x, x // 12345)
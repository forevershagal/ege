from fnmatch import *

for x in range(0, 10**7+1, 387):
    s = str(x)
    if fnmatch(s, '*16*9?0?'):
        print(x)
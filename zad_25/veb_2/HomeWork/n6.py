from fnmatch import *

for x in range(0, 10**12 + 1, 178750):
    s = str(x)
    if fnmatch(s, '137?15*7*50'):
        print(x, x // 178750)

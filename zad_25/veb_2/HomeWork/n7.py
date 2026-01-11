from fnmatch import *

for x in range(0, 10**9+1, 4215):
     s = str(x)
     if fnmatch(s, '?4?8*15?5'):
         print(x, x // 4215)
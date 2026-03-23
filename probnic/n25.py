from fnmatch import *

for i in range(0, 10**9, 9341):
    if fnmatch(str(i), '4?5*07*3'):
        print(i)
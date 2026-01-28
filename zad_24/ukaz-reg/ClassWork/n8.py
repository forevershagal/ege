from re import *
from string import *

f = open('D:/INF_tasks/task24_ukaz-reg/8.txt')
s = f.readline()

p = '(ABCD)+(ABCD|ABC|AB|A)*'

mx = 0

for i in finditer(p, s):
    res = i.group()
    mx = max(mx, len(res))
print(mx)
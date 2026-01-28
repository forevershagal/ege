from re import *
from string import *

f = open('D:/INF_tasks/task24_ukaz-reg/7.txt')
s = f.readline()

p = 'C[QWERTYUIOPASFGHJKLZXVBNM]*D'

mx = 0

for i in finditer(p, s):
    res = i.group()
    mx = max(mx, len(res))
print(mx)
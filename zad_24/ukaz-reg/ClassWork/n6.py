from re import *

f = open('D:/INF_tasks/task24_ukaz-reg/6.txt')
s = f.readline()
mx = 0
p = '(0|[1-7][0-7]*)([+*](0|[1-7][0-7]*))+'

for i in finditer(p, s):
    res = i.group()
    mx = max(mx, len(res))
print(mx)
from re import *

f = open('D:/INF_tasks/task24_reg/1.txt')
s = f.readline()

p = '-{0,1}[1-9]+([+-][1-9]+)+'
mx = 0
for i in finditer(p, s):
    res = i.group()
    print(res)
    mx = max(mx, len(res))

print(mx)
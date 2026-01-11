from re import *
f = open('D:/INF_tasks/task24_reg/24__7h55c.txt')
s = f.readline()
mx = 0

p = 'B[1-6]+([-*][1-6]+)+'

for i in finditer(p, s):
    res = i.group()
    print(res)
    mx = max(mx, len(res))

print(mx)

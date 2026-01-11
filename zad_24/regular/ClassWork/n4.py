from re import *
f = open('D:/INF_tasks/task24_reg/4.txt')
s = f.readline()
mx = 0

p = '[1-9][0-9]*[02468],[1-9][0-9]*[13579]'

for i in finditer(p, s):
    res = i.group()
    print(res)
    mx = max(mx, len(res))
print(mx)
from re import *
f = open('D:/INF_tasks/task24_reg/24_2__7bozs.txt')
s = f.readline()
mx = 0

p = '0|[6-9][06-9]*([-+](0|[6-9][06-9]*))*'

for i in finditer(p, s):
    res = i.group()
    mx = max(mx, len(res))

print(mx)

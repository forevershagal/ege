from re import *

f = open('D:/INF_tasks/task24_reg/Задание_24__7blrn.txt')
s = f.readline()
mx = 0

p = '[1-9A-D][0-9A-D]*[02468AC]'

for i in finditer(p, s):
    res = i.group()
    mx = max(mx, len(res))

print(mx)

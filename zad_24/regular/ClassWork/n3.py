from re import *

f = open('D:/INF_tasks/task24_reg/3.txt')
s = f.readline()
mx = 0

p = '[2468]+([+][2468]+)+'

for i in finditer(p, s):
    res = i.group()
    if eval(res) > mx:
        mx = eval(res)
        st = res

print(mx, st)
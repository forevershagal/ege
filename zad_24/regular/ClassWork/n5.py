from re import *

f = open('D:/INF_tasks/task24_reg/5.txt')
s = f.readline()
mx = 0

p = '(0|[2468][02468]*00)([-/](0|[2468][02468]*00)){1,10}'

for i in finditer(p, s):
    res = i.group()
    mx = max(mx, len(res))
    print(res)

print(mx)
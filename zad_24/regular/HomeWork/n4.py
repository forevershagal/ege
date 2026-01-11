from re import *
s = open('D:/INF_tasks/task24_reg/demo_2025_24__7ae4q.txt').readline()
mx = 0

p = '0|[6-9][06-9]*([-*](0|[6-9][06-9]*))*'

for i in finditer(p, s):
    res = i.group()
    print(res)
    mx = max(mx, len(res))

print(mx)


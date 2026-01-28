from re import *
f = open('D:/INF_tasks/task24_ukaz-reg/2.txt')
s = f.readline()

p = '([B-D][AE][B-D])+'
mx = 0
for i in finditer(p, s):
    res = i.group()
    mx = max(mx, len(res))

print(mx // 3)
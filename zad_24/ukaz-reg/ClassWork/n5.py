from re import *

f = open('D:/INF_tasks/task24_ukaz-reg/5.txt')
s = f.readline()

p = 'A[1-4]+([+*][1-4]+)+'

mx = 0
for i in finditer(p, s):
    res = i.group()
    mx = max(mx, len(res))

print(mx)

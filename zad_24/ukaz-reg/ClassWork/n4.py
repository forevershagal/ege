from re import *

f = open('D:/INF_tasks/task24_ukaz-reg/4.txt')
s = f.readline()

p = '[-]{0,1}[1-9]+([+-][1-9]+)+'
mx = 0
for i in finditer(p, s):
    res = i.group()
    mx = max(mx, len(res))

print(mx)
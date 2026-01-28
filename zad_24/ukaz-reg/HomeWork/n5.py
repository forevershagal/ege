from re import *

f = open('D:/INF_tasks/task24_ukaz-reg/24_1__7boxw.txt')
s = f.readline()

mx = 0
p = '(0|[1234][01234]*)([-+](0|[1234][01234]*))+'

for i in finditer(p, s):
    res = i.group()
    mx = max(mx, len(res))
print(mx)
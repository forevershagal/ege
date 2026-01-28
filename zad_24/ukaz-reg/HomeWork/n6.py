from re import *
mx = 0

f = open('D:/INF_tasks/task24_ukaz-reg/Задание_24__7ajcf.txt')
s = f.readline()

p = '([CDF][AO])+'

for i in finditer(p, s):
    res = i.group()
    print(res)
    mx = max(mx, len(res) // 2)
print(mx)
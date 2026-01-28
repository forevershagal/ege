from re import *
f = open('D:/INF_tasks/task24_ukaz-reg/1.txt')
s = f.readline()
s = s.replace('CD', 'CxD')
p = '(?=([A-E]*(CxD[A-E]*){50}))'
mx = 0
for i in finditer(p, s):
    res = i.group(1)
    mx = max(mx, len(res))
print(mx-50)
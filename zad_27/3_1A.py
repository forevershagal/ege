from math import dist
from turtle import *

f = open('D:/INF_tasks/27_dz_dbscan/27_A__8vcrw.txt')
s = f.readline()
a = [list(map(float, i.replace(',', '.').split())) for i in f]
clusters = [[] for j in range(2)]

for x, y in a:
    if x < 45:
        clusters[0].append((x, y))
    else:
        clusters[1].append((x, y))

# Суммы абсцисс и ординат центров каждого кластера
p = [0, 0]
for i in range(len(clusters)):
     mn = 10**20
     center = (0, 0)
     for j in clusters[i]:
         s = 0
         for star in clusters[i]:
             s += dist(star, j)
         if s < mn:
            mn = s
            center = j
     p[i] = sum(center)

if len(clusters[1]) < len(clusters[0]):
    p[0], p[1] = p[1], p[0]
print(int(abs(p[0]*10000)), int(abs(p[1]*10000)))


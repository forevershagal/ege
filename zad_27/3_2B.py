from math import dist
from turtle import *


f = open('D:/INF_tasks/27_dz_dbscan/27Б__7rojd.txt')
l = f.readline()
a = [list(map(float, i.replace(',', '.').split())) for i in f]

clusters = [[] for i in range(3)]

for x, y in a:
    if x > 4:
        clusters[0].append([x, y])
    elif y > 2.2:
        clusters[1].append([x, y])
    else:
        clusters[2].append([x, y])

px = py = 0

for cl in clusters:
    mn = 10**20
    centroid = []
    for center in cl:
        s = 0
        for star in cl:
            s += dist(star, center)
        if s < mn:
            mn = s
            centroid = center
    px += centroid[0]
    py += centroid[1]

print(int(px/3*10000), int(py/3*10000))
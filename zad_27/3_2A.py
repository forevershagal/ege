from math import dist
from turtle import *

f = open('D:/INF_tasks/27_dz_dbscan/27А__7rojb.txt')
l = f.readline()
a = [list(map(float, i.replace(',', '.').split())) for i in f]

clusters = [[] for i in range(2)]

for x, y in a:
    if x < 3:
        clusters[0].append(([x, y]))
    else:
        clusters[1].append(([x, y]))

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

print(int(px/2*10000), int(py/2*10000))


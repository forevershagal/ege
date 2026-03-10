from math import dist
from math import sqrt
from turtle import *



f = open('D:/INF_tasks/27_dz_dbscan/27_B__8vcrx.txt')
l = f.readline()
a = [list(map(float, i.replace(',', '.').split())) for i in f]

clusters = [[] for i in range(3)]

for x, y in a:
    if 19 < x < 29:
        if y < 32:
            clusters[0].append((x, y))
        elif y > 42:
            clusters[1].append((x, y))
        else:
            clusters[2].append((x, y))

farthest = (0, 0)
closest = (0, 0)
max_dist = 0
mn_dist = 10**20

for i in range(len(clusters)):
    center = (0, 0)
    mn = 10**20
    for j in clusters[i]:
        s = 0
        for star in clusters[i]:
            s += dist(star, j)
        if s < mn:
            mn = s
            center = j
    distance = dist((0, 0), center)
    if distance > mn_dist:
        mn_dist = distance
        closest = center
    if distance > max_dist:
        max_dist = distance
        farthest = center

print(int(abs(farthest[0] * 10000)), int(abs(closest[0] * 10000)))

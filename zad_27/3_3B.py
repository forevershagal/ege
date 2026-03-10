from math import dist
from turtle import *

f = open('smth')
l = f.readline()
a = [list(map(float, i.replace(',', '').split())) for i in f]
clusters = [[] for i in range(5)]

for x, y in a:
    if (-10/7) * x + 340 / 7 < y:
        clusters[0].append([x, y])
    elif ((-10/ 7) * x + 340 / 7 > y) and ((8 / 3) * x - 80 / 3 > y) and (y < 8):
        clusters[1].append([x, y])
    elif ((-10 / 7) * x + 340 / 7 > y) and ((8 / 3) * x - 80 / 3 > y) and (y > 9):
        clusters[2].append([x, y])
    elif y < 15:
        clusters[3].append([x, y])
    else:
        clusters[4].append([x, y])

sx = sy = 0
for cl in clusters:
    mn = 10**20
    centroid = []
    for center in cl:
        s = 0
        for star in cl:
            s += dist(center, star)
        if s < mn:
            mn = s
            centroid = center
    sx += centroid[0]
    sy += centroid[1]

px = sx / len(clusters)
py = sy / len(clusters)

print(int(px*100), int(py*100))



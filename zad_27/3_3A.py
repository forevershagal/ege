from math import dist
from turtle import *

f = open('smth')
l = f.readline()
a = [list(map(float, i.replace(',', '.').split())) for i in f]
clusters = [[] for i in range(6)]

for x, y in a:
    if (0.48 * x + 7.6 > y ) and (y > 13):
        clusters[0].append([x, y])
    elif 0.48 * x + 7.6 > y and x > 20:
        clusters[1].append([x, y])
    elif 0.48 * x + 7.6 > y and x < 15:
        clusters[2].append([x, y])
    elif x > 20:
        clusters[3].append([x, y])
    elif x < 7:
        clusters[4].append([x, y])
    else:
        clusters[5].append([x, y])

px = py = 0
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



            

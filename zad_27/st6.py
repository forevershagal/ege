# Для файла А
from math import dist
from turtle import *
tracer(0), pu()
m = 20
f = open('/Users/shagal/Downloads/27_А__8t1w7.txt')
stars = [list(map(float, i.replace(',', '.').split())) for i in f]
clusters = [[] for i in range(3)]
for star in stars:
    if star[1] > star[0] - 12:
        clusters[0].append(star)
    elif star[1] < -6:
        clusters[2].append(star)
    else:
        clusters[1].append(star)

centers = []
px = py = 0
for cluster in clusters:
    mx = 10**20
    centroid = cluster[0]
    for center in cluster:
        s = 0
        for star in cluster:
            s += dist(center, star) ** 2
        if s < mx:
            mx = s
            centroid = center
    px += centroid[0]
    py += centroid[1]
    centers.append(centroid)

ans1 = int(abs(px / len(clusters)) * 10000)
ans2 = int(abs(py / len(clusters)) * 10000)
print(ans1, ans2)


# Для файла Б
from math import dist
from turtle import *
tracer(0), pu()
m = 10


def dscan(point, r):
    clusters = []
    while points:
        clusters.append([points.pop(0)])
        for point in clusters[-1]:
            for neighbor in points[:]:
                if dist(point, neighbor) < r:
                    clusters[-1].append(neighbor)
                    points.remove(neighbor)
    return clusters

f = open('/Users/shagal/Downloads/27_Б__8t1w9 (1).txt')
r = 1.2
points = [list(map(float, i.replace(',', '.').split())) for i in f]
clusters = dscan(points, r)

centers = []
px = py = 0
for cluster in clusters:
    mx = 10**20
    centroid = []
    for center in cluster:
        s = 0
        for star in cluster:
            s += dist(center, star) ** 2
        if s < mx:
            mx = s
            centroid = center
    centers.append(centroid)
    px += centroid[0]
    py += centroid[1]
ans1 = int(abs(px/len(clusters)) * 10000)
ans2 = int(abs(py/len(clusters)) * 10000)
print(ans1, ans2)










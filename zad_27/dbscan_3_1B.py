from math import dist
from math import sqrt
from turtle import *

def dbscan(a, r):
    cl = []
    while a:
        cl.append([a.pop(0)])
        for i in cl[-1]:
            for j in a[:]:
                if dist(i, j) <= r:
                    cl[-1].append(j)
                    a.remove(j)
    return cl

def dist_to_zero(point):
    return sqrt(point[0]**2 + point[1]**2)


f = open('D:/INF_tasks/27_dz_dbscan/27_B__8vcrx.txt')
l = f.readline()
a = [list(map(float, i.replace(',', '.').split())) for i in f]
r = 15
clusters_raw = dbscan(a, r)
clusters = [i for i in clusters_raw if len(i) > 5]
centers = []

for i in clusters:
    mn = 10000000000000000
    for star in i:
        s = 0
        for j in i:
            s += dist(star, j)
        if s < mn:
            mn = s
            center = star
    centers.append(center)

far_center = max(centers, key=dist_to_zero)
qx = far_center[0]

near_center = min(centers, key=dist_to_zero)
qy = near_center[1]

print(int(abs(qx*10000)), int(abs(qy*10000)))


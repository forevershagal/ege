from math import dist
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


f = open('D:/INF_tasks/27_dz_dbscan/27_A__8vcrw.txt')
s = f.readline()
a = [list(map(float, i.replace(',', '.').split())) for i in f]
r = 4
clusters = dbscan(a, r)
centers = []



for i in clusters:
    mn = 1000000000000000000000
    for star in i:
        s = 0
        for j in i:
            s += dist(star, j)
        if s < mn:
            mn = s
            center = star
            centers.append(center)





# tracer(0)
# m = 4
# pu()
# for j in clusters:
#     for i in j:
#         x, y = i
#         goto(x*m, y*m)
#         dot(5)
# done()
#
# for j in centers:
#     for i in j:
#         x, y = i
#         goto(x*m, y*m)
#         dot(20, 'red')
# done()
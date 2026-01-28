from math import dist
from turtle import *

f = open('D:/INF_tasks/task27_dbscan/1.txt')
t = f.readline()
a = [list(map(float, i.replace(',', '.').split())) for i in f]

clusters = []
r = 0.2

while a:
    clusters.append([a.pop(0)])
    for j in clusters[-1]:
        for i in a[:]:
            if dist(i, j) <= r:
                clusters[-1].append(i)
                a.remove(i)

px = py = 0
for i in clusters:
    if len(i) > 5:
        mn = 10000000000000000000
        for star in i:
            s = 0
            for j in i:
                s += dist(star, j)
            if s < mn:
                mn = s
                center = star
        px += center[0]
        py += center[1]

print(int(px/4 * 100), int(py/4 * 100))
# tracer(100)
# m = 20
# pu()
# for j in clusters:
#     if len(j) > 5:
#         for i in j:
#             x, y = i
#             goto(x*m, y*m)
#             dot(5)
# done()




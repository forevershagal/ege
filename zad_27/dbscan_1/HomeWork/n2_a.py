from math import dist
from turtle import *

f = open('D:/INF_tasks/tasks27_dbscan_dz/2_A__5qgu0.txt')
t = f.readline()
a = [list(map(float, i.replace(',', '.').split())) for i in f]

clusters = []
m = 20
r = 0.2

while a:
    clusters.append([a.pop(0)])
    for j in clusters[-1]:
        for i in a[:]:
            if dist(i, j) <= r:
                clusters[-1].append(i)
                a.remove(i)
px = py = cnt = 0
for j in clusters:
    if len(j) > 5:
        x_coords = [point[0] for point in j]
        width = max(x_coords) - min(x_coords)
        if width < 4:
            cnt += 1
            mn = 1000000000000000000
            for star in j:
                s = 0
                for i in j:
                    s += dist(star, i)
                if s < mn:
                    mn = s
                    center = star
            px += center[0]
            py += center[1]
print(int(abs(px)/3 * 1000), int(abs(py)/3 * 1000))

pu()
tracer(0)
for j in clusters:
    if len(j) > 5:
        for i in j:
            x, y = i
            goto(x*m, y*m)
            dot(5)
done()

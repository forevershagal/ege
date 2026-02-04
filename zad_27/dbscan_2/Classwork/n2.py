from math import dist
from turtle import *


def dbscan(a, r):
    cl = []
    while a:
        cl.append([a.pop(0)])
        for i in cl[-1]:
            for j in a[:]:
                if dist(i, j) < r:
                    cl[-1].append(j)
                    a.remove(j)
    return cl


f = open('D:/INF_tasks/27_2_dbscan2/2.txt')
s = f.readline()
a = [list(map(float, i.replace(',', '.').split())) for i in f]
r = 0.45
t = 0.01
clusters = dbscan(a, r)
px = py = 0
for i in clusters:
    mn = 10000000000000000000000000
    if len(i) > 10:
        st = dbscan(i, t)
        for j in st:
            if len(j) == 3:
                p = dist(j[0], j[1]) + dist(j[1], j[2]) + dist(j[2], j[0])
                if p < mn:
                    mn = p
                    mn_st = j
        px += mn_st[0][0] + mn_st[1][0] + mn_st[2][0]
        py += mn_st[0][1] + mn_st[1][1] + mn_st[2][1]
px = int(abs(px/12) * 10000)
py = int(abs(py/12) * 10000)
print(px, py)

tracer(0)
m = 20
pu()

# for j in clusters:
#     if len(j) > 3:
#         for i in j:
#             x, y = i
#             goto(x*m, y*m)
#             dot(5)
# done()
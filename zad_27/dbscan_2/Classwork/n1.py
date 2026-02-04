from math import dist
from turtle import *

def dbscan(a, r):
    cl = []
    while a:
        cl.append([a.pop(0)])
        for i in cl[-1]:
            for j in a[:]:
                if dist(i[:2], j[:2]) < r:
                    cl[-1].append(j)
                    a.remove(j)
    return cl


f = open('D:/INF_tasks/27_2_dbscan2/1.txt')
s = f.readline()
a = [list(map(float, i.replace(',', '.').split())) for i in f]
r = 0.4
t = 0.03
clusters = dbscan(a, r)
px = py = 0

for i in clusters:
    if len(i) > 10:
        st = dbscan(i, t)
        mn_dist = 1000000000000000000000000000
        for j in st:
            if len(j) == 2:
                mn = min(j[0][2], j[1][2])
                mx = max(j[0][2], j[1][2])
                if (0.08 <= mn <= 0.6) and (0.8 <= mx <= 1.2):
                    if dist(j[0][:2], j[1][:2]) < mn_dist:
                        mn_dist = dist(j[0][:2], j[1][:2])
                        mn_st = j
        px += mn_st[0][0] + mn_st[1][0]
        py += mn_st[0][1] + mn_st[1][1]

print(int(abs(px / 10) * 100), int(abs(py / 10) * 100))

# for i in clusters:
#     print(i)
# tracer(0)
# m = 20
# pu()
# for j in clusters:
#     if len(j) > 5:
#         for i in j:
#             x, y = i[:2]
#             goto(x*m, y*m)
#             dot(5)
# done()

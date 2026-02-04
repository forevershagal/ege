from math import dist
from turtle import *


def dbscan(x, r):
    cl = []
    while x:
        cl.append([x.pop(0)])
        for i in cl[-1]:
            for j in x[:]:
                if dist(i[:2], j[:2]) < r:
                    cl[-1].append(j)
                    x.remove(j)
    return cl


f = open('D:/INF_tasks/27_1_dbscan2/2_A__63l52.txt')
s = f.readline()
a = [list(map(float, i.replace(',', '.').split())) for i in f]
t = 0.1
r = 0.8

clusters = dbscan(a, r)
px = py = 0

for i in clusters:
    if len(i) > 10:
        st = dbscan(i, t)
        mx = 0
        for j in st:
            if len(j) == 2:
                if (-2.7 < j[0][2] < 0) and (-2.7 < j[1][2] < 0):
                    if dist(j[0][:2], j[1][:2]) > mx:
                        mx = dist(j[0][:2], j[1][:2])
                        mx_st = j
        px += mx_st[0][0] + mx_st[1][0]
        py += mx_st[0][1] + mx_st[1][1]
print(int(abs(px / 6) * 150), int(abs(py / 6) * 150))


# m = 10
# tracer(0)
# pu()
#
# for j in clusters:
#     if len(j) > 5:
#         for i in j:
#             x, y = i[:2]
#             goto(x*m, y*m)
#             dot(5)
# done()
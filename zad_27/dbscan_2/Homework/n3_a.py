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


f = open('D:/INF_tasks/27_1_dbscan2/3_A__5wz76.txt')
s = f.readline()
a = [list(map(float, i.replace(',', '.').split())) for i in f]
r = 0.68
t = 0.2
clusters = dbscan(a, r)
px = py = 0
for i in clusters:
    if len(i) > 10:
        st = dbscan(i, t)
        mx = 0
        for j in st:
            if len(j) == 2:
                if (j[0][2] < -2.7 and j[1][2] > 0) or (j[1][2] < -2.7 and j[0][2] > 0):
                    if abs(abs(j[0][2]) - abs(j[1][2])) > mx:
                        mx = abs(abs(j[0][2]) - abs(j[1][2]))
                        mx_st = j

        px += mx_st[0][0] + mx_st[1][0]
        py += mx_st[0][1] + mx_st[1][1]
print(int(abs(px/10) * 100), int(abs(py/10) * 100))




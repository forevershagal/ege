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
mn_cluster = min(clusters, key=len)
mx_cluster = max(clusters, key=len)

mn = 10**20
best_center = []

for star in mn_cluster:
    s = 0
    for j in mn_cluster:
        s += dist(star, j)
    if s < mn:
        mn = s
        mn_center = star

mn = 10**20
for star in mx_cluster:
    s = 0
    for j in mx_cluster:
        s += dist(star, j)
    if s < mn:
        mn = s
        mx_center = star

# 3. Выводим результат: сумма абсциссы и ординаты
p1 = mn_center[0] + mn_center[1]
p2 = mx_center[0] + mx_center[1]

print(int(abs(p1*10000)), int(abs(10000)))
# Твоя визуализация (если нужно проверить глазами):
# m = 20
# tracer(0)
# for x, y in target_cluster:
#     goto(x*m, y*m)
#     dot(5, 'blue')
# goto(best_center[0]*m, best_center[1]*m)
# dot(15, 'red')
# update()
# done()


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
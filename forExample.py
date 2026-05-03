from math import dist
from turtle import *
f = open('/Users/shagal/Downloads/5B__5am9n.txt')
s = f.readline()
clusters = [[] for i in range(4)]
for line in f:
    x, y, m = list(map(float, line.replace(',', '.').split()))
    if 3 < m < 8:
        if -200 < x < -100 and 175 < y < 275:
            clusters[0].append([x, y])
        elif -100 < x < -25 and -250 < y < -160:
            clusters[1].append([x, y])
        elif 0 < x < 75 and -325 < y < -225:
            clusters[2].append([x, y])
        elif -50 < x < 50 and 100 < y < 190:
            clusters[3].append([x, y])

px = py = 0
m = 20
tracer(0)
pu()

# Проверка кластеризации с помощью модуля turtle
# for cluster in clusters:
#     for star in cluster:
#         x, y = star
#         goto(x*m, y*m)
#         dot(5, 'red')
# done()

for cluster in clusters:
    mn = 10**20
    centroid = []
    for center in cluster:
        s = 0
        for star in cluster:
            s += dist(center, star)
        if s < mn:
            centroid = center
            mn = s
    px += centroid[0]
    py += centroid[1]

ans1 = int(abs(px/len(clusters)) * 500)
ans2 = int(abs(py/len(clusters)) * 500)
print(ans1, ans2)

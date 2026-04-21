from math import dist
from turtle import *
tracer(0)
m = 5
pu()

f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/tasks/27_A__a7xle.txt')
stars = [list(map(float, i.replace(',', '.').split())) for i in f]
clusters = [[] for i in range(2)]

for star in stars:
    if star[1] < 15:
        clusters[0].append(star)
    else:
        clusters[1].append(star)

centers = []
center = (0, 0)
for cl in clusters:
    min_dist = 10**100
    for cent in cl:
        s = 0
        for star in cl:
            s += dist(cent, star)
        if s < min_dist:
            center = cent
            min_dist = s
    centers.append(center)

counts = list(map(len, clusters)) # список кол-ва звезд в кластерах
max_cluster_index = counts.index(max(counts)) # индекс самого большого кластера
max_cluster = clusters[max_cluster_index]
max_center = centers[max_cluster_index]

p1 = 0 # число точек, ординаты которых меньше ординаты центра
for star in max_cluster:
    if star[1] < max_center[1]:
        p1 += 1
p2 = abs(centers[0][0] - centers[1][0]) # расстояние по оси абсцисс между центрами
print(p1, int(p2*10000))


# Проверка кластеров с помощью черепахи
# for j in clusters:
#     for i in j:
#         x, y = i
#         goto(x*m, y*m)
#         dot(5, 'green')
# done()


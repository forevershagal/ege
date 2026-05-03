from math import dist

def dbscan(a, r):
    clusters = []
    while a:
        clusters.append([a.pop(0)])
        for i in clusters[-1]:
            for j in a[:]:
                if dist(i, j) < r:
                    clusters[-1].append(j)
                    a.remove(j)
        if len(clusters[-1]) < 20:
            clusters.remove(clusters[-1])
    return clusters

f = open('/Users/shagal/Downloads/27A__8tx0d.txt')
s = f.readline()
r = 1
a = [list(map(float, i.replace(',', '.').split())) for i in f]
clusters = dbscan(a, r)
px = py = 0
j = 0
anticentroids = []
for cluster in clusters:
    mx = 0
    anticentroids.append([])
    for anticentroid in cluster:
        s = 0
        for star in cluster:
            s += dist(star, anticentroid)
        if s > mx:
            mx = s
            anticentroids[j] = [mx, anticentroid[0], anticentroid[1]]
    j += 1
anticentroids.sort()
print(int(abs(anticentroids[0][1]*10000)), int(abs(anticentroids[0][2] * 10000)))


# Проверка кластеризации с помощью модуля turtle
from turtle import*
penup(), tracer(0)
m = 7
colors = ['green', 'red', 'blue', 'black', 'yellow']
for i in range(len(clusters)):
    for star in clusters[i]:
        goto(star[0]*m, star[1]*m)
        dot(4, colors[i])
done()
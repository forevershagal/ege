# Для файла А
from math import dist
from turtle import *
tracer(0), pu()
m = 10

def dbscan(points, r):
    clusters = []
    while points:
        clusters.append([points.pop(0)])
        for point in clusters[-1]:
            for neighbor in points[:]:
                if dist(point, neighbor) < r:
                    clusters[-1].append(neighbor)
                    points.remove(neighbor)
        if len(clusters[-1]) <= 15:
            clusters.remove(clusters[-1])
    return clusters


f = open('/Users/shagal/Downloads/27A__8xikf.txt')
stars = [list(map(float, i.replace(',', '.').split())) for i in f]
clusters = dbscan(stars, 0.4)
diameter_pairs = []
for cluster in clusters:
    mx_diam = -10**20
    diam_pairs = [cluster[0], cluster[1]]
    for star1 in range(len(cluster)):
        for star2 in range(star1+1, len(cluster)):
            d = dist(cluster[star1], cluster[star2])
            if d > mx_diam:
                mx_diam = d
                diam_pairs = [cluster[star1], cluster[star2]]
    diameter_pairs.append(diam_pairs)
px = py = 0
ans1 = []
ans2 = []
for pair in diameter_pairs:
    p1 = pair[0]
    p2 = pair[1]
    px = p1[0] + p2[0]
    py = p1[1] + p2[1]
    ans1.append(px)
    ans2.append(py)
print(int(max(ans1) * 10000), int(max(ans2) * 10000))





# Для файла Б
from math import dist
from turtle import *
tracer(0), pu()
m = 10

def dbscan(points, r):
    clusters = []
    while points:
        clusters.append([points.pop(0)])
        for point in clusters[-1]:
            for neighbor in points[:]:
                if dist(point, neighbor) < r:
                    clusters[-1].append(neighbor)
                    points.remove(neighbor)
        if len(clusters[-1]) <= 15:
            clusters.remove(clusters[-1])
    return clusters


f = open('/Users/shagal/Downloads/27B__8xiki.txt')
stars = [list(map(float, i.replace(',', '.').split())) for i in f]
clusters = dbscan(stars, 0.4)

# Список для хранения пар точек диаметров
diameter_pairs = []
for cluster in clusters:
    max_diam = -10**10
    diam_pair = [cluster[0], cluster[1]] # Начальное значение, служит для объявления переменной
    for star1 in range(len(cluster)):
        for star2 in range(star1+1, len(cluster)):
            d = dist(cluster[star1], cluster[star2])
            if d > max_diam:
                max_diam = d
                diam_pair = [cluster[star1], cluster[star2]]
    diameter_pairs.append(diam_pair)

# Считаем количество точек в каждом кластере
counts = [len(cluster) for cluster in clusters]
max_cluster_index = counts.index(max(counts))
# Берем пару точек из этого диаметра
p1, p2 = diameter_pairs[max_cluster_index]
q1 = dist(p1, p2)
q2 = 0

# Сравниваем пары диаметров между собой
for i in range(len(diameter_pairs)):
    for j in range(i+1, len(diameter_pairs)):
        pair_i = diameter_pairs[i] # Точки [p1, p2] первого кластера
        pair_j = diameter_pairs[j] # Точки [p1, p2] второго кластера
        # Перебираем все комбинации (по типу АА АБ БА ББ. Итого 4 варианта)
        for p_i in pair_i:
            for p_j in pair_j:
                d = dist(p_i, p_j)
                if d > q2:
                    q2 = d
print(int(q1*10000), int(q2*10000))

# Проверка верности кластеризации
for cluster in range(len(clusters)):
    for star in clusters[cluster]:
        goto(star[0]*m, star[1]*m)
        dot(3, 'red')
setpos = (0, 0)
update(), done()


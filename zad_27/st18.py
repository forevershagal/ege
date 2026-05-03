# Для файла А
from math import dist
f = open('/Users/shagal/Downloads/27_A__a5n6i.txt')
stars = []
for line in f:
    x, y, c = line.replace(',', '.').split()
    x, y = float(x), float(y)
    stars.append([x, y, c])

clusters = [[] for i in range(2)]
for star in stars:
    if star[0] < 25:
        clusters[0].append(star)
    else:
        clusters[1].append(star)

centers = []
for cluster in clusters:
    mn = 10**20
    centroid = cluster[0]
    for center in cluster:
        s = 0
        for star in cluster:
            s += dist(center[:2], star[:2])
        if s < mn:
            centroid = center
            mn = s
    centers.append(centroid)
counts = [len(cluster) for cluster in clusters]
min_cluster_index = counts.index(min(counts))
center_min_cluster = centers[min_cluster_index]
mn = 10 ** 20
for star in clusters[min_cluster_index]:
    if star[2][0] == 'A' and star[2][2:] == 'III':
        d = dist(center_min_cluster[:2], star[:2])
        if d < mn:
            mn = d
            a1, a2 = star[0], star[1]

print(int(a1*10000), int(a2*10000))

# Для файла Б
from math import dist
f = open('/Users/shagal/Downloads/27_B__a5n6h.txt')
stars = []
for line in f:
    x, y, c = line.replace(',', '.').split()
    x, y = float(x), float(y)
    stars.append([x, y, c])

clusters = [[]  for i in range(3)]
for star in stars:
    if star[1] > 14:
        clusters[0].append(star)
    elif 8 < star[1] < 14:
        clusters[1].append(star)
    else:
        clusters[2].append(star)

centers = []
for cluster in clusters:
    mn = 10**20
    centroid = []
    for center in cluster:
        s = 0
        for star in cluster:
            s += dist(center[:2], star[:2])
        if s < mn:
            mn = s
            centroid = center
    centers.append(centroid)

counts = []
for cluster in clusters:
    cnt = 0
    for star in cluster:
        if star[2][0] == 'M' and star[2][2:] == 'I':
            cnt += 1
    counts.append(cnt)
max_cluster_index = counts.index(max(counts))
min_cluster_index = counts.index(min(counts))

# b1 - расстояние между их центрами
b1 = dist(centers[min_cluster_index][:2], centers[max_cluster_index][:2])
b2 = 0
# b2 - максимальное расстояние между двумя желтыми карликами в одном кластере
for cluster in clusters:
    yellows = []
    for star in cluster:
        if star[2][0] == 'G' and star[2][2:] == 'V':
            yellows.append(star[:2])
    for i in range(len(yellows)):
        for j in range(i+1, len(yellows)):
            b2 = max(b2, dist(yellows[i], yellows[j]))
print(int(b1*10000), int(b2*10000))




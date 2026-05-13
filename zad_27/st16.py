# для файла А
from math import dist
def dbscan(points, r):
    clusters = []
    while points:
        clusters.append([points.pop(0)])
        for point in clusters[-1]:
            for neighbor in points[:]:
                if dist(point, neighbor) < r:
                    clusters[-1].append(neighbor)
                    points.remove(neighbor)
        if len(clusters[-1]) <= 5:
            clusters.remove(clusters[-1])
    return clusters
f = open('/Users/shagal/Downloads/27_A__9jdxu.txt')
stars = [list(map(float, i.replace(',', '.').split())) for i in f]
clusters = dbscan(stars, 0.4)
max_inter_diam = 0
inter_pair = []
inter_pairs = []
for i in range(len(clusters)):
    for j in range(i+1, len(clusters)):
        for star in clusters[i]:
            for star2 in clusters[j]:
                d = dist(star, star2)
                if d > max_inter_diam:
                    max_inter_diam = d
                    inter_pair = [star, star2]
        inter_pairs.append(inter_pair)
px = py = 0
for pair in inter_pairs:
    p1 = pair[0]
    p2 = pair[1]
    px += p1[0] - p2[0]
    py += p1[1] + p2[1]
print(int(abs(px)*1000), int(py*1000))

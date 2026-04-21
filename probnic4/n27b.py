from math import dist
f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/tasks/27_B__a7xld.txt')
stars = [list(map(float, i.replace(',', '.').split())) for i in f]
clusters = [[] for i in range(3)]
for star in stars:
    if star[1] > 22:
        clusters[0].append(star)
    elif star[0] < 24:
        clusters[1].append(star)
    else:
        clusters[2].append(star)

centers = []
center = (0, 0)
for cl in clusters:
    min_dist = 10 ** 100
    for cent in cl: # перебираем кандидатов на центр
        s = 0 # сумма расстояний от кандидата до остальных звезд
        for star in cl:
            s += dist(cent, star)
        if s < min_dist:
            center = cent
            min_dist = s
    centers.append(center)

counts = list(map(len, clusters))
min_cluster_index = counts.index(min(counts))
min_cluster = clusters[min_cluster_index]
min_center = centers[min_cluster_index]
x_center, y_center = min_center # Координаты центра

p1 = 0 # Число точек находящихся в квадрате вокруг центра
side = 1.8 # Сторона квадрата
for star in min_cluster:
    # Считаем те, которые лежат в квадрате
    x, y = star
    if abs(x-x_center) < side / 2 and abs(y-y_center) < side / 2:
        p1 += 1

max_cluster_index = counts.index(max(counts))
mid_cluster_index = (0 + 1 + 2) - max_cluster_index - min_cluster_index # индекс среднего кластера
p2 = abs(centers[max_cluster_index][1] - centers[mid_cluster_index][1]) # расстояние по оси ординат между центрами
print(p1, int(p2 * 10000))




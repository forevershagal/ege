from math import dist

f = open('D:/INF_tasks/tasks27_dbscan_dz/3B__5qktg.txt')  # предположим такое название
t = f.readline()
a = [list(map(float, i.replace(',', '.').split())) for i in f]

r = 0.4
clusters = []

while a:
    clusters.append([a.pop(0)])
    for j in clusters[-1]:
        for i in a[:]:
            if dist(i, j) <= r:
                clusters[-1].append(i)
                a.remove(i)

def get_quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return 0


centers = []
for j in clusters:
    if len(j) > 10:
        mn = 1000000000000000
        for star in j:
            s = 0
            for i in j:
                s += dist(star, i)
            if s < mn:
                mn = s
                center = star
        centers.append(center)

# Считаем центры по четвертям
quadrant_counts = [0, 0, 0, 0]
for center in centers:
    quadrant = get_quadrant(center[0], center[1])
    if 1 <= quadrant <= 4:
        quadrant_counts[quadrant - 1] += 1

# Если во всех четвертях одинаковое количество центров
if len(set(quadrant_counts)) == 1:
    Zx = Zy = 0
else:
    # Находим четверть с максимальным количеством центров
    max_count = max(quadrant_counts)
    popular_quadrant = quadrant_counts.index(max_count) + 1

    # Фильтруем центры (исключаем центры из популярной четверти)
    filtered_centers = []
    for center in centers:
        if get_quadrant(center[0], center[1]) != popular_quadrant:
            filtered_centers.append(center)

    # Вычисляем средние
    if filtered_centers:
        sum_x = sum(center[0] for center in filtered_centers)
        sum_y = sum(center[1] for center in filtered_centers)
        px = sum_x / len(filtered_centers)
        py = sum_y / len(filtered_centers)
    else:
        px = py = 0

print(int(abs(px) * 1000), int(abs(py) * 1000))
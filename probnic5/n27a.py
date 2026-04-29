import math


def solve(filename, clusters_count, m_min, m_max):
    # 1. Чтение и фильтрация данных
    points = []
    with open(filename) as f:
        s = f.readline()
        for line in f:
            # Структура: X Y m (может варьироваться, проверьте порядок в файле)
            x, y, m = map(float, line.replace(',', '.').split())
            if m_min < m < m_max:
                points.append([x, y])

    # 2. Кластеризация (поиск связных компонентов)
    clusters = []
    unvisited = points[:]

    while unvisited:
        curr_cluster = [unvisited.pop(0)]
        i = 0
        while i < len(curr_cluster):
            p1 = curr_cluster[i]
            j = 0
            while j < len(unvisited):
                p2 = unvisited[j]
                # Расстояние между точками должно быть <= 2 (согласно условию об аномалиях)
                if math.dist(p1, p2) <= 2:
                    curr_cluster.append(unvisited.pop(j))
                else:
                    j += 1
            i += 1
        # Сохраняем только крупные группы (игнорируем одиночные аномалии)
        if len(curr_cluster) > 5:
            clusters.append(curr_cluster)

    # Оставляем только нужное количество самых больших кластеров
    clusters.sort(key=len, reverse=True)
    clusters = clusters[:clusters_count]

    # 3. Поиск центроидов
    centroids = []
    for cluster in clusters:
        min_sum_dist = float('inf')
        best_point = cluster[0]

        for p1 in cluster:
            curr_sum_dist = sum(math.dist(p1, p2) for p2 in cluster)
            if curr_sum_dist < min_sum_dist:
                min_sum_dist = curr_sum_dist
                best_point = p1
        centroids.append(best_point)

    # 4. Расчет среднего и итогового значения
    px = sum(c[0] for c in centroids) / len(centroids)
    py = sum(c[1] for c in centroids) / len(centroids)

    return int(abs(px) * 500), int(abs(py) * 500)


# Запуск для файла А
res_a_x, res_a_y = solve('/Users/shagal/Downloads/5A__5am9k.txt', clusters_count=3, m_min=9, m_max=13)
print(f"Файл А: {res_a_x} {res_a_y}")

# Запуск для файла Б
res_b_x, res_b_y = solve('/Users/shagal/Downloads/5B__5am9n.txt', clusters_count=4, m_min=3, m_max=8)
print(f"Файл Б: {res_b_x} {res_b_y}")
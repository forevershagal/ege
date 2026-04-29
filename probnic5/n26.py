f = open('/Users/shagal/Downloads/26_meteo__6jap6 (1).txt')
n = int(f.readline())
a = []
for x in range(n):
    a.append(int(f.readline()))
a.sort(reverse=True)
b = [a[0]] # Список установленных метеостанций, начинаем с самой дальней
for i in range(1, n): # перебор остальных точек
    if b[-1] - a[i] >= 12: # Проверка условия расстояния
        b.append(a[i])
print(len(b), min(b))
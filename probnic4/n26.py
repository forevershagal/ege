f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/tasks/26__a7ysc.txt')
n = int(f.readline())
requests = []  # список для хранения всех заявок
for i in range(n):
    start, length = map(int, f.readline().split())

    # из (начало, длительность) переходим в (начало, конец)
    requests.append([start, start + length])
requests.sort(key=lambda x: x[1])  # сортируем по концу заявки
done = [requests.pop(0)]  # список для хранения самой длинной комбинации
for x in requests:
    # если начало заявки больше или равно
    # концу последней взятой, берём
    if x[0] >= done[-1][1]:
        done.append(x)

# переменная для хранения максимального конца для последней заявки
max_end = 0
for x in requests:
    # чтобы поменять последнюю заявку на более выгодную, вторая должна
    # начинаться дальше предпоследней взятой
    if x[0] >= done[-2][1]:
        max_end = max(max_end, x[1])
print(len(done), 10000 - max_end)


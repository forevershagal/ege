f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/tasks/26-3/1.txt')
k = int(f.readline())
n = int(f.readline())
a = [list(map(int, i.split())) for i in f]
a.sort()
cells = [[] for i in range(k)]
с = 0
mx = []
cnt = 1439

# i = пассажир
for i in a:
    for j in range(k):
        if (not cells[j]) or (i[0] > cells[j][-1][1]):
            #i[0] - время прихода пассажира в комнату с камерами хранения
            # cells[j][-1][1] - [j] элемент j в списке cells (ячейка),
            # [j][-1] это сам багаж (в ячейке хранятся все багажи,
            # которые лежали в ней, но нам нужно
            # оттолкнуться от последнего, так что получаем [-1],
            # [j][-1][1] - время "забирания"
            cells[j].append(i) # добавили пассажира и делаем break
            с += 1 # Считаем кол-во пассажиров
            if i[0] == cnt:
                mx.append(j+1)
            break

#

print(с, max(mx))
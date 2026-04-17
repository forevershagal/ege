f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/tasks/26-2__2yr4z.txt')
a = [list(map(int, i.split())) for i in f]
value = a.pop(0)
k, n = value[0], value[1]
cells = [[] for i in range(k)]
c = mx = 0
a.sort()
for i in a:
    for j in range(k):
        if (not cells[j]) or (i[0] >= cells[j][-1][1] + 1):
            cells[j].append(i)
            c += 1
            if i[1] <= 1440:
                mx = max(mx, j)
            break

for i in range(k):
    print(i + 1, cells[i])
print(c, mx)
f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/tasks/26-4/1.txt')
n = int(f.readline())
k = 100001
a = [list(map(int, i.split())) for i in f]
row = [[] for i in range(k)]
for i in a:
    x, y = i # Ряд и место
    row[x].append(y) # В ряд "кладем" место, которое было занято


for i in range(k):
    if row[i]:
        row[i].sort()
        for j in range(len(row[i])-1):
            if row[i][j+1] - row[i][j] == 3:
                print(i, row[i][j], row[i][j+1])

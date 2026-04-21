f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/tasks/26-4/2.txt')
n, m, k = map(int, f.readline().split())
a = [list(map(int, i.split())) for i in f]
res1 = 10**25
hall = [[0] for i in range(k+1)]
for i in a:
    x, y = i
    hall[y].append(x)

for i in range(k+1):
    if hall[i]:
        hall[i].sort(reverse=True)
        # print(i, hall[i])

for i in range(1, k):
    p1 = hall[i][0]+1
    p2 = hall[i+1][0]+1
    if max(p1, p2) < res1:
        res1 = max(p1, p2)
        res2 = i
print(res1, res2)
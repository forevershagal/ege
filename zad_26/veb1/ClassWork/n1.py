f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/tasks/1.txt')
n = int(f.readline())
a = [list(map(int, i.split())) for i in f]
a.sort(key=lambda x: x[1])
schedule = [a.pop(0)]
c = 1
for i in a:
    if i[0] > schedule[-1][1]:
        schedule.append(i)
        c += 1
print(c)
mx = 0
for i in a:
    if i[0] > 1393:
        mx = max(mx, i[0])
print(mx)

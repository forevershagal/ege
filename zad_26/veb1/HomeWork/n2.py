f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/tasks/4_26_conf__3uzok.txt')
a = [list(map(int, i.split())) for i in f]
l = a.pop(0)
c = 1
mx = 0
a.sort(key=lambda x: x[1])
schedule = [a.pop(0)]
for i in a:
    if i[1] <= l[0] and i[0] >= schedule[-1][1]:
        schedule.append(i)
        c += 1
for i in a:
    if i[0] >= schedule[-2][1] and i[1] <= l[0]:
        mx = max(mx, i[0])
print(c, mx)
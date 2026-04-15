f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/tasks/3_26_conf__3uznv.txt')
n = int(f.readline())
a = [list(map(int, i.split())) for i in f]
a.sort(key=lambda x: x[1])
schedule = [a.pop(0)]
c = 1
mn = 1000000000
for i in a:
    if  i[0] >= schedule[-1][1]:
        schedule.append(i)
        c += 1
for i in a:
    if i[0] >= 1288:
        mn = min(mn, i[0])
print(mn)
print('-------------')
print(schedule)
print(c)
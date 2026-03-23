f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/probnic/Задание 9.csv')
cnt = 0
for i in f:
    l = list(map(int, i.replace(',', ' ').split()))
    for j in l:
        usl1 = [j for j in l if l.count(j) == 4]
        usl2 = [j for j in l if l.count(j) == 1]
        usl3 = [j for j in l if l.count(j) > 1]
        if sum(usl2) / len(usl2) > sum(usl3) and len(usl1) == 4:
            cnt += 1
            break
print(cnt)
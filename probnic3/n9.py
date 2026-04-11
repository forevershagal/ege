f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/probnic/pb3_t9.csv')
l = f.readline()
cnt = 0
a = [list(map(int, i.replace(';', ' ').split())) for i in f]
for i in a:
    usl1 = min(i) > sum(int(digit) for number in i for digit in str(number))
    usl2 = max(i) % 2 == sum(int(j) for j in str(max(i))) % 2
    if usl1 and usl2:
        cnt += 1
print(cnt)
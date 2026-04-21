f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/tasks/9__a7xdd.txt')
cnt = 0
l = f.readline()
a = [list(map(int, i.replace(';', ' ').split())) for i in f]
for i in a:
    temp = sorted(i)
    if i[0] < i[1] < i[2] < i[3] < i[4] and temp[0] + temp[-1] <= sum(temp[1:4]):
        cnt +=1
print(cnt)
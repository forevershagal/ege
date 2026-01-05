f = open('D:/INC/task17_veb1_class/1.csv')
c = 0
for i in f:
    a = sorted(list(map(int, i.split(','))))

    m50 = [j for j in a if j < 50]
    b50 = [g for g in a if g > 50]

    if ((a[2] % (a[4]-a[0])) == 0) and (len(m50) > len(b50)):
        c += 1

print(c)
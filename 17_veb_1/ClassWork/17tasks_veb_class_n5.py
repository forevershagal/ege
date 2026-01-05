f = open('D:/INC/task17_veb1_class/5.csv')
c = 0
for i in f:
    a = sorted(map(int, i.split(',')))

    c3 = [g for g in a if a.count(g) == 3]
    c1 = [j for j in a if a.count(j) == 1]

    if (len(c3) == 3 and len(c1) == 3) and (((sum(c3))**2) > ((sum(c1))**2)):
        c += 1

print(c)

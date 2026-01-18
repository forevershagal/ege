f = open('D:/INC/task17_veb1_class/2.csv')
c = 0
for i in f:
    a = sorted(map(int, i.split(',')))

    c1 = len([j for j in a if j % 2 == 0])
    c2 = len([j for j in a if j % 2 != 0])

    if (c1 % 2 == 0) and (c2 % 2 != 0):
        c += 1

print(c)
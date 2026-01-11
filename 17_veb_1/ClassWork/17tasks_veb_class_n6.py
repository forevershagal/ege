f = open('D:/INC/task17_veb1_class/6.txt')
c = 0
mn = 10000000000000000000000000000
a = [int(i) for i in f]

# находим максимальное число кратное 19
mx19 = max(abs(g) for g in a if g % 19 == 0)


for i in range(len(a) - 1):
    if a[i] > mx19 or a[i + 1] > mx19:
        c += 1

        if a[i] + a[i + 1] < mn:
            mn = a[i] + a[i + 1]


print(c, mn)
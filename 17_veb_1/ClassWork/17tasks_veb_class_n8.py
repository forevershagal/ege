f = open('D:/INC/task17_veb1_class/8.txt')

c = 0
min1 = 100000000000000000000000000000000000

a = [int(i) for i in f]

min3 = min(i for i in a if ((100 <= i <= 999) and (i % 10 == 3)))

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if ((100 <= a[i] <= 999) != (100 <= a[j] <= 999)) and ((a[i] + a[j]) % min3 == 0):
            c += 1
            if (a[i] + a[j]) < min1:
                min1 = (a[i] + a[j])

print(c, min1)
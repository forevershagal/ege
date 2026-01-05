f = open('D:/INC/task17_veb1_class/7.txt')
c = 0
mx = -10000000000000000000000000000000000000000

a= [int(i) for i in f]

sr = sum(a) / len(a)

for i in range(len(a) - 1):
    if (a[i] > sr or a[i+1] > sr) and ((abs(a[i])) % 10 == 6 or (abs(a[i+1]) % 10 == 6)):
        c += 1
        if (a[i] + a[i+1]) > mx:
            mx = (a[i] + a[i+1])

print(c, mx)

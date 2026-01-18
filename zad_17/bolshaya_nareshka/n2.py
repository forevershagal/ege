f = open('D:/INF_tasks/tasks17_bolshaya_nareshka/17__1srlh.txt')
a = [int(i) for i in f]
c = 0
mx = -100000000000000000000
mx3 = max(i for i in a if i % 10 == 3)

for i in range(len(a)-1):
    if ((abs(a[i]) % 10 == 3) != (abs(a[i+1]) % 10 == 3)) and (((a[i]) ** 2) + (a[i + 1] ** 2) > mx3 ** 2):
        c += 1
        mx = max(mx, a[i] ** 2 + a[i+1] ** 2)

print(c, mx)
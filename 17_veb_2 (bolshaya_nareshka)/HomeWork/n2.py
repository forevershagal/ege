f = open('D:/INF_tasks/tasks17_bolshaya_nareshka/17__1srlh.txt')
a = [int(i) for i in f]
c = 0
mx = -1000000000000000
k3 = ([g for g in a if str(g)[-1] == '3'])
kk3 = max([abs(x) for x in k3]) ** 2
for i in range(len(a)-1):
    if (((a[i] ** 2) + (a[i+1] ** 2)) >= kk3) and ((abs(a[i]) % 10 == 3) != (abs(a[i+1]) % 10 == 3)):
        c += 1
        mx = max(mx, (a[i] ** 2) + (a[i+1] ** 2))

print(c, mx)
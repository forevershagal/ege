f = open('D:/INF_tasks/tasks17_bolshaya_nareshka/17__1sh9k.txt')
a = [int(i) for i in f]
c= 0
mx = -100000000000000000
for i in range(len(a)-1):
    if ((a[i] + a[i+1]) % 7 == 0) and ((a[i]*a[i+1]) % 15 == 0):
        c += 1
        mx = max(mx, a[i] + a[i+1])

print(c, mx)
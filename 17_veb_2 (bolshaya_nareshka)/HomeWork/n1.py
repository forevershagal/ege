f = open('D:/INF_tasks/tasks17_bolshaya_nareshka/17__1ss6e.txt')
a = [int(i) for i in f]
c = 0
mx = -100000000000000000

for i in range(len(a)-1):
    if ((abs(a[i] - a[i+1]) % 73) == 0) and (a[i] % 3 == 0 or a[i+1] % 3 == 0):
        c += 1
        mx = max(mx, abs(a[i] - a[i+1]))

print(c, mx)
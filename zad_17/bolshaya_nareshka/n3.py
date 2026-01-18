f = open('D:/INF_tasks/tasks17_bolshaya_nareshka/17__1sn7o.txt')
a = [int(i) for i in f]
c = 0
mx = -1000000000000
rara = sum(a) % 54321

for i in range(len(a)-1):
    if (a[i] % 16 == 11 or a[i+1] % 16 == 11) and a[i] <= rara and a[i+1] <= rara:
        c += 1
        mx = max(mx, a[i] * a[i+1])

print(c, mx)
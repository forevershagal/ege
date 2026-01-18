f = open('D:/INF_tasks/tasks17_bolshaya_nareshka/17__1nxre.txt')
a = [int(i) for i in f]
c = 0
mn = 100000000000000000000000

for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]
    c1 = all([int(g) % 2 == 0 for g in str(x)])
    c2 = all([int(g) % 2 == 0 for g in str(y)])
    nc1 = all([int(g) % 2 != 0 for g in str(x)])
    nc2 = all([int(g) % 2 != 0 for g in str(y)])

    if (c1 and c2) or (nc1 and nc2):
        c += 1
        mn = min(mn, x+y)
print(c, mn)

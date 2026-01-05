f = open('D:/INF_tasks/tasks17_bolshaya_nareshka/17__1nxre.txt')
a = [int(i) for i in f]
c = 0
mn = 100000000000000000000000000
for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]

    ch_x = all(int(g) % 2 == 0 for g in str(x))
    ch_y = all(int(g) % 2 == 0 for g in str(y))
    nch_x = all(int(g) % 2 != 0 for g in str(x))
    nch_y = all(int(g) % 2 != 0 for g in str(y))

    if (ch_x and ch_y) or (nch_x and nch_y):
        c += 1
        mn = min(mn, a[i] + a[i+1])

print(c, mn)
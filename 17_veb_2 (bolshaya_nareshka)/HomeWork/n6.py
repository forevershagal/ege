f = open('D:/INF_tasks/tasks17_bolshaya_nareshka/17-2__7byhg.txt')
a = [int(i) for i in f]
c = 0
mx = -1000000000000

mn5 = min([g for g in a if len(str(abs(g))) == 3 and str(abs(g))[0] == '5'])

for i in range(len(a)-2):
    t = a[i:i+3]
    k1 = len([g for g in t if abs(g) % 10 == 4])
    if (k1 == 1) and (sum(t) % mn5 != 0):
        c += 1
        mx = max(mx, sum(t))

print(c, mx)

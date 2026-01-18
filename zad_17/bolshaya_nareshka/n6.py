f = open('D:/INF_tasks/tasks17_bolshaya_nareshka/17-2__7byhg.txt')
a = [int(i) for i in f]

mn3 = min([g for g in a if len(str(abs(g))) == 3 and str(abs(g))[0] == '5'])

c = 0
mx = -100000000000000

for i in range(len(a)-2):
    t = a[i:i+3]
    t3 = len([g for g in t if abs(g) % 10 == 4])
    if t3 == 1 and (abs(sum(t)) % mn3 != 0):
        c += 1
        mx = max(mx, sum(t))

print(c, mx)


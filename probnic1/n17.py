f = open('D:/INF_tasks/probnic1/17__7jgln.txt')

a = [int(i) for i in f]
c = 0
mx = -100000000000000000
mx321 = max([g for g in a if str(g)[-3:] == '321'])

for i in range(len(a)-2):
    t = a[i:i+3]
    usl2 = [g % 5 == 0 for g in t]
    usl1 = [i for i in t if len(str(i)) == 5]
    if any(usl2) and len(usl1) == 2 and sum(t) > mx321:
        c += 1
        mx = max(mx, sum(t))

print(c, mx)
f = open('D:/INF_tasks/tasks17_bolshaya_nareshka/17-1__7byb8.txt')
a = [int(i) for i in f]
c = 0
mx = -1000000000000
ok7 = max([g for g in a if abs(g) % 10 == 7])

for i in range(len(a)-2):
    t = a[i:i+3]
    t7 = [g for g in t if abs(g) % 10 == 7 and len(str(abs(g))) == 3]
    if ((str(abs(a[i])))[0] == str(abs(a[i+1]))[0] == str(abs(a[i+2]))[0]) and (len(t7) > 0) and (abs(sum(t)) < ok7):
        c += 1
        mx = max(mx, abs(sum(t)))

print(c, mx)
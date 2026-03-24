f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/17/1/17_17__8hqnx.txt')
a = [int(i) for i in f]
c = 0
mn = 10**19
mx17 = max([i for i in a if abs(i) % 17 == 0])
for i in range(len(a)-4):
    t = a[i:i+5]
    usl1 = [j for j in t if abs(j) % 2 == 0]
    if len(usl1) == 3 and sum(t) > mx17:
        c += 1
        mn = min(mn, sum(t))
print(c, mn)
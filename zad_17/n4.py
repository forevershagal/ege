f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/17/1/17_20__8hqp5.txt')
a = [int(i) for i in f]
c = 0
mn = 10**19
for i in range(len(a)-5):
    t = a[i:i+6]
    usl1 = [j for j in t if j < 0]
    usl2 = int(sum(t)/len(t)) % 3 == 0
    if len(usl1) >= 2 and usl2:
        c += 1
        mn = min(mn, int(sum(t)/len(t)))
print(c, mn)

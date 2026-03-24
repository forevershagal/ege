f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/17/1/17_22__8hqqr.txt')
a = [int(i) for i in f]
c = 0
mx = -10**19
for i in range(len(a)-7):
    t = a[i:i+8]
    c4 = [j for j in t if abs(j) % 4 == 0]
    c3 = [j for j in t if abs(j) % 3 == 0]
    usl2 = [str(abs(j))[0] for j in t]
    l = set((map(int, usl2)))
    if len(l) == 8 and len(c4) > len(c3):
        c += 1
        mx = max(mx, sum(t))
print(c, mx)

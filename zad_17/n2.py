f = open('')
a = [int(i) for i in f]
c = 0
mx = -1000000000000000000000000
for i in range(len(a)-7):
    t = a[i:i+8]
    c4 = [j for j in t if j % 4 == 0]
    c3 = [j for j in t if j % 3 == 0]
    usl2 = [str(j)[0] for j in t]
    l = set((map(int, usl2)))
    if len(l) == 8 and len(c4) > len(c3):
        c += 1
        mx = max(mx, t)
print(c)

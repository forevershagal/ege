f = open('')
a = [int(i) for i in f]
mx = -10**19
c = 0
for i in range(len(a)-5):
    t = a[i:i+6]
    ch = [j for j in t if j % 2 == 0]
    nch = [j for j in t if j % 2 != 0]
    t = sorted(t)
    if ((t[3] * t[4] * t[5]) % abs(t[0]+t[1]+t[2]) == 0) and (len(ch) == len(nch)):
        c += 1
        mx = max(mx, sum(t))
print(c, mx)
f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/17/1/17_16__8hqqv.txt')
a = [int(i) for i in f]
m13 = max(i for i in a if abs(i) % 100 == 13)
c = 0
mn = 10**19
for i in range(len(a)-8):
    t = a[i:i+9]
    ch = [j for j in t if abs(j) % 2 == 0]
    nch = [j for j in t if abs(j) % 2 != 0]
    ch2 = [j**2 for j in ch]
    if (sum(ch2) < (m13 ** 2)) and (len(nch) > len(ch)):
        c += 1
        mn = min(mn, sum(t))
print(c, mn)
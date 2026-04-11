f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/probnic/5__1vf59.txt')
a = [int(i) for i in f]
cnt = 0
mx = -10**10
sr = sum(a) / len(a)
for i in range(len(a)-2):
    t = a[i:i+3]
    usl1 = [i for i in t if abs(i) % 2 == 0]
    usl2 = max(t) + min(t) < sr
    if len(usl1) == 1 and usl2:
        cnt += 1
        mx = max(mx, sum(t))
print(cnt, mx)

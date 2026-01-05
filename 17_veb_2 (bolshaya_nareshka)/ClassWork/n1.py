f = open() # здесь что-то открывается
a = [int(i) for i in f]

mk11 = min([g for g in a if g % 11 == 0])

c = mx = 0

for i in range(len(a) - 1):
    sr = a[i:i+2]
    t = ([(('12' in str(g)) or ('21' in str(g))) for g in sr])
    if (a[i] > mk11) and (a[i+1] > mk11) and (any(t)):
        c += 1
        mx = max(mx, (a[i] * a[i+1]))

print(c, mx)
k = 0
for x in range(850001, 851000):
    c = set()
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            c.add(i)
            c.add(x//i)
    l = sorted(c)
    f = 0
    if len(l) > 0:
        f = l[-1] - l[0]
    elif len(l) == 0:
        f = 0
    if (f != 0) and (f % 13 == 0):
        print(x, f)
        k += 1
        if k == 6:
            break



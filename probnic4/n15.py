c = []
for a in range(1, 100):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = 0
            if (x*y < a) or (5*x < y) or (486 <= x):
                f = 1
                break
        if f == 1:
            c.append(a)
print(c)
print(min(c))


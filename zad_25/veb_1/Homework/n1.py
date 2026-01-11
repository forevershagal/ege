l = []
for x in range(100010, 321342):
    c = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            c.add(i)
            c.add(x // i)

    if len(c) == 3:
        l.append(x)

print(len(l))
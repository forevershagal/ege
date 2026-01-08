l = []

for x in range(135792, 139449):
    c = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            if i % 2 == 0:
                c.add(i)
            if (x // i) % 2 == 0:
                c.add(x//i)

    if len(c) == 6:
        l.append(x)

print(len(l))
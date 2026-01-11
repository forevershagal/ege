l = []
for x in range(123123, 143124):
    if x**0.5 == int(x**0.5):
        c = set()
        for i in range(1, int(x**0.5)+1):
            if x % i == 0:
                c.add(i)
                c.add(x//i)

            if len(c) > 3:
                break
        if len(c) == 3:
            l.append(x)

print(*l)
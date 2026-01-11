for x in range(536710, 1256990):
    c = set()
    if x**0.5 == int(x**0.5):
        for i in range(1, int(x**0.5) + 1):
            if x % i == 0:
                c.add(i)
                c.add(x//i)
    if len(c) == 5:
        print(x)
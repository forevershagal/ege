for x in range(500000, 501000):
    c = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            c.add(i)
            c.add(x//i)

    r = sum(c)

    if r % 10 == 6:
        print(x, r)
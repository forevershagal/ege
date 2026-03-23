for x in range(412500, 412671):
    c = set()
    for i in range(1, int(x**0.5)+1):
        if x%i == 0:
            c.add(i)
            c.add(x//i)
    if len(c) == 6:
        print(*sorted(c))
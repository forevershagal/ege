for a in range(1, 101):
    f = 0
    for x in range(1, 1000):
        if (x & a == 0) and (x & 58 != 0) and (x & 22 == 0):
            f = 1
            break
    if f == 0:
        print(a)
        break

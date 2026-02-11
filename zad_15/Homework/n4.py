for a in range(-10, 1000):
    for x in range(1, 3000):
        for y in range(1, 3000):
            f = 0
            if ((x > 16) or (y > 25) or (a > x + y)) == False:
                f = 1
                break
        if f == 1:
            break
    if f == 0:
        print(a)
        break
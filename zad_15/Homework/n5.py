for a in range(1, 1000):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = 0
            if ((7*x+ 2*y >= a) or (x <= 20) or (y < 52)) == False:
                f = 1
                break
        if f == 1:
            break
    if f == 0:
        print(a)

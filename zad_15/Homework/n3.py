for a in range(1, 1000):
    for x in range(1, 1000):
        f = 0
        if ((x&a != 0) <= ((x&14 == 0) <= (x&75 != 0))) == False:
            f = 1
            break
    if f == 0:
        print(a)
    
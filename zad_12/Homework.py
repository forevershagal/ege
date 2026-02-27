for n in range(1, 100):
    for a in range(-500, 500):
        for b in range(-500, 500):
            x = y = 0
            x += 12
            y += 11
            for i in range(n):
                x += a
                y += b
                x += 1
                y += 2
            x -= 57
            y += 49
            if x == 0 and y == 0:
                print(n)
                break
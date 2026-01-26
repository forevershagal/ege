for n in range(100):
    for a in range(-100, 100):
        for b in range(-100, 100):
            x = y = 0
            x += 16
            y -= 21
            for i in range(n):
                x += a
                y += b
                x -= 1
                y -= 2
            x -= 60
            y -= 12
            if x == 0 and y == 0:
                print(n)

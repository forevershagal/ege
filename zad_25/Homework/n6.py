for x in range(1568, 10000):
    s = 0
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            s += i + x // i
            break

    if s % 10 == 7:
        print(x, s)
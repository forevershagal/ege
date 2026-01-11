for x in range(800000, 801000):
    m = 0
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            m += i + x // i
            break

    if m % 10 == 4:
        print(x, m)
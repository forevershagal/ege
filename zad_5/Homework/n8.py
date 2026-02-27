for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[0] + r[-1]
    if n % 3 != 0:
        r = r[-1] + r[0] + r
    if int(r, 2) < 500:
        print(n)
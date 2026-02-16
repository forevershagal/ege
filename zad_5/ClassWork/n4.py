for n in range(1,1000):
    r = bin(n)[2:]
    r = r[:-1]
    if n % 2 != 0:
        r = r + '10'
    elif n % 2 == 0:
        r = r + '01'
    if int(r, 2) == 769:
        print(n)

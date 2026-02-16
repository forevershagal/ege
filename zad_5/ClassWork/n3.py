for n in range(1, 128):
    r = bin(n)[2:].zfill(8)
    r = r.replace('0', '*')
    r = r.replace('1', '0')
    r = r.replace('*', '1')
    r = int(r, 2) + 1
    if r == 130:
        print(n)

mn = mnn = 100000000000000000
for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r = r + bin((n % 3) * 3)[2:]

    if int(r, 2) > 151:
        if int(r, 2) < mn:
            mn = int(r, 2)
            mnn = n
print(mn, mnn)
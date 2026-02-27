mnn = mn = 1000000000000000
for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 2 != 0:
        r = '0' + r + '1'
    if n % 2 == 0:
        r = r + bin(r.count('1'))[2:]
    if int(r, 2) > 250:
        if int(r, 2) < mn:
            mn = int(r, 2)
            mnn = n
print(mnn)
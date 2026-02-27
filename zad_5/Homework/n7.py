mnn = mn = 10 ** 10
for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 4 == 0:
        r = r + r[-2:]
    if n % 4 != 0:
        r = r + bin((int(r)%4) * 3)[2:]
    if int(r, 2) > 76:
        if int(r, 2) < mn:
            mn = int(r, 2)
print(mn)


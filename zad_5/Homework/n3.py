mn = mnn = 1000000000000000000000
for n in range(1, 1000):
    r = bin(n)[2:]
    r = r + r[-1:]
    if r.count('1') % 2 == 0:
        r = r + '0'
    else:
        r = r + '1'
    if r.count('1') % 2 == 0:
        r = r + '0'
    else:
        r = r + '1'
    if int(r, 2) > 204:
        if int(r, 2) < mn:
            mn = int(r, 2)
print(mn)

mrn = mn = 10**10
for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 2 != 0:
        r = '0' + r + '1'
    else:
        r = r + str(bin(r.count('1'))[2:])
    r = int(r, 2)
    if r > 250:
        if r < mrn:
            mrn = r
            mn = n
print(mn)
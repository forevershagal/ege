mn =mnn = 10000000000000000000000000
for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 2 != 0:
        r = '0' + r + '1'
    else:
        r = r + bin(sum([int(i) for i in r]))[2:]
    if int(r, 2) > 600:
        if int(r,2) < mn:
            mn = int(r, 2)
            mnn = n
print(mn, mnn)
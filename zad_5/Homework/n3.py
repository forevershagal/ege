a = []
mnr = 10**10
for n in range(1, 1000):
    r = bin(n)[2:]
    r = r + r[-1:]
    for i in range(2):
        if (r.count('1') % 2) == 0:
            r = r + '0'
        else:
            r = r + '1'
    r = int(r, 2)
    if r > 204:
        if r < mnr:
            mnr = r
print(mnr)

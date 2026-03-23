c = []
for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + '00'
    else:
        r = r + '11'
    r = int(r, 2)
    if r < 94:
        c.append(n)
print(max(c))
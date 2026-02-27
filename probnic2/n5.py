c = []
for n in range(1, 300):
    r = bin(n)[2:]
    for i in range(2):
        if r.count('0') == r.count('1'):
            r = r + r[-1]
        else:
            if r.count('0') > r.count('1'):
                r = r + '1'
            else:
                r = r + '0'
    r = int(r, 2)
    if (r%3 == 0) and (r%6 != 0):
        c.append(n)
print(max(c))
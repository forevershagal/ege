mx = set()
for x in range(1, 10241):
    r = 32**200 + 32**120 - x
    c = 0
    while r > 0:
        if r%32 == 0:
            c += 1
        r //= 32
    mx.add(c)
print(max(mx))
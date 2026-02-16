def f(x):
    s = ''
    while x > 0:
        s = str(x%3) + s
        x //= 3
    return s


mx = 0
for n in range(1, 1000):
    r = f(n)
    if (sum([int(i) for i in r]) % 3) == 0:
        r = '112' + r[3:]
    else:
        r = r + str(f(sum([int(i) for i in r])))
    if int(r, 3) % 2 == 0 and int(r, 3) <= 679:
        if int(r, 3) > mx:
            mx = int(r, 3)
print(mx)
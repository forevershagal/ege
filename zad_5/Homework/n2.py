def f(n):
    s = ''
    while n > 0:
        s = str(n%5) + s
        n //= 5
    return s

a = []
mxn = 0
for n in range(1, 1000):
    r = str(f(n))
    if (n%5) % 2 == 0:
        r = r + str(f(sum([int(i) for i in r])))
    else:
        r = '21' + r
    l = int(r, 5)
    if l <= 320:
        if n > mxn:
            mxn = n
print(mxn)

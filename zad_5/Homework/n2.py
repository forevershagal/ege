def f(x):
    s = ''
    while x > 0:
        s = str(x%5) + s
        x //= 5
    return s

mx = mxn = 1
for n in range(1, 1000):
    r = str(f(n))
    if ((n%5) % 2) == 0:
        r = r + str(f(sum([int(i) for i in str(r)])))
    elif ((n%5) % 2) != 0:
        r = '21' + r
    if int(r, 5) <= 320:
        if int(r, 5) > mx:
            mx = int(r, 5)
            mxn = n
print(mxn)

mx = -10**19
mxlen = 0
for x in range(28454, 28599):
    c = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            c.add(i)
            c.add(x//i)
    if len(c) > mxlen:
        mxlen = len(c)
        mx = x

    elif mxlen == len(c):
        if x > mx:
            mx = x
print(mx, mxlen)

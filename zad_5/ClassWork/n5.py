for n in range(1, 1000):
    r = oct(n)[2:]
    ch = [int(i) for i in r if int(i) % 2 == 0]
    nch = [int(i) for i in r if int(i) % 2 != 0]
    if len(ch) > len(nch):
        r = r + oct(sum(ch))[2:]
    elif nch > ch:
        r = r + oct(sum(nch))[2:]
    else:
        r = r + oct((sum(ch)) // 2)[2:]
    if int(r, 8) <= 870:
        print(n)
    
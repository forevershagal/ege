def f(x):
    s = ''
    while x > 0:
        s = str(x%3) + s
        x //= 3
    return s

a = []
for n in range(1, 1000):
    r = f(n)
    for i in range(2):
        usl1 = [i for i in r if i == '1']
        usl2 = [i for i in r if i == '2']
        if (len(usl1) + len(usl2)) % 2 == 0:
            r = r + '0'
        elif (len(usl1) + len(usl2)) % 2 != 0:
            r = r + '1'
    if int(r, 3) > 337:
        a.append(int(r, 3))
print(min(a))
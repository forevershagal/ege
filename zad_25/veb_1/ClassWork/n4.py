for x in range(800000, 991000):
    cc = set()
    cn = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            if i % 2 == 0:
                cc.add(i)
            else:
                cn.add(i)
            if x // 2 % i == 0:
                cc.add(x // i)
            else:
                cn.add(x // i)

    if (sum(cn) % 2 == 0) and (sum(cc) % 10 == 4):
        print(x, len(cn) + len(cc))
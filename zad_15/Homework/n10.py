def f(a):
    for x in range(1, 1000):
        if ((x&10 != 0) or (x&39 == 0) or (x&a == 0)) == 0:
            return False
    return True

for a in range(1, 1000):
    if f(a):
        print(a)
def f(a):
    for x in range(1, 1000):
        if ((x&105 == 0) <= ((x&58 != 0) <= (x&a != 0))) == 0:
            return False
    return True

for a in range(1, 1000):
    if f(a):
        print(a)
        break
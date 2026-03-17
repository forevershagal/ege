def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((a < x + y) or (x >= 48) or (y > 2)) == 0:
                return False
    return True

for a in range(1, 1000):
    if f(a):
        print(a)

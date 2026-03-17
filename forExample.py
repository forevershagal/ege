def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((x+2*y < a) or (y > x) or (x > 60)) == 0:
                return False
    return True

for a in range(1, 1000):
    if f(a):
        print(a)
        break
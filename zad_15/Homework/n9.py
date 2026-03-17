def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((y + 2*x < a) or (x > 30) or (y > 20)) == 0:
                return False
    return True

for a in range(1, 1000):
    if f(a):
        print(a)
        break
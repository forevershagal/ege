def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((2*x < y) or (x > 13) or (x*y < a)) == 0:
                return False
    return True

for a in range(1, 1000):
    if f(a):
        print(a)
        break
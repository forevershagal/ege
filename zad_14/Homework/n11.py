for x in range(1, 27001):
    n = 3 * 27**9 + 2 * 27**6 + 27**3 - x
    s = []
    while n > 0:
        s.append(n%27)
        n //= 27
    if s.count(0) == 6:
        print(x)
        break

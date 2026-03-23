def prime(x):
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return x > 1

for n in range(1325000-1, 1320000, -1):
    c = set()
    for x in range(1, int(n**0.5)+1):
        if n % x == 0:
                if prime(x) and x != n:
                    c.add(x)
                if prime(n//x) and n // x != n:
                    c.add(n//x)
    s = sum(c)
    if (s != 0) and (s <= 30000) and (s % 5 == 0):
        print(n)
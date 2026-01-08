def prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return x > 1
m = []
for x in range(500001, 535243):
    c = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            c.add(i)
            c.add(x//i)
    sm = sum(c)
    if (sm % 184 == 0) and (prime(sum(int(i) for i in str(sm)))):
        m.append(x)

print(min(m))


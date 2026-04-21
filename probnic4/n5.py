def f(x):
    s = ''
    while x > 0:
       s = str(x%3) + s
       x //= 3
    return s
mnr = 10**10
for n in range(1, 1000):
    r = f(n)
    if n % 3 == 0:
        r = r + str(r[-2:])
    else:
        r = r + str(f((sum(int(i) for i in r))*2))
    r = int(r, 3)
    if r > 520 and r % 2 != 0:
        mnr = min(r, mnr)
print(mnr)
from math import prod

def f(n):
    s = ''
    while n>0:
        s = str(n%4) + s
        n //= 4
    return s

a = []
for n in range(1, 1000):
    r = str(f(n))
    usl = [i for i in r if i != '0']
    if prod(map(int, usl)) % 3 == 0:
        r = r + '21'
    else:
        r = r + '12'
    l = int(r, 4)
    if int(l) <= 280:
        a.append(l)
print(max(a))
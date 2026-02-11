def f(n, osn):
    s = ''
    while n > 0:
        s += str(n % osn)
        n = n // osn
    s = s[::-1]
    return s

for n in range(1, 300):
    s = f(n, 3)
    if n % 5 == 0:
        s += '02'
    if n % 5 != 0:
        k = (n%5) * 3
        s1 = f(k, 3)
        s += s1[len(s1)-2:]
    r = int(s, 3)
    if r == 192:
        print(n)
        break
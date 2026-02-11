
# функция перевода числа с основанием osn
def f(n, osn):
    s = ''
    while n > 0:
        s += str(n % osn)
        n //= osn
    s = s[::-1]
    return s

a = set()

for n in range(1, 200):
    s = f(n, 4)
    k = map(int, s)
    mult = 1

    for i in k:
        if i != 0:
            mult *= i

    if mult % 3 == 0:
        s = s + '21'

    if mult % 3 != 0:
        s = s + '12'

    r = int(s, 4)

    if r < 280:
        a.add(r)

print(max(a))



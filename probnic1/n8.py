from itertools import product

a = product('АПРСУ', repeat=5)
c = 0
for i in a:
    s = ''.join(i)
    c += 1
    if s.count('У') <= 1 and s.count('АА') == 0:
        print(c)
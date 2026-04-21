from itertools import product
a = 'ВИЛМОC'
n = 0
for i in product(a, repeat=5):
    s = ''.join(i)
    n += 1
    if s[0] not in 'ОC'  and s.count('В') == 1 and s.count('C') <= 1:
        print(n, s)

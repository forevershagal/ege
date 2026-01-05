from itertools import product
count = set()
for i in range(2, 6):
    for x in product('АБВГДЕ', repeat=i):
        s = ''.join(x)
        if s[0] not in 'АЕ' and s[-1] in 'АЕ':
            count.add(s)

print(len(count))

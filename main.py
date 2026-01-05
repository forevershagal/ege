# c = bin(161)
# c1 = bin(86)
# c2 = bin(222)
# c3 = bin(234)
# print(c, c1, c2, c3)
#
# # print(int('10011001', 2))
# # print(int('00000011', 2))
# # print(int('00010000', 2))
# # print(int('00000000', 2))

from itertools import product

ans = set()
alf = 'ПОЛИНА'

for w in product(alf, repeat=6):
    w = "".join(w)
    if (w.count('Л')) <= 1 and(w[0] != 'Л') and (w[-1] != 'Л') and ('ЛА' not in w) and ('АЛ' not in w):
        ans.add(w)

print(len(ans))




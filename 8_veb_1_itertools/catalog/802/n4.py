from itertools import *
#
# alf = permutations('САМОРЗВИТЕ', 4)
# c = 0
# for i in alf:
#     s = ''.join(i)
#     c += 1
# print(c)

# Или такой код с использованием генераторов
s1 = len([i for i in permutations('САМОРЗВИТЕ', 4)])
print(s1)
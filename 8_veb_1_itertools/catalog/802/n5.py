from itertools import *


# ----- такой код с использованием генераторов
s1 = len([w for w in product('ПШК', repeat=3) if w[0] == 'Ш'])
s2 = len([w for w in product('ДМШК', repeat=4) if w[0] == 'Ш'])
print(s1 * s2)



# ----------- ИЛИ такой код обычный ------------
# alf1 = product('ПШК', repeat=3)
# alf2 = product('ДМШК', repeat=4)
# c = 0
# set_for_3 = set()
# set_for_4 = set()
# answer = set()
# for i in alf1:
#     s1 = ''.join(i)
#     if s1[0] == 'Ш':
#         set_for_3.add(s1)
#
# for i in alf2:
#     s1 = ''.join(i)
#     if s1[0] == 'Ш':
#         set_for_4.add(s1)
#
# for i in set_for_3:
#     for g in set_for_4:
#         answer.add(i+g)
#
# print(len(answer))
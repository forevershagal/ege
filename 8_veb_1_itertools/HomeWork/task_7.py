# Сколько слов из шести символов может составить
# Петя перестановкой букв слова БАОБАБ?


from itertools import *


a = 'БАОБАБ'
c = set()

for i in permutations(a, 6):

    s = ''.join(i)
    c.add(s)

print(len(c))

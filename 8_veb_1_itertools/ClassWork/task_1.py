# Определите количество шестиричных пятизначных чисел,
# в записи которых не менее двух цифр 5 и
# не более трех нечетных цифр, меньших 4


from itertools import *

a = '012345'
c = 0

for i in product(a, repeat=5):
    s = ''.join(i)
    t = [g for g in s if g in '13']
    if(s[0] != '0') and (s.count('5') >= 2) and (len(t) <= 3):
        c += 1
        print(s)

print(c)
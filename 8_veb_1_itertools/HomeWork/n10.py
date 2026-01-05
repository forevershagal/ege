from itertools import permutations

c = set()

for x in permutations('012345678', 7):
    s = ''.join(x)
    if s[0] != '0':
        s1 = s.replace('2', '0').replace('4', '0').replace('6', '0').replace('8', '0')
        s1 = s1.replace('1', '1').replace('3', '1').replace('5', '1').replace('7', '1')

        if '00' not in s1 and '11' not in s1:
            c.add(s)

print(len(c))
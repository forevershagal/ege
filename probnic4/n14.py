mn = 10**100
a = '0123456789abcdefghijklm'
for x in a:
    s1 = int('761' + x + '035', 23)
    s2 = int('338' + x + '932', 23)
    s = s1 + s2
    if s % 22 == 0:
        mn = min(s, mn)
print(mn // 22)
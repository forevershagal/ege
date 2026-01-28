f = open('D:/INF_tasks/task24_ukaz-reg/24_M3__42nfh.txt')
s = f.readline()

cD = start = mx = cZv = 0

s = s.replace('A', '*')
s = s.replace('E', '*')
s = s.replace('I', '*')
s = s.replace('O', '*')
s = s.replace('U', '*')
s = s.replace('Y', '*')

for end in range(len(s)):
    if s[end] == '*':
        cZv += 1
    if s[end] == '.':
        cD += 1

    while cD > 6:
        if s[start] == '.':
            cD -= 1
        if s[start] == '*':
            cZv -= 1
        start += 1

    if cD == 6 and cZv > 15:
        mx = max(mx, end-start + 1 + cZv * 5)

print(mx)
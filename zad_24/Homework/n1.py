f = open('smt')
s = f.readline()
gs = 'AEIOUY'
cG = cT = mx = start = 0

for end in range(len(s)):
    if s[end] == '.':
        cT += 1

    if s[end] in gs:
        cG += 1

    while cT > 6 or cG <= 15:
        if s[start] == '.':
            cT -= 1
        if s[start] in gs:
            cG -= 1

        start += 1

    if cT <= 6 and cG > 15:
        mx = max(mx, end-start+1)

print(mx)
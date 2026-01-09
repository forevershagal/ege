f = open('smth')
s = f.readline()

start = mx = cT = 0

for end in range(len(c)):
    if s[end] == 'T':
        cT += 1

    while cT != 100:
        if s[start] == 'T':
            cT -= 1
        start += 1

    if cT == 100:
        mx = max(mx, end-start+1)

print(mx)
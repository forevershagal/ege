f = open('smth')
s = f.readline()

mn = start = cY = 0

for end in range(len(s)):
    if s[end] == 'Y':
        cY += 1

    while cY < 100:
        if s[start] == 'Y':
            cY -= 1
        start += 1

    if cY >= 100:
        mn = min(mn, end-start+1)

print(mn)
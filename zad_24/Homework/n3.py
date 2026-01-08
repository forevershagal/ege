f = open('smth')
s = f.readline()

start = mx = cF = cL = 0

for end in range(len(s)):
    if s[end] == 'F':
        cF += 1
    if s[end] == 'L':
        cL += 1

    while cF > 3 or cL > 3:
        if s[start] == 'F':
            cF += 1
        if s[start] == 'L':
            cL += 1

        start += 1

    if cF <= 3 and cL <= 3:
        mx = max(mx, end-start+1)

print(mx)
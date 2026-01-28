f = open('D:/INF_tasks/task24_ukaz-reg/24__7h6ti.txt')
s = f.readline()

start = mx = cU = cV = cW = cX = cY = cZ = 0

for end in range(len(s)):
    if s[end] == 'U':
        cU += 1
    if s[end] == 'V':
        cV += 1
    if s[end] == 'W':
        cW += 1
    if s[end] == 'X':
        cX += 1
    if s[end] == 'Y':
        cY += 1
    if s[end] == 'Z':
        cZ += 1

    while cU > 100 or cV > 100 or cW > 100 or cX > 100 or cY > 100 or cZ > 100:
        if s[start] == 'U':
            cU -= 1
        if s[start] == 'V':
            cV -= 1
        if s[start] == 'W':
            cW -= 1
        if s[start] == 'X':
            cX -= 1
        if s[start] == 'Y':
            cY -= 1
        if s[start] == 'Z':
            cZ -= 1
        start += 1

    if cU <= 100 and cV <= 100 and cW <= 100 and cX <= 100 and cY <= 100 and cZ <= 100:
        mx = max(mx, end-start+1)

print(mx)
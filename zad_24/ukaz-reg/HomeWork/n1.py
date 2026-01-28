f = open('D:/INF_tasks/task24_ukaz-reg/24__7h7ej.txt')
s = f.readline()

mx = cX = cY = start = 0

for end in range(len(s)):
    if s[end] == 'X':
        cX += 1
    if s[end] == 'Y':
        cY += 1

    while cX > 1 or cY > 1:
        if s[start] == 'X':
            cX -= 1
        if s[start] == 'Y':
            cY -= 1
        start += 1

    if cX == 1 and cY == 1:
        mx = max(mx, end-start+1)
print(mx)
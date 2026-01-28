
f = open('D:/INF_tasks/task24_ukaz-reg/9.txt')
s = f.readline()
mx = cY = start = cnt = 0
while '2025' in s: s = s.replace('2025', '*')

for end in range(len(s)):
    if s[end] == '*':
        cnt += 1
    if s[end] == 'Y':
        cY += 1

    while cY > 80:
        if s[start] == 'Y':
            cY -= 1
        if s[start] == '*':
            cnt -= 1
        start += 1

    if cnt >= 90 and cY == 80:
        mx = max(mx, end-start-1 + cnt * 3)
print(mx)




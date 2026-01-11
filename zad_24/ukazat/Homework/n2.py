f = open('D:/INF_tasks/task_24_ukazat/24_2024__7aiiq.txt')
s = f.readline()

start = mx = cT = 0

for end in range(len(s)):
    if s[end] == 'T':
        cT += 1

    while cT > 100:
        if s[start] == 'T':
            cT -= 1
        start += 1

    if cT == 100:
        mx = max(mx, end-start+1)

print(mx)
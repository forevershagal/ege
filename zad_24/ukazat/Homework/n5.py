f = open('D:/INF_tasks/task_24_ukazat/24_4__3b9tg.txt')
s = f.readline()

mx = start = cD = 0

for end in range(len(s)):
    if s[end] == 'D':
        cD += 1

    while cD > 100:
        if s[start] == 'D':
            cD -= 1

        start += 1

    if cD <= 100:
        mx = max(mx, end-start+1)

print(mx)

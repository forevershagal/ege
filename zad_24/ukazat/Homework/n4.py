f = open('D:/INF_tasks/task_24_ukazat/24_16__3b9u2.txt')
s = f.readline()

mn = 10 ** 6
start = cY = 0

for end in range(len(s)):
    if s[end] == 'Y':
        cY += 1

    while cY >= 100:
        if end-start + 1 < mn:
            mn = end - start + 1
        if s[start] == 'Y':
            cY -= 1
        start += 1

print(mn)
f = open('D:/INF_tasks/task24_ukaz-reg/3.txt')
s = f.readline()

start = mx = cnt = 0

for end in range(len(s)):
    if s[end] == 'B':
        cnt += 1

    while cnt > 53:
        if s[start] == 'B':
            cnt -= 1
        start += 1

    if cnt == 53:
        mx = max(mx, end-start+1)

print(mx)
f = open('D:/INF_tasks/task24_ukaz-reg/1.txt')
s = f.readline()
mx = cnt = start = 0

for end in range(len(s)):
    if s[end:end+2] == '*':
        cnt += 1

    while cnt > 50:
        if s[start:start+2] == '*':
            cnt -= 1
        start += 1

    if cnt == 50:
        mx = max(mx, end-start+1)

print(mx+1)
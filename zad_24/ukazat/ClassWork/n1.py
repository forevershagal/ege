f = open('smth')
s = f.readline()

start = cb = mx = 0

for end in range(len(s)):
    if s[end] == "B":
        cb += 1
    while cb > 53:
        if s[start] == "B":
            cb -= 1
        start += 1

    if cb == 53:
        mx = max(mx, end-start+1)

print(mx)
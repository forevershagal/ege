f = open('D:/INF_tasks/probnic1/24__7h6y9.txt')
s = f.readline()
start = 0
mx = 0
a = b = c = d = e = f = 0

for end in range(len(s)):
    if s[end] == 'A':
        a += 1
    if s[end] == 'B':
        b += 1
    if s[end] == 'C':
        c += 1
    if s[end] == 'D':
        d += 1
    if s[end] == 'E':
        e += 1
    if s[end] == 'F':
        f += 1

    while a > 100 or b > 100 or c > 100 or d > 100 or e > 100 or f > 100:
        if s[start] == 'A':
            a -= 1
        if s[start] == 'B':
            b -= 1
        if s[start] == 'C':
            c -= 1
        if s[start] == 'D':
            d -= 1
        if s[start] == 'E':
            e -= 1
        if s[start] == 'F':
            f -= 1
        start += 1

    if a <= 100 and b <= 100 and c <= 100 and d <= 100 and e <= 100 and f <= 100:
        mx = max(mx, end-start + 1)

print(mx)


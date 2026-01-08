f = open('smth')
s = f.readline()
c = [0] * 6
cnt = mx = start = 0

for end in range(len(s)):
    if s[end] in 'UVWXYZ':
        c[ord(s[end]) - 85] += 1

    while max(c) > 100:
        if s[start] in 'UVWXYZ':
            c[ord(s[end]) - 85] -= 1
        start -= 1

    if max(c) <= 100:
        mx = max(mx, end-start+1)

print(mx)
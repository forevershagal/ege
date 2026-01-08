f = open('smth')
s = f.readline()
cY = c2 = start = mx = 0

while '2025' in s: s = s.replace('2025', '*')

for end in range(len(s)):
    if s[end] == "Y":
        cY += 1
    if s[end] == '*':
        c2 += 1

    while cY > 80 or c2 < 90:
        if s[start] == 'Y':
            cY -= 1
        if s[start] == '*':
            c2 -= 1
        start -= 1


    if cY == 80 and c2 >= 90:
        mx = max(mx, end-start+1 + c2*3)

print(mx)
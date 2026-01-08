f = open('smth')
s = f.readline()

start = mx = cC = cD = 0

for end in range(len(s)):
    if s[end] == 'C':
        cC += 1
    if s[end] == 'D':
        cD += 1

    while cC > 2 or cD > 2:
        if s[start] == 'C':
            cC -= 1
        if s[start] == 'D':
            cD -= 1

        start +=1

    if cC <= 2 and cD <= 2:
        mx = max(mx, end-start+1)

print(mx)
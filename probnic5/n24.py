mx = 0
start = -1 # Индекс последнего найденного "С"
f = open('/Users/shagal/Downloads/24-280__6eq3c.txt')
s = f.readline()
for end in range(len(s)):
    if s[end] == 'C':
        start = end
    elif s[end] == 'D':
        if start != -1:
            mx = max(mx, end-start+1)
            start = -1
print(mx)


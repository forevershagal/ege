f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/tasks/2.txt')
n = int(f.readline())
l_start = []
l_end = []
for i in range(n):
    g, p = map(int, f.readline().split())
    if g > p:
        l_start.append([g, i])
    else:
        l_end.append([p, i])
l_start.sort()
l_end.sort(reverse=True)
line = l_start+l_end
print(l_start)
print(l_end)
print(line)
print(len(l_end))
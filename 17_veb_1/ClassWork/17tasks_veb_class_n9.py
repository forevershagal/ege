f = open('D:/INC/task17_veb1_class/9.txt')

a = [int(i) for i in f]
sr = sum(a) / len(a)
c = 0

mx = -100000000000000000000000000000
for i in range(len(a) - 2):
    t = [a[i], a[i+1], a[i+2]]

    ch = len([x for x in t if x % 2 == 0])

    if (ch == 1) and (max(t) + min(t) < sr):
        c += 1
        mx = max(mx, sum(t))

print(c, mx)
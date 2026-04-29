f = open('/Users/shagal/Downloads/9_2__3h2ur.txt')
cnt = 0
a = [list(map(str, i.replace(';', ' ').split())) for i in f]
for i in a:
    l = i[0]+i[1]+i[2]+i[3]+i[4]+i[5]
    usl1 = int(l, 2) % 4 == 0
    usl2 = int(i[0]+i[1]+i[2], 2) < int(i[3]+i[4]+i[5], 2)
    if usl1 and usl2:
        cnt += 1
print(cnt)

f = open('C:/Users/Руслан/Desktop/Users/9.txt')

a = [list(map(int, i.replace(',', ' ').split())) for i in f]
count = 0
for j in a:
    usl1 = [i for i in j if j.count(i) > 1]
    usl2 = [i for i in j if j.count(i) == 1]
    if (len(usl1) > len(usl2)) and (sum(usl1) < sum(usl2)):
        count += 1
print(count)
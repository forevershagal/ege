f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/tasks/26-3/2.txt')
n = int(f.readline())
k = 100
a = []
cars = busses = 0
for i in f:
    t = i.split()
    a.append([int(t[0]), int(t[0]) + int(t[1]), t[2]])
a.sort()
# print(a[:10])
park = [[] for i in range(k)]
for i in a:
    if i[2] == 'A':
        for j in range(k):
            if (not park[j]) or (i[0] >=  park[j][-1][1]):
                # park[j] - парковочное место,
                # [-1] - последняя "машина", которая стояла там,
                # [1] время конца парковки
                park[j].append(i)
                cars += 1
                break
    else:
        for j in range(80, k):
            if (not park[j]) or (i[0] >= park[j][-1][1]):
                park[j].append(i)
                busses += 1
                break
print(cars, n - cars - busses)
# for i in range(k):
#     print(i+1, park[i])

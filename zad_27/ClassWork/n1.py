from turtle import *
from math import dist


f = open('D:/INF_tasks/tasks27/1__81ktp.txt')
a = [list(map(float, i.replace(',', '.').split())) for i in f]
clusters = [[], [], []]
for i in a:
    x, y = i
    if x > 4:
        clusters[2].append(i)
    elif (x - 1.4) ** 2 + (y - 0.4) ** 2 <= 1.7 ** 2:
        clusters[0].append(i)
    else:
        clusters[1].append(i)


centers = []

for j in range(3):
    mn = 1050000000000000
    for star in clusters[j]:
        s = 0
        for i in clusters[j]:
            s += dist(star, i)
        if s < mn:
            mn = s
            mn_star = star
    centers.append(mn_star)

px = (centers[0][0] + centers[1][0] + centers[2][0]) / 3
py = (centers[0][0] + centers[1][1] + centers[2][1]) / 3
print(int(px*10000), int(py*10000))

# m = 80
# tracer(0)
# pu()
# cl = ['red', 'green', 'blue']
#
# for j in range(3):
#     for i in clusters[j]:
#         x, y, = i
#         goto(x * m, y * m)
#         dot(5, cl[j])
#
# for i in centers:
#     x, y = i
#     goto(x*m, y*m)
#     dot(15, 'black')
#
# done()

from math import dist

f = open('D:/INF_tasks/tasks27/veb1/zad1/27_B_1__4uxdf.txt')
a = [list(map(float, i.replace(',', '.').split())) for i in f]

clusters = [[], [], [], []]

for i in a:
    x, y = i
    if x < -30:
        clusters[3].append(i)
    elif x > 10:
        if y > 0:
            clusters[1].append(i)
        else:
            clusters[0].append(i)
    else:
        clusters[2].append(i)

centers = []
for g in range(4):
    mn = 1000000000000000000
    for star in clusters[g]:
        s = 0
        for i in clusters[g]:
            s += dist(star, i)
        if s < mn:
            mn = s
            mn_star = star
    centers.append(mn_star)

px = abs(centers[0][0] + centers[1][0] + centers[2][0] + centers[3][0] ) / 4
py = abs(centers[0][1] + centers[1][1] + centers[2][1] + centers[3][1] ) / 4

print(int(px*1000), int(py*1000))

# 33644 4375 792 24451

# from turtle import *
# m = 5
# tracer(0)
# pu()
# cl = ['red', 'green', 'blue', 'black']
#
# for g in range(4):
#     for i in clusters[g]:
#         x, y = i
#         goto(x*m, y*m)
#         dot(3, cl[g])
#
# done()

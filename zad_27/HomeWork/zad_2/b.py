from math import *
f = open('D:/INF_tasks/tasks27/veb1/zad2/27_B_2__4uxf3.txt')
a = [list(map(float, i.replace(',', '.').split())) for i in f]

clusters = [[], [], []]

for i in a:
    x, y = i
    if x > 0:
        clusters[0].append(i)
    elif x < 0 and y > -20:
        clusters[1].append(i)
    else:
        clusters[2].append(i)

centers = []

for g in range(3):
    mn = 100000000000000
    for star in clusters[g]:
        s = 0
        for i in clusters[g]:
            s += dist(star, i)
        if s < mn:
            mn = s
            mn_star = star
    centers.append(mn_star)


px = abs(centers[0][0] + centers[1][0] + centers[2][0] ) / 3
py = abs(centers[0][1] + centers[1][1] + centers[2][1])  / 3

print(int(px*1000), int(py*1000))

# from turtle import *
#
# m = 10
# cl = ['red', 'green', 'blue']
# tracer(0)
# pu()
#
# for g in range(3):
#     for i in clusters[g]:
#         x, y = i
#         goto(x*m, y*m)
#         dot(5, cl[g])
#
# done()

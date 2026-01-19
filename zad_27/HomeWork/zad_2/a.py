from math import dist

f = open('D:/INF_tasks/tasks27/veb1/zad2/27_A_2__4uxf2.txt')
a = [list(map(float, i.replace(',', '.').split())) for i in f]
clusters = [[], [], [], [], []]
for i in a:
    x, y = i
    if x > 20:
        if y > 5:
            clusters[1].append(i)
        else:
            clusters[0].append(i)
    elif x < 0:
        if y < -20:
            clusters[2].append(i)
        elif (x + 28) ** 2 + (y + 4) ** 2 < 9 ** 2:
            clusters[3].append(i)
        else:
            clusters[4].append(i)


centers = []
for g in range(5):
    mn = 100000000000000000
    for star in clusters[g]:
        s = 0
        for i in clusters[g]:
            s += dist(star, i)
        if s < mn:
            mn = s
            mn_star = star
    centers.append(mn_star)

px = abs(centers[0][0] + centers[1][0] + centers[2][0] + centers[3][0] + centers[4][0] ) / 5
py = abs(centers[0][1] + centers[1][1] + centers[2][1] + centers[3][1] + centers[4][1] ) / 5

print(int(px*1000), int(py*1000))


# from turtle import *
# m = 5
# tracer(0)
# pu()
# cl = ['red', 'green', 'blue', 'black', 'purple']
#
# for g in range(5):
#     for i in clusters[g]:
#         x, y = i
#         goto(x*m, y*m)
#         dot(5, cl[g])
# done()
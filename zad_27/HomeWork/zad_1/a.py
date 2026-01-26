from math import dist

f = open('D:/INF_tasks/tasks27/veb1/zad1/27_A_1__4uxdd.txt')
a = [list(map(float, i.replace(',', '.').split())) for i in f]
clusters = [[], []]
for i in a:
    x, y = i
    if y > 0:
        clusters[1].append(i)
    else:
        clusters[0].append(i)

centers = []
for g in range(2):
    mn = 1000000000000000000
    for star in clusters[g]:
        s = 0
        for i in clusters[g]:
            s += dist(star, i)
        if s < mn:
            mn = s
            mn_star = star
    centers.append(mn_star)

px = abs(centers[0][0] + centers[1][0]) / 2
py = abs(centers[0][1] + centers[1][1]) / 2

print(int(px*1000), int(py*1000))


# from turtle import *
# tracer(0)
# m = 5
# pu()
# cl = ['red', 'green']
# for g in range(2):
#     for i in clusters[g]:
#         x, y = i
#         goto(x*m, y*m)
#         dot(5, cl[g])
# done()
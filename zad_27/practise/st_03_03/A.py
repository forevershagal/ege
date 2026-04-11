from math import dist
from turtle import *
tracer(0)

def dbscan(a, r):
    cl = []
    while a:
        cl.append([a.pop(0)])
        for i in cl[-1]:
            for j in a[:]:
                if dist(i, j) < r:
                    cl[-1].append(j)
                    a.remove(j)
    return cl

f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/st_27_0303/27_A.txt')
a = [list(map(float, i.replace(';', ',').split())) for i in f]
r = 7
m = 20
clusters = dbscan(a, r)

md = 0 # max dist btw 2 stars
for i in clusters[0]:
    for j in clusters[1]:
        if dist(i, j) > md:
            md = dist(i, j)
            md_stars = [i, j] # save the pair of stars

px = md_stars[0][0] + md_stars[1][0] # solve summary of x of needed stars
py = abs(md_stars[0][1] - md_stars[1][1]) # solve abs diff y of needed stars

print(int(abs(px * 1000)), int(abs(py*1000)))


# pu()
# for j in clusters:
#     if len(j) > 3:
#         for i in j:
#             x, y = i
#             goto(x*m, y*m)
#             dot(5)
# done()

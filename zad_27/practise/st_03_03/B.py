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

f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/st_27_0303/27_B.txt')
a = [list(map(float, i.replace(';', ',').split())) for i in f]
r = 6
m = 20
pairs = [(0, 1), (0, 2), (1, 2)]
diams = []
st_diams = []
point = (2, 2)

clusters = dbscan(a, r)
clusters = [i for i in clusters if len(i) > 1]

for i, j in pairs:
    md = 0
    for star1 in clusters[i]:
        for star2 in clusters[j]:
            if dist(star1, star2) > md:
                md = dist(star1, star2)
                md_stars = (star1, star2)
    diams.append(md)
    st_diams.append(md_stars[0])
    st_diams.append(md_stars[1])

q1 = sum(diams)
q2 = max(dist(p, point) for p in st_diams) # max dist from point to all in stars, which gived max

print(int(q1*100), int(q2*100))



# pu()
# for j in clusters:
#     if len(j) > 3:
#         for i in j:
#            x, y = i
#            goto(x*m, y*m)
#            dot(5)
# done()
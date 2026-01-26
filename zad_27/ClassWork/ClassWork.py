from math import dist

f = open('D:/INF_tasks/tasks27/1__81ktp.txt')
a = [list(map(float, (i.replace(',', '.').split()))) for i in f]
clusters = [[], [], []]
for i in a:
    x, y = i
    if x > 4:
        clusters[2].append(i)
    elif (x-1.4) ** 2 + (y-0.4) ** 2 < 1.7 ** 2:
        clusters[0].append(i)
    else:
        clusters[1].append(i)

centers = []
for g in range(3):
    mn = 1000000000000000000000000000
    for star in clusters[g]:
        s = 0
        for i in clusters[g]:
            s += dist(star, i)
        if s < mn:
            mn = s
            mn_star = star
    centers.append(mn_star)

px = (centers[0][0] + centers[1][0] + centers[2][0]) / 3
py = (centers[0][1] + centers[1][1] + centers[2][1]) / 3
print(int(px*10000), int(py*10000))



from turtle import *
m = 50
tracer(0)
pu()
cl = ['red', 'green', 'blue']


for g in range(3):
    for i in clusters[g]:
        x, y = i
        goto(x * m, y * m)
        dot(5, cl[g])

for i in centers:
    x, y = i
    goto(x*m, y*m)
    dot(15)

for i in range(-100, 100):
    for g in range(-100, 100):
        x, y = i / 5, g / 5
        if (x-1.4) ** 2 + (y-0.4) ** 2 < 1.7 ** 2:
            goto(x*m, y*m)
            dot(5, 'purple')
done()

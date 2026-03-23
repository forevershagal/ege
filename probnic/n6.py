from turtle import *

m = 20
tracer(10)

path_points = []
path_points.append((0, 0))

def move(dist):
    for i in range(dist):
        forward(1*m)
        curr_pos = (round(xcor()/m), round(ycor()/m))
        path_points.append(curr_pos)

for i in range(4):
    for j in range(4):
        move(6)
        right(90)
    move(10)
    right(90)
    move(3)

uniqe_points = set()
more_than_one = set()

for p in path_points:
    if p in uniqe_points:
        more_than_one.add(p)
    else:
        uniqe_points.add(p)

print(len(more_than_one))
update()
done()
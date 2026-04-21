from turtle import *
tracer(0)
m = 7
left(90)
screensize(2000, 2000)
for i in range(6):
    fd(71*m)
    right(90)
    fd(73*m)
    right(90)
pu()
fd(18*m)
right(90)
fd(22*m)
left(90)
pd()
for j in range(6):
    fd(45*m)
    right(90)
    fd(58*m)
    right(90)

pu()
for x in range(-1, 100):
    for y in range(-1, 100):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()
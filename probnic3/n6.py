from turtle import *
m = 20
tracer(0)


fd(10*m)
pd()
for i in range(5):
    fd(-6*m)
    left(180)
    fd(4*m)
    right(90)
forward(-5*m)
for i in range(8):
    fd(3*m)
    right(135)
    fd(-5*m)
    right(45)

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(5)

done()

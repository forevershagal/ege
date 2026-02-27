from turtle import *

tracer(0)
left(90)
m = 50
for i in range(12):
    for b in range(15):
        forward(2*m)
        right(90)
    forward(5*m)

pu()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(5)
update()
done()
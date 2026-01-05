from turtle import *

m = 20
left(90)
tracer(0)

for i in range(4):
    forward(5*m)
    right(150)
    forward(5*m)
    right(30)

penup()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(5)

update()
done()
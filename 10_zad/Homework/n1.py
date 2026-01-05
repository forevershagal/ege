from turtle import *
tracer(0)

m = 20
left(90)
for i in range(4):
    right(90)
    for g in range(2):
        forward(4*m)
        right(315)
    right(90)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(5)

done()
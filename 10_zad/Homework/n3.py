from turtle import *

m = 20
tracer(0)

left(90)

for i in range(4):
    forward(10*m)
    right(90)


penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(5)

update()
done()
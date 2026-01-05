from turtle import *

left(90)
tracer(0)
m = 20

for i in range(2):
    forward(10*m)
    right(90)
    forward(20*m)
    right(90)

penup()

forward(5*m)
right(90)
forward(7*m)
left(90)

pendown()

for i in range(2):
    forward(20*m)
    right(90)
    forward(40*m)
    right(90)


penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(5)

update()
done()
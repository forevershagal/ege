from turtle import *
tracer(0)
m = 20
screensize(3000, 3000)
pd()
for i in range(2):
    forward(21*m)
    right(90)
    forward(27*m)
    right(90)
pu()

forward(9*m)
right(90)
forward(10*m)
left(90)

pd()

for i in range(2):
    forward(86*m)
    right(90)
    forward(47*m)
    right(90)

pu()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(5)

done()

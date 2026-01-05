from turtle import *

tracer(0)
m = 80

left(90)
for i in range(4):
    for g in range(2):
        forward(2*m)
        right(45)
        forward(2*m)
        left(90)
    right(180)
update()
done()
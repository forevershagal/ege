from turtle import *
tracer(1000)
m = 20
screensize(2000, 2000)
for i in range(4):
    fd(4*m)
    right(60)
    fd(8*m)
    right(120)

pu()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(3, 'red')
done()



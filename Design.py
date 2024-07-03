from turtle import *
t = Turtle()
bgcolor("black")
t.speed(20)
colors = ["red","yellow","blue","green","purple","orange"]
for i in range(180):
    t.pencolor(colors[i%6])
    t.fd(i*2)
    t.right(61)
done()

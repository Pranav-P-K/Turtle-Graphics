from turtle import * # 2-D Flag
f = Turtle()
bgcolor('black')
f.speed(15)
f.penup()
f.goto(-300,100)
f.pendown()
f.pensize(10)
f.pencolor('orange')
f.fillcolor('orange')
f.begin_fill()
f.lt(90)
f.fd(200)
f.rt(90)
f.fd(600)
f.rt(90)
f.fd(200)
f.end_fill()
f.pencolor('white')
f.fillcolor('white')
f.begin_fill()
f.rt(90)
f.fd(600)
f.lt(90)
f.fd(200)
f.lt(90)
f.fd(600)
f.lt(90)
f.fd(200)
f.end_fill()
f.bk(200)
f.rt(90)
f.bk(300)
f.pencolor('blue')
f.circle(100)
f.penup()
f.lt(90)
f.fd(100)
f.pendown()
f.pensize(5)
for i in range(24):
    f.fd(85)
    f.bk(85)
    f.lt(15)
f.penup()
f.pensize(10)
f.bk(108)
f.lt(90)
f.pendown()
f.pencolor('green')
f.fillcolor('green')
f.bk(300)
f.fd(600)
f.begin_fill()
f.lt(90)
f.fd(200)
f.lt(90)
f.fd(600)
f.lt(90)
f.fd(200)
f.end_fill()
'''
#from turtle import * #3-D Flag
f = Turtle()
bgcolor('black')
f.lt(45)
for i in range(24):
    f.pensize(10)
    if (i<7):
        f.pencolor('orange')
    if (i>=7) and (i<12):
        f.pencolor('white')
    if (i>=12) and (i<19):
        f.pencolor('green')
    if (i>=19) and (i<24):
        f.pencolor('white')
    f.fd(100)
    f.rt(135)
    f.fd(50)
    f.bk(50)
    f.lt(135)
    f.bk(100)
    f.lt(15)
f.penup()
f.rt(135)
f.fd(40)
f.lt(90)
f.pendown()
f.pencolor('blue')
f.fillcolor('white')
f.begin_fill()
f.circle(40)
f.end_fill()
f.penup()
f.lt(90)
f.fd(40)
f.pensize(2)
f.pendown()
for i in range(24):
    f.fd(30)
    f.bk(30)
    f.lt(15)
'''

done()
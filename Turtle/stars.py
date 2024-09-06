import turtle
t=turtle.Turtle()
wd=turtle.Screen()
wd.bgcolor("Black")
t.speed(3)
    
def star(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor("Yellow")
    for i in range(5):
        t.forward(150)
        t.right(144)
    t.end_fill()
    t.up()
    t.home()
        
t.speed(10)
t.pensize(2)
star(0,0)
star(200,200)
star(-200,200)
star(-200,-200)
star(200,-200)

turtle.done()

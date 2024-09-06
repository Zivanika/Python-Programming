import turtle
t=turtle.Turtle()

def circle(x,y,color,rad):
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(rad)
    t.end_fill()
    t.up()
    t.home()
    
t.speed(10)
t.pensize(2)
circle(0,-50,"Green",50)
circle(100,100,"Orange",50)
circle(-100,100,"Blue",50)
circle(-100,-100,"Red",-50)
circle(100,-100,"Yellow",-50)

turtle.done()

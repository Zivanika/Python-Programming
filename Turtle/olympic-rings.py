import turtle
t=turtle.Turtle()

def circle(x,y,color):
    t.goto(x,y)
    t.down()
    t.color(color)
    t.pensize(6)
    t.circle(50)
    t.up()
    
t.speed(10)
colors=["red","green","black","yellow","blue"]
t.up()

circle(100,0,colors[0])
circle(50,-50,colors[1])
circle(0,0,colors[2])
circle(-50,-50,colors[3])
circle(-100,0,colors[4])

turtle.done()
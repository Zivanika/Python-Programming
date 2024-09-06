import turtle
t=turtle.Turtle()
t.speed(10)
t.up()
t.forward(10)
colors=["Green","Yellow","Red"]
for i in range(3):
    t.down()
    t.begin_fill()
    t.fillcolor(colors[i])
    t.circle(-40)
    t.end_fill()
    t.up()
    t.left(90)
    t.forward(100)
    t.right(90)
    
turtle.done()
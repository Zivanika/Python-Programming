import turtle
t=turtle.Turtle()
t.speed(10)
t.begin_fill()
t.fillcolor("Yellow")
t.circle(100,steps=3)
t.end_fill()
t.begin_fill()
t.circle(-100,steps=5) #use steps to make different shapes
t.fillcolor("Blue")
t.end_fill()
t.reset()
t.circle(100,extent=180)
turtle.done()
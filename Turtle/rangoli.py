import turtle
t=turtle.Turtle()
t.speed(10)

colors=["red","green","purple","blue","orange"]

for i in range(150):
    t.color(colors[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    # t.left(45)
    t.left(59)
    
#for spiral
# colors=["red","green","yellow","purple","blue","orange"]

# for i in range(150):
#     t.color(colors[i%6])
#     t.pensize(i/10+1)
#     t.forward(i)
#     # t.left(45)
#     t.left(59)
    
turtle.done()
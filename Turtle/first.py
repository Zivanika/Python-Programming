import turtle
import time
var=turtle.Turtle()
var.shape("turtle")
var.forward(200)
# help(turtle.shape) #  'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
var.color("Red","Green") #first para for line, 2nd for pointer
var.backward(300)
# turtle.colormode(255) #for RBG codes, by default it is 1
# var.color(255,255,255)
# var.forward(100)
# turtle.shape("turtle")
# turtle.forward(200)
# turtle.color("Red","Green")
# turtle.forward(100)

wn=turtle.Screen()
wn.bgcolor("Black")
wn.title("Ekansh")
var.circle(100)
var.forward(300)
var.circle(100)
# time.sleep(3)
turtle.done()

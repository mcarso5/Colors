#initialization
import turtle
import random

t = turtle.Turtle()
t.left(90)

#functions
def randomDot():
    t.color("teal")
    t.begin_fill()
    t.circle(100)
    t.end_fill()
#main
randomDot()

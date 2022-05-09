import turtle as t
from turtle import *
import random
tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

"""Drawing a spirograph turning 5 degrees at a time"""
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

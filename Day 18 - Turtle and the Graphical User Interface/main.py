from turtle import Screen
import turtle as t
import random

jimmy = t.Turtle()
t.colormode(255)
jimmy.shape('turtle')
jimmy.color('black')
jimmy.speed("fastest")


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        jimmy.color(random_color())
        jimmy.circle(100)
        jimmy.setheading(jimmy.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()


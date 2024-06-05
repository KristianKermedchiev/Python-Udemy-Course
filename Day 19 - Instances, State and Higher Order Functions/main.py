from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race, red, blue, orange, purple "
                                                          "or green? Enter a color: ")


colors = ["red", "blue", "green", "purple", "orange"]
all_turtles = []


for i in range(5):
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x=-240, y=(-100 + i * 50))
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle won!")
            else:
                print(f"You've lost! The {winning_color} turtle won!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

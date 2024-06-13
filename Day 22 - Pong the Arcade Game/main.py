from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from middle_line import MiddleLine

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((345, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
middle_line = MiddleLine()
middle_line.draw_line()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle

    if ball.distance(r_paddle) < 40 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.add_point("left")
    elif ball.xcor() < -390:
        ball.reset_position()
        scoreboard.add_point("right")

screen.exitonclick()

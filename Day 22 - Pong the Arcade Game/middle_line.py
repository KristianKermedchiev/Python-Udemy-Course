from turtle import Turtle

class MiddleLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, 300)  # Start position (top of the screen)
        self.setheading(270)  # Point the turtle downwards

    def draw_line(self):
        for _ in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

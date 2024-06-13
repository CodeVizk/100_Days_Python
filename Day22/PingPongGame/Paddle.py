from turtle import Turtle
LEFT = (-350, 0)
RIGHT = (350, 0)

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)


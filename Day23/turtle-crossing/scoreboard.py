from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-260, 250)
        self.write(f"Level {self.level}", align="left", font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level {self.level}", align="left", font=FONT)
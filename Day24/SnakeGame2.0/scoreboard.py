from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Snake_data.txt") as scores:
            self.highest_score = int(scores.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score {self.highest_score} ", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.highest_score < self.score:
            self.highest_score = self.score
            with open("Snake_data.txt", mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

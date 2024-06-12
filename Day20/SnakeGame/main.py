# Creating a snake game using turtle graphics
# This is not the final version of the game in this we are only creating a snake and moving it with keyboards inputs
import time
from snake import Snake

from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(fun=snake.up, key="Up",)
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.03)
    snake.move()
screen.exitonclick()

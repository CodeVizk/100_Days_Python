# Creating a snake game using turtle graphics
import time
from snake import Snake

from turtle import Screen
import food
import scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


food = food.Food()
score = scoreboard.Scoreboard()
snake = Snake()


screen.listen()
screen.onkey(fun=snake.up, key="Up",)
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


is_game_on = True
while is_game_on:
    screen.update()

    time.sleep(0.1)
    snake.move()

#     detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.refresh_score()
        snake.extend_segment()
#     Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        score.game_over()
#     Detect collision with tail
#     if head collide with any segment then trigger game over
    for segments in snake.snake_body[1:]:
        if snake.head.distance(segments) < 7:
            is_game_on = False
            score.game_over()

screen.exitonclick()

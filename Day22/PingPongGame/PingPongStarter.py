import time
import turtle as t
from Paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")

t.tracer(0)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    t.update()
    ball.move()

    # Detect collision with top and bottom wall
    if ball.ycor() < -285 or ball.ycor() > 285:
        ball.bounce_y()
    # Detect collision with paddle
    elif ball.xcor() >= 330 and ball.distance(r_paddle) < 50 or ball.xcor() >= -390 and ball.distance(l_paddle) < 30:
        ball.bounce_x()

    # Detect if ball misses
    elif ball.xcor() == 370:
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() == -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()

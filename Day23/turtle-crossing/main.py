import time

from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()

player = Player()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkeypress(player.move, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()



    # detect finish line
    player.finished()

    # update level
    if player.ycor() == 280:
        scoreboard.update_level()
        car.move_speed()
    # elif car.collide():
    #     car.reset()

    # detect collision with cars




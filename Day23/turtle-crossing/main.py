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
screen.onkeypress(player.go_up, "Up")

while game_is_on:
    time.sleep(0.05)
    screen.update()
    car.create_car()
    car.move_cars()

    # update level and increase speed
    if player.crossed_finish_line():
        scoreboard.update_level()
        player.go_to_start()
        car.move_speed()

    # detect collision with cars
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False






screen.exitonclick()

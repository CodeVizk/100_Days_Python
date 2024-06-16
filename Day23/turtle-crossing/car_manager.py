import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        spawn_chance = random.randint(1, 6)
        if spawn_chance == 6 :
            new_car = Turtle()
            new_car.shape("square")
            new_car.color("black")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-230, 230)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def move_speed(self):
        self.car_speed += MOVE_INCREMENT


import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        # self.increase_speed()/

    def move_speed(self):
        self.move_speed = STARTING_MOVE_DISTANCE
        self.move_speed += MOVE_INCREMENT
        for cars in self.all_cars:
            cars.backward(self.move_speed)



    def create_car(self):
        spawn_chance = random.randint(1, 6)
        if spawn_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-230, 230)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for cars in self.all_cars:
            cars.backward(STARTING_MOVE_DISTANCE)



    def reset(self):
        random_y = random.randint(-230, 230)
        for cars in self.all_cars:
            cars.goto(300, random_y)

    def collide(self):
        for cars in self.all_cars:
            cars.distance()



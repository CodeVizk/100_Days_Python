# Creating a spirograph using turtle graphics

import turtle as t
import random
t.colormode(255)

jim = t.Turtle()

jim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color




def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        jim.color(random_color())
        jim.circle(120)
        jim.setheading(jim.heading()+ size_of_gap)

draw_spirograph(int(input("How many gaps? ")))


my_screen = t.Screen()
my_screen.exitonclick()

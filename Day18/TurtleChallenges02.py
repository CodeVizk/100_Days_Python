# creating a random walk turtle
import turtle as t
import random
t.colormode(255)

jim = t.Turtle()

jim.width(15)
jim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color


direction = [0, 90, 270, 180]

for _ in range(200):

    jim.color(random_color())
    jim.setheading(random.choice(direction))
    jim.forward(30)





my_screen = t.Screen()
my_screen.exitonclick()
# Using Turtle graphics documentation
# Use different methods of turtle class
import turtle as t

jim = t.Turtle()
jim.shape("turtle")
jim.color("red")


# Challenge 1-
# Make a dashed line
for i in range(20):
    jim.forward(7)
    jim.penup()
    jim.forward(7)
    jim.pendown()

# Resetting the turtle clearing the dashed line by clear() and returning thr turtle to base position
# using home() which sends it to coordinates (0,0)
jim.home()
jim.clear()


# Challenge 2-
# Drawing a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
import random
colors = ["HotPink", "darkOrange", "gold", "DarkOrchid1", "Chartreuse1", "Firebrick1", "DeepSkyBlue",
          "coral4"]


def draw_shape(sides):
    angles_n = 360/sides
    for _ in range(sides):
        jim.forward(100)
        jim.right(angles_n)


for shape_size in range(3, 11):
    jim.color(random.choice(colors))
    draw_shape(shape_size)


my_screen = t.Screen()
my_screen.exitonclick()

# Extracting colours from an image using colorgram module to make a hist painting
import turtle
import turtle as t
import random
jim = t.Turtle()
jim.speed("fastest")
jim.hideturtle()
jim.penup()
# import colorgram
# colors = colorgram.extract('image.jpg',30)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_tuple = (r, g, b)
#     color_list.append(new_tuple)
# print(color_list)
turtle.colormode(255)
color_list = [(207, 155, 102), (57, 107, 128), (162, 82, 43), (125, 79, 97), (122, 156, 171),
              (126, 175, 159), (195, 142, 39), (226, 198, 130), (188, 89, 109), (191, 131, 145),
              (14, 44, 57), (53, 38, 19), (51, 164, 128), (59, 121, 114), (218, 90, 70), (159, 22, 32),
              (41, 31, 33), (8, 30, 28), (81, 146, 165), (238, 167, 162), (156, 28, 21), (23, 80, 91),
              (233, 168, 173), (173, 206, 188), (106, 126, 157), (26, 87, 84)]


y_coordinate = 50


def horizontal_painter():

    jim.dot(20, random.choice(color_list))
    jim.forward(50)


def vertical_painter():
    jim.setx(-194.45436482630055)
    jim.sety(-194.45436482630058 + y_coordinate)


jim.setheading(225)
jim.forward(275)
print(jim.heading())
print(jim.xcor(), jim.ycor())
jim.setheading(0)
for x in range(10):
    for _ in range(10):
        horizontal_painter()

    vertical_painter()
    y_coordinate += 50


# Another method
# before using this move the turtle to (0,0) first
# jim.setheading(225)
# jim.forward(300)
# jim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     jim.dot(20, random.choice(color_list))
#     jim.forward(50)
#
#     if dot_count % 10 == 0:
#         jim.setheading(90)
#         jim.forward(50)
#         jim.setheading(180)
#         jim.forward(500)
#         jim.setheading(0)


my_screen = t.Screen()
my_screen.exitonclick()

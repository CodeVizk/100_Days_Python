# we can give inputs with keyboards and control our turtle using listen

# Here is an etch-a-sketch game project
import turtle as t

jim = t.Turtle()


def move_forward():
    jim.forward(10)


def move_backwards():
    jim.back(10)


def move_left():
    jim.left(10)


def move_right():
    jim.right(10)


def clear():
    jim.penup()
    jim.clear()
    jim.home()
    jim.pendown()


screen = t.Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()

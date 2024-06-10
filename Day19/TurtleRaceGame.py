from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_dist = 0
for x in colors:

    new_turtle = Turtle(shape="turtle")
    new_turtle.color(x)
    new_turtle.penup()
    new_turtle.goto(x=-235, y=-90 + y_dist)
    y_dist += 35
    all_turtles.append(new_turtle)


is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 223:
            winner = turtle.pencolor()
            is_race_on = False
            if winner == user_bet:
                print(f"You won! the {winner} turtle is the winner. ")
            else:
                print(f"You lost! the {winner} turtle is the winner. ")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()

import turtle as t
import pandas as pd

# Retrieving states name and coordinates
all_states = pd.read_csv("50_states.csv")
check_state = all_states["state"].tolist()


screen = t.Screen()
screen.title("U.S States Games")
img = "blank_states_img.gif"
screen.addshape(img)
t.shape(img)


guessed_state = []

while len(guessed_state) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_state)}/50 States.", prompt="What's another state's name?").title()
    print(user_answer)
    if user_answer == "Exit":
        missed_state = [states for states in check_state if states not in guessed_state]
        missing_state = pd.DataFrame(missed_state)
        missing_state.to_csv("missing state.csv")
        break
    if user_answer in check_state:
        state_data = all_states[all_states.state == user_answer]
        jim = t.Turtle()
        jim.penup()
        jim.hideturtle()
        jim.goto(int(state_data.x), int(state_data.y))
        jim.write(state_data.state.item())
        guessed_state.append(user_answer)

screen.exitonclick()

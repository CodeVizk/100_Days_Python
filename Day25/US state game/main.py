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
        break
    if user_answer in check_state:
        state_data = all_states[all_states.state == user_answer]
        jim = t.Turtle()
        jim.penup()
        jim.hideturtle()
        jim.goto(int(state_data.x), int(state_data.y))
        jim.write(state_data.state.item())
        guessed_state.append(user_answer)


missed_state = []
# missed states to go in csv
for i in range(50):
    if check_state[i] not in guessed_state:
        missed_state.append(check_state[i])

missing_state = pd.DataFrame(missed_state)
missing_state.to_csv("missing state.csv")

screen.exitonclick()
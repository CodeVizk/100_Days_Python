from tkinter import *


def button_click():
    print("Clicked")


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

window = Canvas(width=215, height=255, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")

window.create_image(100, 130, image=tomato_img)
window.grid(column=1, row=1)

window.create_text(100, 145, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)
window.grid(column=1, row=1)

start_button = Button(text="Start", command=button_click, font=(FONT_NAME, 8, "bold"), highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=button_click, font=(FONT_NAME, 8, "bold"), highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmark = Label(text="✓", fg="green", bg=YELLOW, font=10)
checkmark.grid(column=1, row=3)

window.mainloop()

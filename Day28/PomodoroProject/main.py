from tkinter import *
import math




# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_button_click():
    window.after_cancel(timer)
    global reps
    reps = 0
    checkmark.config(text="")
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_min)
        timer_label.config(text="BRAKE", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_min)
        timer_label.config(text="BRAKE", fg=PINK)
    else:
        count_down(work_min)
        timer_label.config(text="WORK", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=215, height=255, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(100, 130, image=tomato_img)
canvas.grid(column=1, row=1)

timer_text = canvas.create_text(100, 145, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark=""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✓"
        checkmark.config(text=mark)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, font=(FONT_NAME, 8, "bold"), highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_button_click, font=(FONT_NAME, 8, "bold"), highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmark = Label(fg="green", bg=YELLOW, font=10)
checkmark.grid(column=1, row=3)

window.mainloop()

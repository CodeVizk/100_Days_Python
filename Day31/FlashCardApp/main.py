from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card ")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=1, row=1)

flash_card_front = PhotoImage(file="images/card_front.png")
flash_canvas = Canvas(highlightthickness=0, bg="white")
flash_canvas.create_image(800, 526, image=flash_card_front)
flash_canvas.grid(column=0, row=0, columnspan=2)


language_label = Label(text="French", font=("Ariel", 20, "italic"))
language_label.place(x=400, y=250)
language_label.grid(column=0, row=0, columnspan=2)














mainloop()
from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

lang_data = pandas.read_csv("data/french_words.csv")
lang_data.to_dict(orient="records")
print(lang_data)
def french_words():
    f_words = random.choice(lang_data)
    flash_canvas.create_text(400, 263, text=f"{f_words}", font=("Ariel", 60, "bold"))


window = Tk()
window.title("Flash Card ")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0, command=french_words)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

flash_card_front = PhotoImage(file="images/card_front.png")
flash_canvas = Canvas(highlightthickness=0, bg=BACKGROUND_COLOR, width=800, height=526)
flash_canvas.create_image(400, 263, image=flash_card_front)
flash_canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
# flash_canvas.create_text(400, 263, text=f"{f_words}", font=("Ariel", 60, "bold"))
flash_canvas.grid(column=0, row=0, columnspan=2)
















mainloop()
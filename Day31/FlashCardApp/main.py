from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
word_list = {}
data_list = {}

try:
    lang_data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_list = original_data.to_dict(orient="records")
else:
    data_list = lang_data.to_dict(orient="records")


def french_words():
    global word_list, flip_timer
    window.after_cancel(flip_timer)
    word_list = random.choice(data_list)
    flash_canvas.itemconfig(bg_img, image=flash_card_front)
    flash_canvas.itemconfig(card_title, text="French", fill="black")
    flash_canvas.itemconfig(card_word,  text=f"{word_list["French"]}", fill="black")
    flip_timer = window.after(3000, eng_words)


def eng_words():
    flash_canvas.itemconfig(bg_img, image=flash_card_back)
    flash_canvas.itemconfig(card_title, text="English", fill="white")
    flash_canvas.itemconfig(card_word, text=f"{word_list["English"]}", fill="white")


def correct_ans():
    data_list.remove(word_list)
    learned_word = pandas.DataFrame(data_list)
    learned_word.to_csv("data/words_to_learn.csv", index=False)
    french_words()


window = Tk()
window.title("Flash Card ")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, eng_words)



right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0, command=correct_ans)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=french_words)
wrong_button.grid(column=0, row=1)

flash_card_back = PhotoImage(file="images/card_back.png")
flash_card_front = PhotoImage(file="images/card_front.png")
flash_canvas = Canvas(highlightthickness=0, bg=BACKGROUND_COLOR, width=800, height=526)

bg_img = flash_canvas.create_image(400, 263, image=flash_card_front)

card_title = flash_canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = flash_canvas.create_text(400, 263, text=f"", font=("Ariel", 60, "bold"))
flash_canvas.grid(column=0, row=0, columnspan=2)

french_words()

mainloop()

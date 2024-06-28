# Miles to Km project
from tkinter import *

window = Tk()
window.title("Mile to KM converter")
window.config(padx=20, pady=15)


def convert():
    km = float(miles_entry.get())
    answer = round(km * 1.609)
    result_label.config(text=f"{answer}")


# creating an entry box to get miles input
miles_entry = Entry(width=5)
miles_entry.insert(END, string="0")
miles_entry.grid(column=1, row=0)


# creating all labels
label = Label(text="Miles")
label.grid(column=2, row=0)

label2 = Label(text="is equal to ")
label2.grid(column=0, row=1)

label3 = Label(text="Km")
label3.grid(column=2, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)


# creating a button to start calculating
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=3)


mainloop()

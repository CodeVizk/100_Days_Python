from tkinter import *


# there are three layout manager
# pack()  - not precise placement / limited option = left, right, top, bottom
# place() - precise placement / enter the x, y coordinate
# grid()  - easy to use / divide the window into rows and columns

def button_click():
    print("I got clicked")
    my_label.config(text=input.get())


window = Tk()
window.title("GUI program")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

# label
my_label = Label(text="I am a Label", font=("Arial", 24, "italic"))

# my_label.pack(side='bottom')
# my_label.place(x=100, y=150)
my_label.grid(column=0, row=0)
my_label.config(padx=25, pady=25)
# Button
my_button = Button(text="Click me!", command=button_click)
new_button = Button(text="New_button", command=button_click)
# my_button.pack()
my_button.place(x=10, y=90)
my_button.grid(column=1, row=1)
new_button.grid(column=2, row=0)
# Entry
input = Entry(width=10)

# input.pack()
# input.place(x=70, y=70)
input.grid(column=3, row=2)
mainloop()

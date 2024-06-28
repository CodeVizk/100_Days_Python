from tkinter import *

window = Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="I am a Label", font=("Arial", 24, "italic"))
# to display our label we need to use pack() function
my_label.pack()

my_label["text"] = "new text"
# or
my_label.config(text="new text")

# Button


def button_click():
    print("I got clicked")
    my_label.config(text=input.get())
    print("YOOO")


my_button = Button(text="Click me!", command=button_click)
my_button.pack()

# Entry
input = Entry(width=10)
input.pack()

# we can store the input using get function


mainloop()

import tkinter

window = tkinter.Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "italic"))
# to display our label we need to use pack() function
my_label.pack()


tkinter.mainloop()



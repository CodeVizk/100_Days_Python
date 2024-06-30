from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)

# Logo
lock_img = PhotoImage(file="logo.png")
canvas.create_image (100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Buttons
generate_pass = Button(text="Generate Password")
generate_pass.grid(column=2, row=3)

add_button = Button(text="Add", width=36)
add_button.grid(column=1, columnspan=2, row=4)

# Entries
website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=36)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

mainloop()

from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg="black")
window.title("Password Manager")

canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)

# Logo
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg="black", fg="white")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", bg="black", fg="white")
username_label.grid(column=0, row=2)

password_label = Label(text="Password: ", bg="black", fg="white")
password_label.grid(column=0, row=3)


# Buttons
generate_pass = Button(text="Generate Password", font=("aerial", 7))
generate_pass.grid(column=2, row=3, padx=(4, 0), ipady=0, sticky="EW")

add_button = Button(text="Add", width=35, font=("aerial", 8))
add_button.grid(column=1, columnspan=2, row=4, sticky="WE", pady=(4, 0))

# Entries
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="WE", pady=4)

username_entry = Entry(width=36)
username_entry.grid(column=1, row=2, columnspan=2, sticky="WE", pady=4)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW", pady=4)

mainloop()

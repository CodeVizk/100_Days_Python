from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_num = [choice(numbers) for _ in range(randint(2, 4))]
    password_sym = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters+password_sym+password_num
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web_name = website_entry.get()
    user_email = username_entry.get()
    user_pass = password_entry.get()

    if len(web_name) == 0 or len(user_pass) ==0 or len(user_email) == 0:
        empty_fields = messagebox.showwarning(title="OOPS!", message="Please, don't leave empty fields!!")
    else:
        is_ok = messagebox.askokcancel(title=web_name, message=f"These are the details entered.\nEmail: {user_email}"f"\nPassword: "
                                                               f"{user_pass}\nIs it ok to save? ")

        if is_ok:
            with (open("data.txt", mode="a") as data):
                data.write(f"{web_name} | {user_email} | {user_pass}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


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
generate_pass = Button(text="Generate Password", font=("aerial", 7), command=pass_gen)
generate_pass.grid(column=2, row=3, padx=(4, 0), ipady=0, sticky="EW")

add_button = Button(text="Add", width=35, font=("aerial", 8), command=save)
add_button.grid(column=1, columnspan=2, row=4, sticky="WE", pady=(4, 0))

# Entries
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="WE", pady=4)
website_entry.focus()

username_entry = Entry(width=36)
username_entry.grid(column=1, row=2, columnspan=2, sticky="WE", pady=4)
username_entry.insert(0, "vivek223singh@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW", pady=4)

mainloop()

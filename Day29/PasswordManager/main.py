from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import pandas
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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


def search_password():
    web_name = website_entry.get()
    if len(web_name) == 0:
        messagebox.showwarning(title="OOPS!", message="Please, don't leave empty fields!!")
    else:
        try:
            with open("data.json", "r") as search_file:
                data = json.load(search_file)

        except FileNotFoundError:
            messagebox.showinfo("Error", "No data file found")
        else:
            if web_name in data:
                user_email = data[web_name]["email"]
                user_pass = data[web_name]["password"]
                messagebox.showinfo(web_name, f"Email: {user_email}\nPassword: {user_pass}")
            else:
                messagebox.showinfo("Not Found", "The searched website is not found")
        finally:
            website_entry.delete(0, END)


def save():
    web_name = website_entry.get()
    user_email = username_entry.get()
    user_pass = password_entry.get()
    new_data = {
        web_name: {
                "email": user_email,
                "password": user_pass
        }
    }

    if len(web_name) == 0 or len(user_pass) == 0:
        messagebox.showwarning(title="OOPS!", message="Please, don't leave empty fields!!")
    else:
        try:
            with open("data.json", "r") as save_data:
                # Reading old data
                data = json.load(save_data)

        except FileNotFoundError:
            with open("data.json", "w") as save_data:
                json.dump(new_data, save_data, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as save_data:
                # Saving updated data
                json.dump(data, save_data, indent=4)
        finally:
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
generate_pass = Button(text="Generate Password", font=("aerial", 7), pady=-1, command=pass_gen)
generate_pass.grid(column=2, row=3, padx=(4, 0), sticky="EW")

add_button = Button(text="Add", width=35, font=("aerial", 8), command=save)
add_button.grid(column=1, columnspan=2, row=4, sticky="WE", pady=(4, 0))

search_button = Button(text="Search", font=("aerial", 7), pady=-1, command=search_password)
search_button.grid(column=2, row=1, sticky="we", padx=(5, 0))

# Entries
website_entry = Entry()
website_entry.grid(column=1, row=1, sticky="WE", pady=4)
website_entry.focus()

username_entry = Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky="WE", pady=4)
username_entry.insert(0, "CodeVizk@gmail.com")

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW", pady=4)

mainloop()

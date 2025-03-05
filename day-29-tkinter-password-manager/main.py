from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    random_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    random_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = random_numbers + random_symbols + random_letters

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if not website or not email or not password:
        messagebox.showwarning(title="Input required", message="You need to fill all entries first")
        return

    # is_user_ok = messagebox.askokcancel(title="", message=f"There are the details entered: \nEmail: {email.get()}\nWebsite: {website.get()}\nPassword: {password.get()}\nIs it ok to save?")

    # if not is_user_ok:
    #     website.focus()
    #     return

    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", mode="w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        # data = json.load(data_file)
        # Updating old data with new data
        data.update(new_data)
        with open("data.json", "w") as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)
            # print(data)
    finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pw_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pw_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "eavera97@gmail.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Buttons

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ----------------------------- SEARCH WEBSITES --------------------------------- #

def find_password():
    site = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            site_dict = data[site]
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="No data file found")
    except KeyError:
        messagebox.showinfo(title=site, message=f"Website, {site} not found")
    else:
        user = site_dict["username"]
        passwd = site_dict["password"]
        if site in data:
            messagebox.showinfo(title=site, message=f"Username: {user}\nPassword: {passwd}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for char in range(nr_letters)]
    symbol_list = [random.choice(symbols) for char in range(nr_symbols)]
    number_list = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Password Copied", message="Password is copied to clipboard")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():
    data_list = [website_entry.get(), username_entry.get(), password_entry.get()]
    new_data = {
        data_list[0]:
            {
                "username": data_list[1],
                "password": data_list[2]
            }
    }
    if len(data_list[0]) < 1:
        messagebox.showinfo(title="Website", message="Must Enter Website")
    elif len(data_list[1]) < 1:
        messagebox.showinfo(title="Username", message="Must Enter Username")
    elif len(data_list[2]) < 1:
        messagebox.showinfo(title="Password", message="Must Enter Password")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50)

# image ------------------------------------------------------------------------------------------

canvas = Canvas(screen, width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0, padx=20, pady=20)

# labels ------------------------------------------------------------------------------------------

website = Label(screen, text="Website: ")
username = Label(screen, text="Email/Username: ")
password = Label(screen, text="Password: ")
website.grid(column=0, row=1, sticky=E)
username.grid(column=0, row=2, sticky=E)
password.grid(column=0, row=3, sticky=E)

# entries ------------------------------------------------------------------------------------------\

website_entry = Entry(screen, width=30)
username_entry = Entry(screen, width=49)
password_entry = Entry(screen, width=30)
website_entry.focus()
username_entry.insert(0, "hassenmayerr@gmail.com")
website_entry.grid(column=1, row=1, pady=3)
username_entry.grid(column=1, row=2, columnspan=2, pady=3)
password_entry.grid(column=1, row=3, pady=3)

# buttons -------------------------------------------------------------------------------------------

search = Button(screen, text="Search", width=16, command=find_password)
new_password = Button(screen, text="Generate Password", command=generate_password)
save_password = Button(screen, text="add", width=46, highlightthickness=0, command=save_entry)
search.grid(column=2, row=1, pady=3)
new_password.grid(column=2, row=3, pady=3)
save_password.grid(column=1, row=5, columnspan=2, pady=3)

screen.mainloop()




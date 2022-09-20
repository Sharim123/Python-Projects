import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers


    shuffle(password_list)
    password = "".join(password_list)
    input_password.insert(0, f'{password}')
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    password = input_password.get()
    email = input_email.get()
    new_data = {
        website: {
            "email":email,
            "password":password,
             }
    }


    if website == "" or password == "":
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', "r") as file:
                data = json.load(file)
                print(data)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
                print(file)
        finally:
            website_input.delete(0, END)
            input_password.delete(0, END)


#---------------------------Search-------------------------------------#

def find_password():
    website = website_input.get()

    try:
        with open('data.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="This data file doesn't exist")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist")








# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, background="White", highlightthickness=0)
lock = PhotoImage(file='logo - Copy.png')
canvas.create_image(100, 112, image=lock)
canvas.grid(column=2, row=0)

website = Label(text="Website:")
website.grid(column=1, row=5)

website_input = Entry(width=35)
website_input.grid(row=5, column=2, columnspan=2)
website_input.focus()

email = Label(text="Email/Username:")
email.grid(column=1, row=6)

input_email = Entry(width=35)
input_email.grid(row=6, column=2)
input_email.insert(0, "sharim@gmail.com")

password = Label(text="Password:")
password.grid(column=1, row=7)

input_password = Entry(width=21)
input_password.grid(row=7, column=2)


gen_password = Button(text="Generate Password", command=generate_password)
gen_password.grid(row=7, column=3)


Add = Button(text='Add', width=36, command=save)
Add.grid(row=8, column=2, columnspan=2)


Search = Button(text="Search", command=find_password)
Search.grid(row=5, column=3)


window.mainloop()